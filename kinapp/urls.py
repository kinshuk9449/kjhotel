from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.index,name='index'),
    path('delhi',views.delhi,name='delhi'),
    path('hyderabad',views.hyderabad,name='hyderabad'),
    path('mumbai',views.mumbai,name='mumbai'),
    path('ludhiana',views.ludhiana,name='ludhiana'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('confirm',views.confirm,name='confirm'),
    path('oldbooking',views.oldbooking,name='oldbooking'),
    path('<str:hotel_name>',views.booking,name='booking'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)