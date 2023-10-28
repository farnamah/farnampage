from django.shortcuts import render


# Create your views here.
def login_views(request):
    return render(request, 'accounts/login.html')


def logout_views(request):
    return render(request, 'accounts/logout.html')


def signup_views(request):
    return render(request, 'accounts/signup.html')
