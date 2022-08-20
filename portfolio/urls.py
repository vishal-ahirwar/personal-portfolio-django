from django.urls import path
from portfolio.views import Home 
app_name='portfolio'
urlpatterns=[
    path('',Home,name='home')
]