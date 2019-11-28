from django.contrib import admin
from .models import KjHotel,details,data

# Register your models here.
class KjHotel_admin(admin.ModelAdmin):
    list_display = ('id','email','mobile','profile')

class details_admin(admin.ModelAdmin):
    list_display=('id','city','hotel_name','price','pic1')

class booking_admin(admin.ModelAdmin):
    list_display=('id','email','checkin','checkout','amount','hotel')

admin.site.register(KjHotel,KjHotel_admin)
admin.site.register(details,details_admin)
admin.site.register(data,booking_admin)