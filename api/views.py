from rest_framework.decorators import api_view
from api import models,serializers
from rest_framework.response import Response
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	RetrieveUpdateAPIView,
	ListCreateAPIView,
	DestroyAPIView
	)
# Create your views here.

class StudentListView(ListCreateAPIView):
	queryset=models.Student.objects.all()
	serializer_class=serializers.StudentSerializer


class StudentDetailsView(RetrieveUpdateAPIView):
	queryset=models.Student.objects.all()
	serializer_class=serializers.StudentSerializer

class StudentDeleteView(DestroyAPIView):
	queryset=models.Student.objects.all()
	serializer_class=serializers.StudentSerializer



# Patch,get requests for RetrieveUpdateAPIView, patch to update and get to read the data.
# get,post requests for ListCreateAPIView get to read all the data and post to add a new record into the table.
# ListCreateAPIView is for performing the creating a new entry and read the whole table.
# RetrieveUpdateAPIView is for performing Retrieve and Update operations.
# DestroyAPIView is for performing the delete operation.
# To delete a record head up to deletestudent/pk url and select the delete option out of the given options and send
# for deletestudent/pk check out the urls.py file of api application.