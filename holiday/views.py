from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
'''
class SignupView():
    pass
'''
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'holiday/signup.html'

def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Hemal Mamtora'
    args = {'myName' : name, 'numbers':numbers}
    return render(request, 'holiday/home.html', args)