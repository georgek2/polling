from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth.models import User

import openai 
from openai import OpenAI

from . import models

# Create your views here.

def home(request):
    surveys = models.Survey.objects.all()
    context = {
        'surveys': surveys,
    }

    return render(request, 'polls/homepage.html', context)

@login_required
def survey(request, pk):

    survey = models.Survey.objects.get(id=pk)
    # qns = models.Question.
    context = {
        'survey': survey
    }
    return render(request, 'polls/survey.html', context)

def login_page(request):
    surveys = models.Survey.objects.all()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials!!')
            return redirect('login')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
        'surveys': surveys
    }
    
    return render(request, 'polls/login.html', context=context)

def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User with that username already exists!!')
            return redirect('register')
        
        if len(password1) < 8:
            messages.error(request, 'Password must be longer than 8 characters!!')
            return redirect('register')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match!!')
            return redirect('register')
        
        else:
            if form.is_valid():
                form.save()
                # login(request, form.save())
                messages.success(request, 'User created successfully..')
                return redirect('login')
        
    else:
        form = UserCreationForm()
    
    return render(request, 'polls/register.html', {'form':form})


def logout_page(request):
    
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    
    return render(request, 'polls/logout.html')
    

def password_reset(request):
    
    return render(request, 'polls/password_reset.html')


def password_reset_sent(request):
    
    return render(request, 'polls/password_reset_sent.html')


def ai_survey(request):
    
    client = OpenAI.chat.completions.create()
    
    return render(request, 'polls/ai_survey.html')



