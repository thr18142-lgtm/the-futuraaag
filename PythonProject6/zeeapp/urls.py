from django.urls import path

from zeeapp import views

urlpatterns = [
    path('home',views.home,name='home'),

]