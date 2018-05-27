from django import forms
from .models import Customer, Aircraft


class CustomerCreateForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = [
			'name',
			'contact_person',
			'email',
			'notes',
			'billing_address',
			'shipping_address'
		]

class AircraftCreateForm(forms.ModelForm):
	class Meta:
		model = Aircraft
		fields = [
			'registration',
			'aircraft_type',
			'serial_number',
			'customer',
			'notes',
		]
