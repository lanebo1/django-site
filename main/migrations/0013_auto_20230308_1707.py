# Generated by Django 3.2.16 on 2023-03-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='title1',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='title2',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='title3',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='desc1',
            field=models.CharField(max_length=8000, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='desc2',
            field=models.CharField(max_length=8000, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='desc3',
            field=models.CharField(max_length=8000, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='finaldesc',
            field=models.CharField(max_length=8000, null=True),
        ),
    ]
