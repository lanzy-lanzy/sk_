# Generated by Django 5.1.2 on 2024-10-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sk_project', '0005_user_address_user_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='price_per_unit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
