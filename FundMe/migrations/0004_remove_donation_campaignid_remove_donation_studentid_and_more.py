# Generated by Django 5.1 on 2024-10-08 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FundMe', '0003_campaign_donation_payment_staff_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='campaignid',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='studentid',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='donationid',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='Campaign',
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
