# Generated by Django 4.2.6 on 2023-10-21 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_contact_delete_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['created_date']},
        ),
    ]
