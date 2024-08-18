from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import User
from django.contrib.messages import warning, success
# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')
    

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST.get('email')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        phone = request.POST.get('phone')
        
        if password != password_confirm:
            warning(request, 'Password confirmation is incorrect')
            return redirect(reverse('main:register')+'#form')
        return render(request, 'register.html')
        

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        if not User.objects.filter(username=username).exists():
            warning(request, 'User does not exist')
            return redirect(reverse('main:kirish'))
        
        user = User.objects.get(username=username)
        
        if not user.check_password(password):
            warning(request, 'Password is incorrect')
            return redirect(reverse('main:kirish'))
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('main:home'))
        
        warning(request, 'Error')
        return redirect(reverse('main:kirish'))
