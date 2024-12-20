# Generated by Django 5.1.1 on 2024-11-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=15)),
                ('mobile_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=128)),
                ('admin_id', models.CharField(max_length=10)),
                ('admin_mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('finance_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField()),
            ],
        ),
    ]
