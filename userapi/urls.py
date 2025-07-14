from django.urls import path

from userapi import views as vv

urlpatterns = [

path('CreateTicket',vv.CreateTicketView.as_view()),

]