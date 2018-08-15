from django.urls import path, include
from . import views
from django.contrib.auth.views import login
app_name = 'holiday'
urlpatterns = [
    path('', views.home),
    path('signup/', views.SignUp.as_view(), name='signup'), 
    path('login/', login, {'template_name' : 'holiday/login.html'})
]
