from django.urls import path

from userapi import views as vv

urlpatterns = [
        path('CreateTicket',vv.CreateTicketView.as_view()),
        path('VerifyPayment',vv.VerifyPaymentView.as_view()),
        path('GetBookingData',vv.GetBookingData.as_view()),

        path('GetDashBoardData',vv.GetDashBoardData.as_view()),

        path('GetNotification',vv.GetNotificationViews.as_view()),
        path('GetNotificationById',vv.GetNotificationByIdViews.as_view()),
]