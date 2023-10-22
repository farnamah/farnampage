from django.shortcuts import render
from website.forms import ContactForm
from django.contrib import messages
from django.shortcuts import redirect


# Redirecting to another page with various message types
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # Saving the form data to the database
            form.save()
        else:
            print(form.errors)
    # Creating a new instance of the ContactForm
    form = ContactForm()
    return render(request, 'website/index.html', {'form': form})
