from django.urls import path, include
from . import views

app_name = 'holiday'
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'), 
]
