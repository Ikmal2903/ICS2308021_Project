from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

# Create your models here.
class Student(models.Model):
    studentid = models.CharField(max_length=12, primary_key=True)
    studentname = models.CharField(max_length=200)
    studentemail = models.EmailField(max_length=200)
    studentpassword = models.CharField(max_length=50, validators=[MinLengthValidator(8)]) 
    studentphone = models.CharField(max_length=15)
    studentaddress = models.TextField(max_length=255)

class Staff(models.Model):
    staffid = models.CharField(max_length=12, primary_key=True)
    staffname = models.CharField(max_length=200)
    staffemail = models.EmailField(max_length=200)
    staffpassword = models.CharField(max_length=50, validators=[MinLengthValidator(8)])  
    staffphone = models.CharField(max_length=15)
    staffaddress = models.TextField(max_length=255)


class Campaign(models.Model):
    campaignid = models.CharField(max_length=10, primary_key=True)
    campaignname = models.CharField(max_length=255)
    description = models.TextField()
    goalAmount = models.DecimalField(max_digits=10, decimal_places=2)    
    currentFunding = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Track current funding
    start_date = models.DateField()
    end_date = models.DateField()
    # New field for the image
    campaign_image = models.ImageField(upload_to='campaign_images/', blank=True, null=True)

    def __str__(self):
        return self.campaignname
  

class Donation(models.Model):
    donationid = models.CharField(max_length=10, unique=True, editable=False)
    donationdate = models.DateField(default=timezone.now)
    amount = models.FloatField() 
    paymentmethod = models.CharField(max_length=255)
    studentid = models.ForeignKey('Student', on_delete=models.CASCADE)
    campaignid = models.ForeignKey('Campaign', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.donationid:
            count = Donation.objects.count() + 1  # Count current donations
            self.donationid = f'D{str(count).zfill(3)}'  # Generate custom ID like 'D001', 'D002'
        super(Donation, self).save(*args, **kwargs)

    def __str__(self):
        return self.donationid
class Payment(models.Model):
    paymentid = models.CharField(max_length=10, unique=True, editable=False)
    paymentdate = models.DateField(default=timezone.now)
    paymentstatus = models.CharField(max_length=20)
    donationid = models.ForeignKey('Donation', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.paymentid:
            count = Payment.objects.count() + 1  # Count current payments
            self.paymentid = f'P{str(count).zfill(3)}'  # Generate custom ID like 'P001', 'P002'
        super(Payment, self).save(*args, **kwargs)

    def __str__(self):
        return self.paymentid



