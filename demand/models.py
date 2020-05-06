from django.db import models
from django.core import validators
from employee.models import Employee
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Channel(models.TextChoices):
    ROLB = 'rolb', 'ROLB'
    MCA = 'mca', 'MCA'
    BMB = 'bmb', 'BMB'


class Demand(models.Model):
    pwr = models.CharField(
        'PWR', unique=True, max_length=10,
        validators=[
            validators.RegexValidator('^PWR(\d){1,7}$', message="PWR should start with 'PWR'")
        ]
    )

    channel = models.CharField(max_length=10, choices=Channel.choices, default='')
    release = models.CharField(max_length=10)
    description = models.TextField(max_length=300)

    estimated_design_cost = models.DecimalField(max_digits=20, decimal_places=2)
    estimated_build_cost = models.DecimalField(max_digits=20, decimal_places=2)
    estimated_test_cost = models.DecimalField(max_digits=20, decimal_places=2)
    estimated_support_cost = models.DecimalField(max_digits=20, decimal_places=2)
    estimated_delivery_cost = models.DecimalField(max_digits=20, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'demand'

    def __str__(self):
        return self.release + ' | ' + self.channel + ' | ' + self.pwr


class AllocationTypes(models.IntegerChoices):
    ALLOCATE_100 = 8, '8 hours'
    ALLOCATE_50 = 4, '4 hours'


class AssignmentRoles(models.TextChoices):
    BUILD = 'build', 'BUILD'
    DESIGN = 'design', 'DESIGN'
    SUPPORT = 'support', 'SUPPORT'
    TEST = 'test', 'TEST'


class Assignment(models.Model):
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    demand = models.ForeignKey(
        Demand, null=True, on_delete=models.CASCADE, related_name='assignments'
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    allocation = models.IntegerField(choices=AllocationTypes.choices)
    role = models.CharField(max_length=10, choices=AssignmentRoles.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'assignment'

    def __str__(self):
        return self.role + ' | ' + self.employee.name + ' | ' + self.demand.description

    def clean(self, *args, **kwargs):
        # run the base validation
        super(Assignment, self).clean(*args, **kwargs)

        # Don't allow dates older than now.
        if self.start_date and self.start_date < timezone.now():
            raise ValidationError('Start date/time must be later than current date/time.')

        # Don't allow end_date older start_date
        if self.start_date and self.end_date and self.end_date < self.start_date:
            raise ValidationError('End date/time must be later than start date/time.')


class Holiday(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'holiday'

    def __str__(self):
        return self.date + ' | ' + self.name
