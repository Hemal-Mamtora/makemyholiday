from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from holiday.forms import RegistrationForm
from holiday.models import Holidays, Flight, Hotel
# Create your views here.
'''
class SignupView():
    pass
'''
'''
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'holiday/signup.html'
'''
def signup(request):
    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/holiday')
        #else:
        #    return redirect('/holiday')

    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, 'holiday/signup.html', args)


def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Hemal Mamtora'
    args = {'myName' : name, 'numbers':numbers}
    return render(request, 'holiday/home.html', args)

def holidays_view(request):
    holidays = Holidays.objects.all()
    photo = holidays.values('photo')
    return render(request, 'holiday/holidays.html', {'holidays': holidays, 'photo':photo})

def flights_view(request):
    flights = Flight.objects.all()
    to = request.GET.get('to')
    fro = request.GET.get('fro')
    if to:
        flights = flights.filter(to__icontains = to)
    if fro:
        flights = flights.filter(fro__icontains = fro)
    return render(request, 'holiday/flights.html', {'flights' : flights})

def hotels_view(request):
    hotels = Hotel.objects.all()
    return render(request, 'holiday/hotels.html', {'hotels' : hotels})
