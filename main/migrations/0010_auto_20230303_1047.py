# Generated by Django 3.2.16 on 2023-03-03 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_blogpost_mainimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art', models.IntegerField()),
                ('brand', models.CharField(max_length=50)),
                ('img', models.ImageField(null=True, upload_to='static/images/clients')),
            ],
        ),
        migrations.DeleteModel(
            name='Brands',
        ),
    ]