from django.urls import path

from redapp import views

urlpatterns = [
    path('',views.function1,name='fun1') ,
    path('table',views.function2,name='fun2'),
    path('update1/<int:id>',views.function3,name='update'),
    path('delete/<int:id>',views.function4,name='delete'),
    path('College',views.function5,name='fun5'),


]