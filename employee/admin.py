from django.contrib import admin

# Register your models here.

from .models import Employee, EmployeeCalendar

admin.site.register(EmployeeCalendar)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['brid', 'name', 'designation']
    list_filter = ['designation', 'grade']
    search_fields = ['brid', 'name', 'email']
