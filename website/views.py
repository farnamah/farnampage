from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from website.models import Contact
from django.shortcuts import render
from website.forms import NameForm ,ContactForm
from django.contrib import messages
from django.shortcuts import redirect


def my_view(request):
    messages.debug(request, 'This is debug')
    messages.info(request, 'This is info')
    messages.success(request, 'This is success')
    messages.warning(request, 'This is warning')
    messages.error(request, 'This is error')
    return redirect("/mysite")


def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/index.html')


def contact_view(request):
    if request.method == 'post':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'website/index.html', {'form': form})



def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    form = ContactForm()
    return render(request, 'website/test.html', {'form': form})
