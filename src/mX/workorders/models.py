from django.db import models
from database.models import Customer, AircraftType, AircraftMajorAssembly, Aircraft, Station
from django.db.models.signals import pre_save, post_save

import datetime

# Create your models here.
class WorkOrder(models.Model):
	aircraft 			= models.ForeignKey(Aircraft)
	date_opened 		= models.DateTimeField(default = datetime.datetime.now, null=False, blank=False)
	number 				= models.CharField(max_length = 20)
	station				= models.ForeignKey(Station)
	status  			= models.CharField(max_length = 100, blank = False, null = False )
	customer			= models.ForeignKey(Customer)

	def __str__(self):
		return self.number

def workorder_pre_save_receiver(sender, instance, *args, **kwargs):
	work_orderyear = instance.date_opened.year
	try:
		##TO ADD STATION TO FILTER
		last_workorder_number = int(WorkOrder.objects.filter(date_opened__year = work_orderyear).filter(station = instance.station).order_by('-pk')[0].number[-4:]) #Takes latest WO (sorted by PK), trims last 4 digits and converts to INT. 
	except:
		last_workorder_number = 0 
	instance.number = f'{instance.station.code}-{instance.date_opened.year}-{(last_workorder_number+1):04d}' #IMP - IF '04d' IS CHANGED, CHANGE 4 ON ABOVE LINE AS WELL

# def workorder_post_save_receiver(sender, instance, *args, **kwargs):
# 	instance.station.last_workorder_number += 1
# 	instance.station.save()
# 	print('saved..')


pre_save.connect(workorder_pre_save_receiver, sender = WorkOrder)
# post_save.connect(workorder_post_save_receiver, sender = WorkOrder)



# work_orderyear = datetime.datetime.now().year
# try:
# 	##TO ADD STATION TO FILTER
# 	last_workorder_number = int(WorkOrder.objects.filter(date_opened__year = work_orderyear).order_by('-pk')[0].number[-4:]) #Takes latest WO (sorted by PK), trims last 4 digits and converts to INT. 
# except:
# 	last_workorder_number = 0 
# number = f'MLA-{{work_orderyear}}-{(instance.station.last_workorder_number+1):04d}'

