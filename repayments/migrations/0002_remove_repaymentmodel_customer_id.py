# Generated by Django 5.1.1 on 2024-12-28 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repayments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repaymentmodel',
            name='customer_id',
        ),
    ]
