from django.shortcuts import render
from .forms import *
from .models import UserRegisterDetails
from django.http import HttpResponseRedirect
import pyrebase
import hashlib
from django.contrib import messages

# Create your views here.

config = {
    "apiKey": "AIzaSyDGJ_RQxd1Z1JbY0c7YWGGUXHw3XyBHZiA",
    "authDomain": "healthcare-8986c.firebaseapp.com",
    "databaseURL": "https://healthcare-8986c.firebaseio.com",
    "projectId": "healthcare-8986c",
    "storageBucket": "healthcare-8986c.appspot.com",
    "messagingSenderId": "54361003190"
  }
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db =firebase.database()


def validateEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def login(request):
    print('login page')
    loginform = userLoginForm()
    return render(request, 'login.html', {'log_form':loginform})
def logging_in(request):
    from django.contrib import messages
    print('logging user in')
    loginform = userLoginForm(request.POST)
    if loginform.is_valid():
        username = loginform.cleaned_data['user_name']
        password = loginform.cleaned_data['password']
        if((username != None)and(password != None)):
            if(not validateEmail(username)):
                messages.add_message(request,messages.SUCCESS,"invalid email id")
                return HttpResponseRedirect('/login')

            else:

                user = auth.sign_in_with_email_and_password(username, password)
                if(user != None):
                    request.session['id'] = user
                    messages.add_message(request,messages.SUCCESS,"succesfully logged in ")
                    return HttpResponseRedirect('/user_detail_form')
                else:
                    messages.add_message(request,messages.SUCCESS,"unable to log in ")
                return HttpResponseRedirect('/login')
        else:
            messages.add_message(request,messages.SUCCESS,"Emp")
            return HttpResponseRedirect('/login')

def register(request):
    userdetail = UserRegisterDetails.objects.all()
    form = userRegisterForm()
    print('in register')
    return render (request, 'register.html', {'userdetail':userdetail,'form': form})


def register_users(request):
    from django.contrib import messages
    print('register user')
    form = userRegisterForm(request.POST)
    if form.is_valid():
        details = UserRegisterDetails(user_name = form.cleaned_data['user_name'],
                                       password = form.cleaned_data['password'])

        details.save()
        username = form.cleaned_data['user_name']
        password = form.cleaned_data['password']
        re_password = form.cleaned_data['re_password']


        if((username != None) and (password != None) and (re_password != None) ):
            if((password == re_password) and (validateEmail(username))):
                #messages.add_message(request,messages.SUCCESS,"")
                #user = auth.create_user_with_email_and_password(username,password)
                #db.child(user).child("age").set(str(age))
                return HttpResponseRedirect('/login')
            else:
                messages.add_message(request,messages.SUCCESS,"Passwords do not match or Invalid email")
                return HttpResponseRedirect('/register')
    #return HttpResponseRedirect('/login')
def user_detail_form(request):

    #request.session["id"] = None
    form = userDetailForm()
    if(request.session['id']!= None):

        return render(request,'userdetail_form.html',{'form':form})
    else:
        messages.add_message(request,messages.ERROR,"please login first")
        return HttpResponseRedirect('/login')


def post_details(request):
        if(request.session['id']==None):
            messages.add_message(request,messages.ERROR,"please login first")
            return HttpResponseRedirect('/login')
        form = userDetailForm(request.POST)
        if form.is_valid():
            user = request.session['id']
            first_name=form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            dob = form.cleaned_data['dob']
            address = form.cleaned_data['address']
            blood_group = form.cleaned_data['blood_group']

            results = db.child("users").push(first_name, user['idToken'])
            print(results)
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/user_detail_form')
