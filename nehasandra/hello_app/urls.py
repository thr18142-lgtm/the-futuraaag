from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='function2'),
    path('add_product/', views.add_product, name='add_product'),
    path('read',views.product_read,name='function3'),
    path('p_edit/<int:id>',views.product_edit,name='edit'),
    path('p_delete/<int:id>',views.product_delete,name='delete'),

]
