# Generated by Django 5.1 on 2024-10-19 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FundMe', '0008_campaign_campaign_image_alter_campaign_campaignid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='campaignid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]