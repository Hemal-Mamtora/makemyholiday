from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from holiday.forms import RegistrationForm
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