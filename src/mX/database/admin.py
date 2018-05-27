from django.contrib import admin

from .models import Customer, AircraftType, AircraftMajorAssembly, Aircraft, Station
# Register your models here.
admin.site.register(Customer)
admin.site.register(AircraftType)
admin.site.register(AircraftMajorAssembly)
admin.site.register(Aircraft)
admin.site.register(Station)