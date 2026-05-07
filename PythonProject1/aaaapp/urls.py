from django.urls import path
from . import views

urlpatterns = [
    path('',views.functions1,name='fun'),
    path('first',views.functions2,name="fun2")


    
]
