from django.shortcuts import render
from django.http import HttpResponse

#Define home function
def home(request):
    return HttpResponse('Hello World')