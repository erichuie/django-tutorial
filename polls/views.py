from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
    return HttpResponse("Hello, world. You're at the polls test.")

def test_user(request):
    return HttpResponse("Hello, world. You're at the polls test_user.")