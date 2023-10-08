from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('home page')


def about_view(request):
    return HttpResponse('about page')


def contact_view(request):
    return HttpResponse('contact page')