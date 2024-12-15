# Generated by Django 5.1.1 on 2024-11-23 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_mobile_number', models.CharField(max_length=15)),
                ('alternate_mobile_number', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField()),
                ('aadhar_number', models.CharField(max_length=12, unique=True)),
                ('pan_number', models.CharField(max_length=10, unique=True)),
                ('address', models.TextField()),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usersmodel')),
            ],
        ),
    ]
