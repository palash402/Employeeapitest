from django.contrib.auth.models import User, Group
from rest_framework import serializers
from employeetest.emp.models import Employee, Department


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'password']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class addemployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'First_Name', 'Last_Name', 'DOB', 'DOJ', 'Address',
                  'MOb_No', 'Designation', 'Dept_Id', 'user_id', 'role_id']
