from django.shortcuts import render
from .forms import dataform
from django.http import HttpResponseRedirect
from .models import dry,oily,acne
# Create your views here.

def home(request):
    return render(request,'skincare/web.html')

def skincareform(request):
    if request.method == "POST":
        form = dataform(request.POST)        
        if form.is_valid():           
            form.save()
            if form.cleaned_data['skintype'] == "dry":    
                medncs = dry.objects.all()
                return render(request,'skincare/web-table.html',{'medncs': medncs })
            elif form.cleaned_data['skintype'] == "oily":    
                medncs = oily.objects.all()
                return render(request,'skincare/web-table.html',{'medncs': medncs })
            else:    
                medncs = acne.objects.all()
                return render(request,'skincare/web-table.html',{'medncs': medncs })
    else:
        return render(request,'skincare/web-table.html')


# admin id , password == qirrat qirrat1