# Generated by Django 5.1 on 2024-10-14 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FundMe', '0005_campaign_staff_donation_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='donationid',
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
