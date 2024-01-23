from django.shortcuts import redirect, render
from pages.models import *

def home_page_view(request):    
    return render(request, 'index.html')

def booking_post(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        date_come = request.POST.get('date_come')
        date_go = request.POST.get('date_go')
        guests = request.POST.get('guests')
        room = request.POST.get('room')

        
        new_booking = bookingModel(email=email, date_come=date_come, date_go=date_go, guests=guests, room=room)
        new_booking.save()

        return redirect('pages:home')
    else:
        return render(request, 'index.html')






def contact_page_view(request):
    return render(request, 'contact.html')


def restaurant_page_view(request):
    breakfast = BreakfastModel.objects.all().order_by('-pk')[:6]
    lunch = LunchModel.objects.all().order_by('-pk')[:6]
    dinner = DinnerModel.objects.all().order_by('-pk')[:6]
    
    context = {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
    }
    
    return render(request, 'restaurant.html', context)
    
    

def activities_page_view(request):
    return render(request, 'activities.html')



def contact_page_view(request):
    return render(request, 'contact.html')


def about_page_view(request):
    return render(request, 'about.html')