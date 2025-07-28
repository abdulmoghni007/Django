from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.
def home(request):
#     return HttpResponse('Hello World Of Abdul Moghni') #this is for the base response
      return render(request,'home/welcome.html',{'today': datetime.today()}) #this is for the return html file .. 

def basicHome(request):
    return render(request,'home/welcome.html',{}) #this is for the return html file ..

@login_required(login_url = '/admin')
def authorized(request):
     return render(request, 'home/authorized.html',{})