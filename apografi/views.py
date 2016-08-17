
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf


def login(request):
    
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    
    username=request.POST['username']
    password=request.POST['password']
   
    user=auth.authenticate(username=username,password=password)
     
    if user is not None:     
        auth.login(request, user)
        return HttpResponseRedirect('/loggedIn/')
    else:
        return HttpResponseRedirect('/invalid/')
    
def loggedin(request):
    
    return render_to_response('valid.html')

def invalid(request):
    
    return render_to_response('invalid.html')

def logout_view(request):
    
    auth.logout(request)
    return render_to_response('login.html')