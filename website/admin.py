from django.contrib import admin
from website.models import Contact


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'message', 'created_date')

    # ordering = ['created_date']
    # search_fields = ('name')
    class Meta:
        ordering = ['created_date']


admin.site.register(Contact, ContactAdmin)
