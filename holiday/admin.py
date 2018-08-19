from django.contrib import admin
from holiday.models import Holidays, Flight, Hotel
# Register your models here.
admin.site.register(Holidays)
admin.site.register(Flight)
admin.site.register(Hotel)