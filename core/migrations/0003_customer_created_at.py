# Generated by Django 4.1 on 2022-09-04 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_customer_age_customer_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]