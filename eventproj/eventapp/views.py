
from .models import Portfolio
from .forms import ServiceForm
# from eventapp.forms import ReviewForm
# from django.views.generic.edit import FormView
# from django.shortcuts import render, redirect
from django.http import HttpResponse

# from .tasks import send_booking_confirmation_email
from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    return render(request,'index.html')
def portfolio(request):
    dict_eve={
        'eve':Portfolio.objects.all()
    }
    return render(request,'portfolio.html',dict_eve)

def services(request):
    if request.method=='POST':
        form=ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form=ServiceForm()
    dict_form={
        'form':form
    }

    return render(request,'services.html',dict_form)

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def wedding(request):
    return render(request,'wedding.html')

def floral(request):

    return render(request,'floral.html')

def homedec(request):

    return render(request,'homedec.html',)

def party(request):
    return render(request,'party.html')


def styling(request):
    return render(request,'styling.html')

def favors(request):
    return render(request,'favors.html')


def confirm(request):
    return render(request,'alert.html')

def review(request):
    return render(request,'review.html')




