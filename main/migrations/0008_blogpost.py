# Generated by Django 3.2.16 on 2023-03-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_newmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art', models.IntegerField()),
                ('name', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=50, null=True)),
                ('date', models.CharField(max_length=50, null=True)),
                ('maindesc', models.CharField(max_length=400, null=True)),
                ('desc1', models.CharField(max_length=800, null=True)),
                ('img1', models.ImageField(upload_to='static/images/blog')),
                ('desc2', models.CharField(max_length=800, null=True)),
                ('img2', models.ImageField(upload_to='static/images/blog')),
                ('desc3', models.CharField(max_length=800, null=True)),
                ('img3', models.ImageField(upload_to='static/images/blog')),
                ('finaldesc', models.CharField(max_length=800, null=True)),
            ],
        ),
    ]
