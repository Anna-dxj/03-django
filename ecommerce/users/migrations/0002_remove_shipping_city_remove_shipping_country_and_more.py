# Generated by Django 5.1 on 2024-09-05 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='city',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='country',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='post_code',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='state_district',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='street_address',
        ),
    ]
