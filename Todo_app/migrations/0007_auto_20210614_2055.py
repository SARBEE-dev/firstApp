# Generated by Django 3.1.7 on 2021-06-14 19:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_app', '0006_auto_20210614_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
