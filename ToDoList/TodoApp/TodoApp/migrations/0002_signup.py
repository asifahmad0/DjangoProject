# Generated by Django 5.1.5 on 2025-01-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uname', models.CharField(max_length=25)),
                ('Email', models.CharField(max_length=100)),
                ('Pass', models.CharField(max_length=100)),
            ],
        ),
    ]
