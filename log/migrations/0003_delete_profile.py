# Generated by Django 2.2 on 2021-03-03 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]