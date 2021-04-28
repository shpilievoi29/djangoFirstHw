from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Home")


def about(request):
    return HttpResponse("About")


def foo(request, foo='foo'):
    return HttpResponse(f"resource and slug is {foo}")
