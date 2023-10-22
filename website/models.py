from django.db import models


class Contact(models.Model):
    # Contact model with relevant fields
    name = models.CharField(max_length=225)
    email = models.EmailField()
    subject = models.CharField(max_length=225)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        # Setting default ordering by created_date
        ordering = ['created_date']

    def __str__(self):
        # String representation of the Contact object
        return self.name
