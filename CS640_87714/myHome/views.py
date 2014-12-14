from django.shortcuts import render
from django.template import RequestContext
#from myHome.models import Page
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render_to_response("home.html")
