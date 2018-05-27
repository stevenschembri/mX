from django.db import models
from database.models import Customer, AircraftType, AircraftMajorAssembly, Aircraft, Station
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

import datetime

# Note: A Work Order Number of '000-0000-0000' will indicate that pre_save did not work 
class WorkOrder(models.Model):

	WORKORDER_STATUS = (
	('ongoing', 'Ongoing'),
	('future', 'Future Project'),
	('rts', 'RTS Issued'),
	('closed', 'Closed'),
	)

	aircraft 			= models.ForeignKey(Aircraft)
	date_opened 		= models.DateTimeField(default = datetime.datetime.now, null=False, blank=False)
	number 				= models.CharField(max_length = 13, default = '000-0000-0000')
	station				= models.ForeignKey(Station)
	status  			= models.CharField(max_length = 50, choices=WORKORDER_STATUS, blank = False, null = False )
	customer			= models.ForeignKey(Customer)
	aircraftETA			= models.DateTimeField(null=True, blank=True)
	aircraftETD			= models.DateTimeField(null=True, blank=True)
	notes				= models.TextField(blank = True, null = True)

	def __str__(self):
		return self.number

	def get_absolute_url(self):
		return reverse("workorders:detail", kwargs={'number':self.number})


def workorder_pre_save_receiver(sender, instance, *args, **kwargs):
	try:
		# Filters all Open WO by comparing current new WO's date & station. Gets last Number by PK
		# Trims number to last digits 
		# Converts string to integer 
		# if the quesyset is found empty, the last_workorder_number will be 0 (except case)
		last_workorder_number = int(WorkOrder.objects.filter(date_opened__year = instance.date_opened.year)
			.filter(station = instance.station)
			.order_by('-pk')[0].number[-4:])
	except:
		# if the quesyset is found empty, the last_workorder_number will be 0
		last_workorder_number = 0 

	#IMP - IF '04d' IS CHANGED, CHANGE 4 ON ABOVE LINE AS WELL
	instance.number = f'{instance.station.code}-{instance.date_opened.year}-{(last_workorder_number+1):04d}' 

pre_save.connect(workorder_pre_save_receiver, sender = WorkOrder)

class Task(models.Model):
	workorder 			= models.ForeignKey(WorkOrder)
	ata_chapter			= models.TextField(blank = True, null = True)
	number 				= models.IntegerField(blank = False, null = False, default = 0)
	name 				= models.CharField(max_length=500)
	rectification 		= models.TextField(blank=True, null=True)
	date 				= models.DateTimeField(blank=True, null=True)
	hours 				= models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits=4)
	hours_invoiced		= models.DecimalField(blank=True, null=True, decimal_places = 2, max_digits=4)
	complete 			= models.BooleanField(default=False)
	locked 				= models.BooleanField(default=False)
	# attached files

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("workorders:task", kwargs={'pk':self.pk, 'number':self.workorder.number})

def task_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.number or instance.number == 0:
		try:
			last_task_number = Task.objects.filter(workorder=instance.workorder).latest('number').number
		except:
			last_task_number = 0 

		instance.number = last_task_number+1

pre_save.connect(task_pre_save_receiver, sender = Task)
