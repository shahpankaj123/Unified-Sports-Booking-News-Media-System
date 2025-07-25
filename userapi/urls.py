from django.urls import path

from userapi import views as vv

urlpatterns = [
    path('CreateTicket',vv.CreateTicketView.as_view()),
    path('VerifyPayment',vv.VerifyPaymentView.as_view()),

    path('GetBookingData',vv.GetBookingData.as_view()),

    path('GetDashBoardData',vv.GetDashBoardData.as_view()),

    path('GetNotification',vv.GetNotificationViews.as_view()),
    path('GetNotificationById',vv.GetNotificationByIdViews.as_view()),

    path('RegisteredEvent',vv.RegisteredEventViews.as_view()),
    path('GetRegisteredEvent',vv.GetRegisteredEventViews.as_view()),

    path('CreateVenueApplication',vv.CreateVenueApplication.as_view()),
    path('UploadVenueApplicationDoc',vv.UploadVenueApplicationDoc.as_view()),

    path('GetCity',vv.GetCity.as_view()),
]