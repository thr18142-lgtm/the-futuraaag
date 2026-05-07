from django.urls import path
from . import views
urlpatterns = [
    path('',views.function1,name='fun'),
    path('jaja',views.function3,name='fun3'),
]
