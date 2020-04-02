from django.shortcuts import render,redirect
from django.views import generic
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User, auth
# from django.contrib.auth( login, logout)
from .models import Member
from .forms import Record

def login(request):
    return render( request, 'login.html')
    



def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username ,password=password )

        if user is not None:
            auth.login(request, user)
            return render(request,'home.html')
       
        else:
            messages.info(request,'Invalid credentials.')
            return render(request,'login.html')
    
    # elif auth.authenticate:
    #     return render(request, 'home.html')    
    elif User.is_authenticated:
        return render(request, 'home.html')

    else:
        return render(request,'login.html')


  
def about(request):
    return render( request, 'about.html')



def addrecord(request):
    if request.method == 'POST':
        form = Record(request.POST)
        if form.is_valid():
            global message
            data = form.cleaned_data
            m = Member(
                ID_number = data.get('ID_number'),
                date =data.get('date'),
                first_name =data.get('first_name'),
                last_name =data.get('last_name'),
                member_type =data.get('member_type'),
                payment_type =data.get('payment_type'),
                Membership_Start_date =data.get('Membership_Start_date'),
                Membership_End_date =data.get('Membership_End_date'),
                rate =data.get('rate'),
                paid =data.get('paid'),
                due =data.get('rate') - data.get('paid'),
                Contact_number =data.get('Contact_number'),
                Email =data.get('Email'),
                Remarks =data.get('Remarks')
            )
            m.save()
            message = "data entered"
            form = Record()
            return render(request, 'addrecord.html', {'message': message, 'form': form})
        else:
            return render(request, 'addrecord.html', {'form': form})


    else:
        form = Record()

    return render(request, 'addrecord.html', {'form': form})


def viewrecord(request):
    allrecord = Member.objects.all()
    return render(request, 'viewrecord.html', { 'mrecord': allrecord})    

def findrecord(request):
    if request.method == 'POST':
        m_id = request.POST['id_number']
        print(m_id)
    mrecord = Member.objects.filter(ID_number=m_id)
    if len(mrecord) > 0:
        return render(request, 'viewrecord.html', { 'mrecord': mrecord})
    else:
        messages.info(request,'No Member log.') 
        allrecord = Member.objects.all()
        return render(request, 'viewrecord.html', { 'mrecord': allrecord})    


