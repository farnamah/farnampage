"""
Importing the path function from the django.urls module
# Explicitly importing the necessary view functions from the website.views module
"""
from django.urls import path
from website.views import *

app_name = 'website'

"""
URL patterns for the website app
"""
urlpatterns = [
    path('', index_view, name='index'),
    path('home', index_view),
    path('about', about_view),
    path('contact', contact_view, name='contact')
]
