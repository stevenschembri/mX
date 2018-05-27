from django.contrib import admin

from .models import WorkOrder, Task
# Register your models here.

admin.site.register(WorkOrder)
admin.site.register(Task)