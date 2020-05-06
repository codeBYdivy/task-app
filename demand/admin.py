from django.contrib import admin
from .models import Assignment, Demand, Holiday

admin.site.register(Holiday)


@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    list_display = ['pwr', 'channel', 'release']
    list_filter = ['channel', 'release']
    search_fields = ['pwr', 'channel', 'release']


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['employee', 'demand', 'allocation', 'start_date', 'end_date']
    list_filter = ['demand__channel', 'demand__release']
    search_fields = ['employee__name']
