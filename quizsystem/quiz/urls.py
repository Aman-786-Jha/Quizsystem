from django.urls import path 
from . import views 

urlpatterns = [
    path('details/',views.details,name='details'),
    path('',views.index,name='index'),
    path('single-details/<int:pk>',views.single_details,name='single-details')
]
