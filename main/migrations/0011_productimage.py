# Generated by Django 3.2.16 on 2023-03-03 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20230303_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='static/images/collection')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
    ]