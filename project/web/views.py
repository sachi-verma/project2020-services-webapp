from django.shortcuts import render,redirect
from .models import User_message
from django.contrib import messages
from .models2 import Services
from django.db.models import Q
#from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'Homepage2.html')

def contact_us(request):
    return render(request,'ContactUs2.html')

def emergency(request):
    return render(request,'EmergencyHelp.html')

def serve(request):
    service1 = Services.objects.all()
    service2 = Services.objects.filter(Q(location='Borivali, Mumbai') | Q(location='Kandivali, Mumbai'))
    service3 = Services.objects.filter(location='Thane, Mumbai')
    service4 = Services.objects.filter(Q(location='Malad, Mumbai') | Q(location='Goregaon, Mumbai') | Q(location='Andheri, Mumbai'))
    service5 = Services.objects.filter(Q(location='Malad, Mumbai') | Q(location='Goregaon, Mumbai') | Q(location='Jogeshwari, Mumbai'))
    service6 = Services.objects.filter(Q(location='Thane, Mumbai') | Q(location='Bhandup, Mumbai'))
    #service3 = Services.objects.filter(category='electrical')
    res_dict = {'service1': service1 , 'service2': service2, 'service3': service3,
     'service4': service4, 'service5': service5,'service6': service6}

    #return render(request,'service.html',context=res_dict)
    return render(request,'form.html', context=res_dict)    

def data1(request):
    if request.method=='POST':
        fname = request.POST['fullname']
        email = request.POST['email_id']
        subject = request.POST['subject']

        user = User_message(Name=fname, Email=email, Message=subject)
        user.save()
        #messages.info(request,"Message delivered sucessfully")
        return redirect('contact_us')

def register(request):
       if request.method=='POST':
           namee = request.POST['fname']
           cat = request.POST['cat']
           num = request.POST['num']
           loc = request.POST['loc']

           r = Services(name=namee, category=cat, phone_number=num, location=loc )
           r.save()
           return redirect('serve')


