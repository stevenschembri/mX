from django.db import models
from django.core.urlresolvers import reverse



# Customer
class Customer(models.Model):
	name 				 = models.CharField(max_length = 200, blank = False, null = False)
	contact_person 		 = models.CharField(max_length = 100, blank = True, null = True)
	email 				 = models.EmailField(max_length=254, blank = True, null = True)
	notes 				 = models.TextField(blank = True, null = True)
	billing_address 	 = models.TextField(blank = True, null = True)
	shipping_address 	 = models.TextField(blank = True, null = True)
	timestamp			 = models.DateTimeField(auto_now_add=True)
	updated				 = models.DateTimeField(auto_now=True)
	hourly_rate_discount = models.DecimalField(max_digits=5, decimal_places=2, default = 0,blank = True, null = True)
	fixed_price_discount = models.DecimalField(max_digits=5, decimal_places=2, default = 0,blank = True, null = True)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("database:customer-detail", kwargs={'pk':self.pk})

# Aircraft Type
class AircraftType(models.Model):
	name 				= models.CharField(max_length = 100, blank = False, null = False)
	official_designation= models.CharField(max_length = 100, blank = True, null = True)
	type_certificate	= models.CharField(max_length = 100, blank = True, null = True)
	# Add Default to below hourly_rate??
	hourly_rate			= models.DecimalField(decimal_places=2, max_digits=8, blank = True, null = True)

	def __str__(self):
		return self.name

# Engines / APUs
class AircraftMajorAssembly(models.Model):
	assembly_name 		= models.CharField(max_length = 100, blank = False, null = False)
	part_number 		= models.CharField(max_length = 20, blank = False, null = False)
	serial_number 		= models.CharField(max_length = 20, blank = False, null = False)
	delta_hours 		= models.DecimalField(max_digits=8, decimal_places=2, default = 0) #Difference between Assembly and Airframe Hours

	def __str__(self):
		return self.assembly_name
# Aircraft
class Aircraft(models.Model):
	serial_number 		= models.CharField(max_length = 20, blank = False, null = False)
	registration 		= models.CharField(max_length = 10, blank = False, null = False)
	major_assemblies 	= models.ManyToManyField(AircraftMajorAssembly)
	aircraft_type		= models.ForeignKey(AircraftType)
	notes 				= models.TextField(blank = True, null = True)
	customer 			= models.ForeignKey(Customer)

	def get_absolute_url(self):
		return reverse("database:aircraft-detail", kwargs={'pk':self.pk})

	def __str__(self):
		return self.registration
# Stations
class Station(models.Model):
	name 					= models.CharField(max_length = 50, blank = False, null = False)
	code 					= models.CharField(max_length = 3, blank = False, null = False)
	shipping_address 		= models.TextField(blank = True, null = True)
	last_workorder_number	= models.IntegerField(default = 0, blank = False, null =False)

	def __str__(self):
		return self.name

# Latest WO in the Station 
# class LatestWorkOrderNumber(models.Model):
# 	year = models.DateTimeField(blank = False, null = False)
# 	station = models.ForeignKey(Station)
# 	latest_workorder_number = models.IntegerField(default = 0, blank = False, null =False)


# class PlaceholderWorkOrders(models.Model):
# 	year = models.DateTimeField(blank = False, null = False)
# 	station = models.ForeignKey(Station)


# Company Information
#  | - Title
#  | - Website
#  | - Standard Hourly Rates 
#  | - Shipping Address
#  | - IBAN 
#  | - Billing Address
#  

# Task
#  | - Title
#  | - Aircraft
#  | - ATA
#  | - Planned Hours
#  | - Parts Required (Many to Many Field)
#  | - Fixed Price
#  | - Access (?)
#  | - 

# Access -- Too much? 
#  | - Panel
#  | - Aircraft
#  | - Time

# Check  -- How to account for prices when during check combination ?? (Split for Access and Tasks?)
#  | - Title
#  | - Aircraft
#  | - Price 
#  | - 
#  | - 
#  | - 
#  |
