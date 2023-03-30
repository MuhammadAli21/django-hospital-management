from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PatentDetail, DoctorDetail, StaffDetail, Appointment

# Create your views here.
@api_view(['GET','POST'])
def get_func_code(request):
    if request.method == 'GET':
        return Response({
            "statas": "200",
            "message" : "get api is working"
        })
    if request.method == 'POST':
        return Response({
            "statas": "200",
            "message" : "POST api is working"
        })
