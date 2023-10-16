from django.urls import path
from website.views import *
app_name = 'website'

urlpatterns = [
    path('home',index_view),
    path('about',about_view),
    path('contact',contact_view),
    path('test',test_view,name='test')
]