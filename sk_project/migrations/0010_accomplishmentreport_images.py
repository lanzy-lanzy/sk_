# Generated by Django 4.2.7 on 2025-01-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sk_project', '0009_alter_mainbudget_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomplishmentreport',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='accomplishment_reports/%Y/%m/%d/'),
        ),
    ]