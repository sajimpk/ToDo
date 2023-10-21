from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name="home"),
    path('add',to_list,name="index"),
    path('delete/<int:id>/',delete,name='delete')
]