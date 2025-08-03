from django.shortcuts import render
from django.http import HttpResponse
#This is for function based view from django.contrib.auth.decorators import login_required
#Now we are using classs based view ie below updates
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.views.generic import TemplateView


class HomeView(TemplateView):
     template_name = 'home/welcome.html'
     extra_context = {'today': datetime.today()}
     
     
#Below is Example of function based views 
def basicHome(request):
    return render(request,'home/welcome.html',{}) #this is for the return html file ..

# This is for function based view But now we are changing the view to class based @login_required(login_url = '/admin')

class authorized(LoginRequiredMixin, TemplateView):

    template_name = 'home/authorized.html'
    login_url = '/admin'


#def authorized(request):
    # return render(request, 'home/authorized.html',{})