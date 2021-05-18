# Generated by Django 2.2 on 2021-05-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0020_record_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField(default=0)),
                ('user', models.EmailField(max_length=254)),
                ('doctor', models.EmailField(max_length=254)),
                ('feedback', models.CharField(max_length=100, null=True)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
       
    ]