from django.shortcuts import render, HttpResponse
from carsapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')


# HttpResponse("working")
def supercars(request):
    return render(request, 'supercars.html')
    # return HttpResponse("working")


def suvcars(request):
    return render(request, 'suvcars.html')
    # return HttpResponse("working")


def sedancars(request):
    return render(request, 'sedancars.html')
    # return HttpResponse("working")


def hatchbackcars(request):
    return render(request, 'hatchbackcars.html')
    # return HttpResponse("working")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your response has been recorded')

    return render(request, 'contact.html')
    # return HttpResponse("working")
