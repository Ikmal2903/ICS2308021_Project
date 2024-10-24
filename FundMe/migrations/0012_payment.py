# Generated by Django 5.1 on 2024-10-20 06:41

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FundMe', '0011_delete_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentid', models.CharField(editable=False, max_length=10, unique=True)),
                ('paymentdate', models.DateField(default=django.utils.timezone.now)),
                ('paymentstatus', models.CharField(max_length=20)),
                ('donationid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FundMe.donation')),
            ],
        ),
    ]
