# Generated by Django 3.0.5 on 2020-04-20 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='owner',
            new_name='contacts',
        ),
    ]
