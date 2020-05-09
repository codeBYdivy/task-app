from django.contrib import admin

from .models import Employee, EmployeeCalendar

# Register your models here.

admin.site.register(EmployeeCalendar)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['brid', 'name', 'designation']
    list_filter = ['designation', 'grade']
    search_fields = ['brid', 'name', 'email']
