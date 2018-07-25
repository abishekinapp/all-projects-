# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    name='abishek'
    numbers = [1,3,4,6,3,2,4,5,55]

    args={'myname':name , 'number':numbers}
    return render(request,'accounts/home.html',args)
