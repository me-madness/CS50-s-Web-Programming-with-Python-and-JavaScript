from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")


def rangel(request):
    return HttpResponse("Hello, Rangel!")