
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django import forms

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from employeetest.emp.serializers import UserSerializer, GroupSerializer, addemployeeSerializer
from employeetest.emp.models import *

# Create your views here.


class UserViewSet(viewsets.ModelViewSet, APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # fn= self.request.query_param.get('fname')

        emp_detail = Employee.objects.all()
        # return HttpResponse('check it again.')
        return emp_detail

    # def get(self,request,*args, **kwargs):

    #     return Response(serializers.UserSerializer)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class userdetails(APIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        emp_detail = Employee.objects.all()
        return emp_detail

    # temp til end1

    def get(self, request, format=None):
        employee = Employee.objects.all()
        serializer = UserSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # end1


class addauthuser(APIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        employee = Employee.objects.all()
        serializer = UserSerializer(employee, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     # ,createuserSerializer(data=request.data)
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, format=None):
    #     if request.method == 'POST':
    #         username=request.POST['username']
    #         password=request.POST['password']
    #         emailaddress=request.POST['email']
    #         First_Name = request.POST['First_Name']
    #         Last_Name = request.POST['Last_Name']
    #         DOB = request.POST['DOB']
    #         DOJ = request.POST['DOJ']
    #         Address = request.POST['Address']
    #         MOb_No = request.POST['MOb_No']
    #         Designation = request['Designation']

    #         User.objects.create(username=username,password=password,email=emailaddress)
    #         # User.objects.
    #         Employee.objects.create(First_Name=First_Name,Last_Name=Last_Name,DOB=DOB,DOJ=DOJ,Address=Address,MOb_No=MOb_No,Designation=Designation,email=emailaddress)
    #         # a=User(username=username,password=password,email=emailaddress, First_Name=First_Name,)
    #         # a.save()
    #     return HttpResponse("auth user details added.")

    def post(self, request, format=None):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            emailaddress = request.POST['email']
            First_Name = request.POST['First_Name']
            Last_Name = request.POST['Last_Name']
            DOB = request.POST['DOB']
            DOJ = request.POST['DOJ']
            Address = request.POST['Address']
            MOb_No = request.POST['MOb_No']
            Designation = request.POST['Designation']

            # User.objects.create(username=username,password=password,email=emailaddress)
            # # User.objects.
            # Employee.objects.create(First_Name=First_Name,Last_Name=Last_Name,DOB=DOB,DOJ=DOJ,Address=Address,MOb_No=MOb_No,Designation=Designation,email=emailaddress)

            a = User(username=username, password=password, email=emailaddress)
            a.save()

            Emp_Id = User.objects.get(username=username)
            # print(Emp_Id)

            b = Employee(user_id=Emp_Id, First_Name=First_Name, Last_Name=Last_Name,
                         DOB=DOB, DOJ=DOJ, Address=Address, MOb_No=MOb_No, Designation=Designation)
            b.save()
            print(b.First_Name)
        return HttpResponse("auth user details added.")


class addemployee(APIView):

    def get(self, request, format=None):
        employee = Employee.objects.all()
        serializer = addemployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            emailaddress = request.POST['email']
            First_Name = request.POST['First_Name']
            Last_Name = request.POST['Last_Name']
            DOB = request.POST['DOB']
            DOJ = request.POST['DOJ']
            Address = request.POST['Address']
            MOb_No = request.POST['MOb_No']
            Designation = request['Designation']
            a = User(username=username, password=password, email=emailaddress)
            a.save()
