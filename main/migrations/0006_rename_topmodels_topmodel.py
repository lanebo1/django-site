# Generated by Django 3.2.16 on 2023-03-02 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_topmodels'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TopModels',
            new_name='TopModel',
        ),
    ]