from django.shortcuts import render
from django.http import HttpResponse
from .models import Servicecard
import pyrebase
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


def index(request):
    scard = Servicecard.objects.all()
    return render(request,'index.html', { 'scards': scard })

def bookbed(request):
    return render(request,'bookbed.html')

def doctor(request):
    users = db.child("doctors").get()
    print("valuee....")
    for user in users.each():
        print(user.val())
    print(users.val())
    return render(request , 'doctor.html',{'user':users.val()})
