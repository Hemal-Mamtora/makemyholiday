from django.urls import path, include
from . import views
from django.contrib.auth.views import login, logout

app_name = 'holidays'
urlpatterns = [
    path('', views.holidays_view, name='home'),
    path('signup/', views.signup, name='signup'), 
    path('login/', login, {'template_name' : 'holiday/login.html'}),
    path('logout/', logout, {'template_name' : 'holiday/logout.html'}),
    path('holidays/', views.holidays_view, name='holidays'),
    path('flights/' ,views.flights_view, name='flights'),
    path('hotels/', views.hotels_view, name='hotels'),
    path('holiday_detail/<int:id>', views.holidays_detail_view, name='holidaydetail'),
    path('hotel_detail/<int:id>', views.hotels_detail_view, name='hoteldetail'),
    path('flight_detail/<int:id>', views.flights_detail_view, name='flightdetail')
]
