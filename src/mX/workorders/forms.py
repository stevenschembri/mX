from django import forms
from .models import Task, WorkOrder


class TaskDetailForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = [
			'number',
			'name',
			'rectification',
			'hours'
		]

class WorkOrderCreateForm(forms.ModelForm):
	class Meta:
		model = WorkOrder
		fields = [
			'aircraft', 	
			'date_opened', 
			'station',		
			'status',  	
			'customer',	
			]

class TaskCreateForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = [
			'name', 	
			'ata_chapter',	
			'workorder',
			]
