# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from accounts.forms import EditProfile


def home(request):
    name='abishek'
    numbers = [1,3,4,6,3,2,4,5,55]

    args={'myname':name , 'number':numbers}
    return render(request,'accounts/home.html',args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/accounts/profile/')
    else :
        form = RegistrationForm()
        arg ={'form' : form }
        return render(request,'accounts/reg_form.html',arg)

def profile(request):
    args = {'user':request.user}
    return render(request , 'accounts/profile.html',args)

def editprofile (request):
    if request.method == 'POST':
        form = EditProfile(request.POST,instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else :
        form = EditProfile(instance = request.user)
        args={'form': form}
        return render(request,'accounts/edit_profile.html',args)
