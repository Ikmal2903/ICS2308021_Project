from django.shortcuts import render, get_object_or_404, redirect
from FundMe.models import Student,Staff,Campaign,Payment,Donation
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
import os
from django.contrib.auth.decorators import login_required
from decimal import Decimal

def index(request):
    context={
        'greeting':0,
    }
    return render(request,'index.html',context)

def signup(request):
    mydetails= Student.objects.all().values()
    context={
        'mydetails':mydetails,
    }
    if request.method=='POST':
        c_role=request.POST['role']
        c_role=c_role.upper()
        if c_role == 'STUDENT':
            c_id= request.POST['id']
            c_name= request.POST['name']
            c_email=request.POST['email']
            c_pass=request.POST['password']
            c_phone=request.POST['phone']
            c_address=request.POST['address']
            data=Student(studentid=c_id, 
                        studentname=c_name, 
                        studentemail=c_email, 
                        studentpassword=c_pass,
                        studentphone=c_phone,
                        studentaddress=c_address,
                        )
            data.save()
            return render(request, "login.html")

        if c_role =='STAFF':            
            s_id= request.POST['id']
            s_name= request.POST['name']
            s_email=request.POST['email']
            s_pass=request.POST['password']
            s_phone=request.POST['phone']
            s_address=request.POST['address']
            data=Staff(staffid=s_id, 
                        staffname=s_name, 
                        staffemail=s_email, 
                        staffpassword=s_pass,
                        staffphone=s_phone,
                        staffaddress=s_address,
                        )
            data.save()
            return render(request, "login.html")
        else:
            messages.error(request, 'Invalid role.')
            return render(request, 'signup.html')


    return render(request,'signup.html',context)
def login(request):
    if request.method == 'POST':
        c_role = request.POST['role'].upper()
        c_email = request.POST.get('email')
        c_password = request.POST.get('password')

        if c_role == 'STUDENT':
            try:
                student = Student.objects.get(studentemail=c_email)
                if student.studentpassword == c_password:
                    # Store user information in session
                    request.session['user_id'] = student.studentid
                    request.session['user_name'] = student.studentname
                    request.session['user_role'] = 'STUDENT'
                    return redirect("student_page")
                else:
                    messages.error(request, 'Invalid password. Please try again.')
            except Student.DoesNotExist:
                messages.error(request, 'No account found with this email.')
        
        elif c_role == 'STAFF':
            try:
                staff = Staff.objects.get(staffemail=c_email)
                if staff.staffpassword == c_password:
                    # Store user information in session
                    request.session['user_id'] = staff.staffid
                    request.session['user_name'] = staff.staffname
                    request.session['user_role'] = 'STAFF'
                    return redirect("staff_page")
                else:
                    messages.error(request, 'Invalid password. Please try again.')
            except Staff.DoesNotExist:
                messages.error(request, 'No account found with this email.')
        else:
            messages.error(request, 'Invalid role. Please select either STUDENT or STAFF.')
        
        # If login fails, re-render the login page with errors
        return render(request, 'login.html')

    return render(request, 'login.html')
def logout(request):
    return redirect(reverse,'index')


def student_page(request):
    user_name = request.session.get('user_name')
    user_role = request.session.get('user_role')
    if request.method == 'GET':
        c_name = request.GET.get('c_name')

        if c_name:
            # Filter campaigns by name (case-insensitive)
            data = Campaign.objects.filter(campaignname__icontains=c_name)
        else:
            # Fetch all campaigns if no search term is entered
            data = Campaign.objects.all()
        context = {
            'data': data,
            'user_name': user_name,
            'user_role': user_role,

        }
        return render(request, "student_page.html", context)
    return render(request, "student_page.html", {'user_name': user_name, 'user_role': user_role})

def staff_page(request):
    return render(request, "staff_page.html")
def manage_campaign(request):
    mycampaign=Campaign.objects.all().values()
    context={
        'mycampaign':mycampaign,
    }
    if request.method == 'POST':
        campaignid = request.POST.get('campaign_id')
        campaignname = request.POST.get('campaign_name')
        description = request.POST.get('description')
        goalAmount = request.POST.get('goalAmount')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        # Handling the image file
        image = request.FILES.get('campaign_image')

        new_campaign = Campaign(
            campaignid=campaignid,
            campaignname=campaignname,
            description=description,
            goalAmount=goalAmount,
            start_date=start_date,
            end_date=end_date,
            campaign_image=image
        )
        new_campaign.save()
        return redirect('manage_campaign')  # Redirect after saving the campaign
    
    campaigns = Campaign.objects.all()
    return render(request, 'manage_campaign.html', {'mycampaign': campaigns})

def view_list_student(request):
    user_name = request.session.get('user_name')
    user_role = request.session.get('user_role')
    if request.method == 'GET':
        s_id = request.GET.get('c_id')

        if s_id:
            # Filter campaigns by name (case-insensitive)
            mystudent= Student.objects.filter(studentid=s_id)
        else:
            # Fetch all campaigns if no search term is entered
            mystudent = Student.objects.all()
        context = {
            'mystudent':mystudent,
            'user_name': user_name,
            'user_role': user_role,

        }
        return render(request, "view_list_student.html", context)
    return render(request, "view_list_student.html", {'user_name': user_name, 'user_role': user_role})

