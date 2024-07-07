from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages



# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Taken")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already In Use")
                return redirect('signup')
            else:
                user_reg = User.objects.create_user(username,email,password1)
                user_reg.save()
                messages.info(request, "Your account has been created Successfully!")
                return redirect('/')
        else:
            messages.info(request, "Your Password doesn't Match")
            return redirect('signup')
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.info(request, "Invalid Details")
            return redirect('signup')
    return render(request,'signin.html')









def logout(request):
    auth.logout(request)
    return redirect('/')



