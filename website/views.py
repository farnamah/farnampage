from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/index.html')


def contact_view(request):
    return render(request, 'website/index.html')


def test_view(request):
    if request.method == 'post':
        print('post')
    return render(request, 'website/test.html',{}