from django.urls import path, include
from . import views
from django.contrib.auth.views import login, logout
app_name = 'holiday'
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'), 
    path('login/', login, {'template_name' : 'holiday/login.html'}),
    path('logout/', logout, {'template_name' : 'holiday/logout.html'})
]
