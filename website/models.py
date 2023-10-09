from django.db import models
#class Post(models.Model):
    #title = models.CharField(max_length=255)
    #content = models.TextField()
    #image
    #category
    #counted_views = models.IntegerField(default=0)
    #status = models.BooleanField(default=False)
    #published_date = models.DateTimeField(null=True)
    #created_date = models.DateTimeField(auto_now_add=True)
    #updated_date = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    subject = models.CharField(max_length=225)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
