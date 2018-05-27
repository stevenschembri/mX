from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from .models import WorkOrder, Task
from .forms import TaskDetailForm, WorkOrderCreateForm, TaskCreateForm
from database.models import Station


# - Work Orders Filtered List View - To amend to show Open/Closed Work Orders, rather than Stations
#   since the bulk of the work orders will be closed after some time
# - To add limit of how many work orders are listed in the query set

class TaskCreateView(CreateView):
	form_class = TaskCreateForm
	template_name = 'workorders/task_create.html'

	def get_initial(self):
		initial = super(TaskCreateView, self).get_initial()
		print(initial)
		print(self.kwargs.get("number"))
		initial["workorder"] = WorkOrder.objects.get(number=self.kwargs.get("number"))
		print(initial)
		return initial

class WorkOderCreateView(CreateView):
	form_class = WorkOrderCreateForm
	template_name = 'workorders/workorder_create.html'		

class WorkOderListView(ListView):
	def get_queryset(self):
		return WorkOrder.objects.all()
	
	def get_context_data(self, *args, **kwargs):
		context = super(WorkOderListView, self).get_context_data(*args, **kwargs)
		stations = Station.objects.all()
		context['stations'] = stations
		return context

class WorkOderFilteredListView(ListView):
	def get_queryset(self):
		if self.kwargs.get("sta") == "":
			return WorkOrder.objects.all()
		else:
			return WorkOrder.objects.filter(station__code__iexact = self.kwargs.get("sta"))
	
	def get_context_data(self, *args, **kwargs):
		context = super(WorkOderFilteredListView, self).get_context_data(*args, **kwargs)
		stations = Station.objects.all()
		context['stations'] = stations
		return context


class WorkOderDetailView(DetailView):

	def get_queryset(self):
		return WorkOrder.objects.all()

	def get_object(self, queryset = None):
		return get_object_or_404(WorkOrder, number=self.kwargs.get("number")) 

class TaskDetailView(UpdateView):
	form_class = TaskDetailForm
	template_name = 'workorders/task_detail.html'

	def get_queryset(self):
		return Task.objects.all()