def update_campaign(request,campaignid):
    data=Campaign.objects.get(campaignid=campaignid)
    dict={
        'data':data
    }
    return render(request ,"update_campaign.html", dict)
def save_update_campaign(request, campaignid):
    # Fetch the campaign data
    data = Campaign.objects.get(campaignid=campaignid)

    # Get updated fields from the form
    c_name = request.POST['campaignname']
    c_desc = request.POST['description']
    c_goal = request.POST['goalAmount']
    s_date = request.POST['start_date']
    e_date = request.POST['end_date']
    
    # Update campaign details
    data.campaignname = c_name
    data.description = c_desc
    data.goalAmount = c_goal
    data.start_date = s_date
    data.end_date = e_date

    # Check if a new image is uploaded
    if 'campaign_image' in request.FILES:
        data.campaign_image = request.FILES['campaign_image']

    # Save the updated data
    data.save()

    return redirect(reverse("manage_campaign"))
def delete_campaign(request,campaignid):
    data=Campaign.objects.get(campaignid=campaignid)
    data.delete()
    return HttpResponseRedirect(reverse("manage_campaign"))
def view_campaign(request,campaignid):
    mycampaign = Campaign.objects.get(campaignid=campaignid)
    context={
        'mycampaign':mycampaign
    }

    return render(request, 'view_campaign.html',context)
def donation(request,campaignid):
    mycampaign = Campaign.objects.get(campaignid=campaignid)
    context={
        'mycampaign':mycampaign
    }   
    return render(request, 'donation.html',context)

def save_donation(request, campaignid):
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the user ID from the session
        user_id = request.session.get('user_id')

        if not user_id:
            messages.error(request, 'You must be logged in to make a donation.')
            return redirect('login')

        # Fetch the campaign data using the campaign ID
        campaign = get_object_or_404(Campaign, campaignid=campaignid)

        # Fetch the student object using the user_id
        student = get_object_or_404(Student, studentid=user_id)

        # Get updated fields from the form
        d_amount = request.POST.get('amount')
        p_method = request.POST.get('payment_method')
        d_date = timezone.now()  # Set the donation date to the current time

        try:
            # Create a new Donation object
            donation = Donation(
                campaignid=campaign,
                amount=Decimal(d_amount),
                paymentmethod=p_method,
                donationdate=d_date,
                studentid=student
            )

            # Save the new donation to the database
            donation.save()

            # Update the campaign's current funding with the new donation amount
            campaign.currentFunding += Decimal(d_amount)
            campaign.save()

            # Use the donation's ID for the payment record
            donation_id_str=get_object_or_404(Donation, donationid=donation.donationid)


            # Create a new Payment object linked to the donation ID
            payment = Payment(
                donationid=donation_id_str,  # Pass the Donation ID as a string
                paymentstatus='Completed',  # Set the payment status
                paymentdate=timezone.now()
            )

            # Save the new payment record
            payment.save()


            # Pass the donation and payment details to the receipt template
            return render(request, 'receipt.html', {
                'donation': donation,
                'campaign': campaign,
                'payment': payment
            })

        except Exception as e:
            messages.error(request, f"An error occurred while processing the donation: {str(e)}")
            return redirect('view_campaign', campaignid=campaignid)

    return redirect('view_campaign', campaignid=campaignid)
def receipt(request):
    return render(request,'receipt.html')
def view_history(request):
    user_name = request.session.get('user_name')
    user_role = request.session.get('user_role')
    if request.method == 'GET':
        d_date = request.GET.get('d_date')

        if d_date:
            # Filter campaigns by name (case-insensitive)
            donation= Donation.objects.filter(donationdate=d_date)
        else:
            # Fetch all campaigns if no search term is entered
            donation = Donation.objects.all()
        context = {
            'donation':donation,
            'user_name': user_name,
            'user_role': user_role,

        }
        return render(request, 'view_history.html', context)
    return render(request, 'view_history.html', {'user_name': user_name, 'user_role': user_role})

def aboutus(request):
    return render(request,'aboutus.html')

def update_student(request,studentid):
    data=Student.objects.get(studentid=studentid)
    dict={
        'data':data
    }
    return render(request ,"update_student.html", dict)
def save_update_student(request, studentid):
    # Fetch the campaign data
    data = Student.objects.get(studentid=studentid)

    # Get updated fields from the form
    s_name = request.POST['studentname']
    s_email = request.POST['studentemail']
    s_password = request.POST['studentpassword']
    s_phone = request.POST['studentphone']
    s_address = request.POST['studentaddress']
    
    # Update campaign details
    data.studentname = s_name
    data.studentemail = s_email
    data.studentpassword = s_password
    data.studentphone = s_phone
    data.studentaddress = s_address
    # Save the updated data
    data.save()

    return redirect(reverse("view_list_student"))
def delete_student(request,studentid):
    data=Student.objects.get(studentid=studentid)
    data.delete()
    return HttpResponseRedirect(reverse("view_list_student"))



