from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from weatherapp.models import userDetails


# Create your views here.


def home(request):
    return render(request, "homepage.html")


@csrf_exempt
def savemail(request):
    first_name = request.POST.get("fname")
    last_name = request.POST.get("lname")
    mail = request.POST.get("email")
    user = userDetails(firstName=first_name, lastName=last_name, email=mail)
    user.save()
    return render(request, "thank.html")


# This is function for senting mail out - Commenting it out for a CronJOb - siva
""" @csrf_exempt
def sendmail(request):
    touser = request.POST.get("t")
    sub = request.POST.get("s")
    bod = request.POST.get("b")
    efrom = settings.EMAIL_HOST_USER
    reclist = [
        touser,
    ]
    send_mail(sub, bod, efrom, reclist)
    msg = "Mail Delivered"
    return HttpResponse(msg)
 """