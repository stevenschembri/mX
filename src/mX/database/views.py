from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView
from .models import Aircraft, AircraftType, AircraftMajorAssembly, Customer, Station
from .forms import CustomerCreateForm, AircraftCreateForm
# customer
# aircraft
# checks
# company-data


# Create your views here.
class DatabaseHomePageView(TemplateView):
	template_name = "database/database_home.html"

class DatabaseCustomerView(ListView):
	def get_queryset(self):
		return Customer.objects.all()

class DatabaseCustomerAddView(CreateView):
	form_class = CustomerCreateForm
	template_name = 'database/customer_create.html'

class DatabaseCustomerDetailView(DetailView):
	def get_queryset(self):
		return Customer.objects.all()

class DatabaseAircraftView(ListView):
	def get_queryset(self):
		return Aircraft.objects.all()

class DatabaseAircraftAddView(CreateView):
	form_class = AircraftCreateForm
	template_name = 'database/aircraft_create.html'

class DatabaseAircraftDetailView(DetailView):
	def get_queryset(self):
		return Aircraft.objects.all()