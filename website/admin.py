"""
imports the admin module from the Django framework
imports the Contact model from the website application
"""

from django.contrib import admin
from website.models import Contact

"""
defines a custom administration interface for the Contact model
specifies the fields that will be displayed in the list view of the Contact model in the admin panel
"""


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'message', 'created_date')

    class Meta:
        ordering = ['created_date']


admin.site.register(Contact, ContactAdmin)
