from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('balance',views.check_balance),
    path('deposit',views.deposit),
    path('withdraw',views.withdraw),
]