# Generated by Django 5.1 on 2024-10-20 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FundMe', '0010_campaign_currentfunding'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
