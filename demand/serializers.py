from rest_framework import serializers

from employee.models import Employee
from .models import Assignment, Demand


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'brid', 'name')


class AssignmentSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)

    # employee = serializers.CharField(source='employee.name', read_only=True)

    class Meta:
        model = Assignment
        fields = ('employee', 'demand', 'start_date', 'end_date', 'allocation', 'role')


class DemandSerializer(serializers.ModelSerializer):
    assignments = AssignmentSerializer(many=True, read_only=True)

    class Meta:
        model = Demand
        fields = (
            'id', 'pwr', 'channel', 'release', 'description', 'estimated_design_cost',
            'estimated_build_cost', 'estimated_test_cost', 'estimated_support_cost',
            'estimated_delivery_cost', 'assignments'
        )
