# Generated by Django 3.1 on 2020-08-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torieeblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='read_time',
            field=models.CharField(default='10-mins', max_length=10),
        ),
    ]
