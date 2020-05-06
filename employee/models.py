from django.db import models


class Employee(models.Model):
    brid = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    grade = models.CharField(max_length=10, blank=True, default='')
    designation = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.brid + ' | ' + self.name


class CalendarEvent(models.TextChoices):
    LEAVE = 'leave', 'LEAVE'
    TASK = 'task', 'TASK'


class EmployeeCalendar(models.Model):
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    category = models.CharField(max_length=20, choices=CalendarEvent.choices)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'calendar'
        verbose_name = 'Employee Calendar'
        verbose_name_plural = 'Employee Calendar'

    def __str__(self):
        return self.employee.name + ' | ' + self.start_date + ' | ' + self.end_date
