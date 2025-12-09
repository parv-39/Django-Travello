from django.shortcuts import render, redirect
from .models import Destination
from .models import ContactMessage
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect
from .models import Booking
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect



# Create your views here.

def index(request):

    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The City That Never Sleeps'
    # dest1.price = 700
    # dest1.img = 'destination_10.jpg'
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = 'Hydrabad'
    # dest2.desc = 'Fisrt Biryani, Then Sherwani'
    # dest2.price = 625
    # dest2.img = 'destination_9.jpg'
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = 'Bengaluru'
    # dest3.desc = 'IT Hub'
    # dest3.price = 750
    # dest3.img = 'destination_8.jpg'
    # dest3.offer = True

    # dests = [dest1, dest2, dest3]

    dests = Destination.objects.all()

    return render(request, "index.html",{'dests': dests})

def contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message_text = request.POST.get("message")
        if name and email and message_text:
            ContactMessage.objects.create(name=name, email=email, message=message_text)
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contactus")
    
        else:
            messages.error(request,"All Fields are required.")

    return render(request, "contact.html")

def destination_detail(request, id):
    dest = Destination.objects.get(id=id)
    return render(request, 'destination_detail.html',{'dest':dest})

def book_destination(request, id):
    dest = get_object_or_404(Destination,id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        adults = request.POST.get("adults")
        children = request.POST.get("children")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        contact_number = request.POST.get("contact_number")

        if name and adults and start_date and end_date and contact_number:
            Booking.objects.create(
                destination=dest,
                name=name,
                adults=int(adults),
                children=int(children) if children else 0,
                start_date = start_date,
                end_date=end_date,
                contact_number=contact_number
            )
            messages.success(request, "Booking successful!, Our team will reach out to you shortly")
            return redirect('book_destination', id=dest.id)  # Redirect to the same destination page
        else:
            messages.error(request, "Please fill all required fields.")
            return redirect('book_destination', id=dest.id)  # Redirect back to the same form page

    return render(request, 'book_destination.html', {'dest': dest})


def news(request):
    return render(request, 'news.html')

def about(request):
    return render(request, 'about.html')