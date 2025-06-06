from django.urls import path

from venue import views as vv

urlpatterns = [

    path('GetUserDetails',vv.GetUserDetailsViews.as_view()),
    path('UpdateUserDetails',vv.UpdateUserDetailsViews.as_view()),
    path('UploadProfileImage',vv.UploadUserProfileImageViews.as_view()),

    path('GetPost',vv.GetPostViews.as_view()),
    path('CreatePost',vv.CreatePostViews.as_view()),
    path('UpdatePost',vv.UpdatePostViews.as_view()),
    path('DeletePost',vv.DeletePostViews.as_view()),
    path('GetPostDetails',vv.GetPostDetailViews.as_view()),

    path('GetDashboardData',vv.GetDashboardViews.as_view()),
    path('GetVenueDetails',vv.GetVenueDetailsViews.as_view()),
    path('UpdateVenueDetails',vv.UpdateVenueDetailsViews.as_view()),
    path('UploadVenueImage',vv.UploadVenueImageViews.as_view()),

    path('GetCounrt',vv.GetCourtViews.as_view()),
    path('GetCounrtById',vv.GetCourtByIdViews.as_view()),
    path('CreateCourt',vv.CreateCourtViews.as_view()),
    path('UpdateCourt',vv.UpdateCourtViews.as_view()),
    path('UploadCourtImage',vv.UploadCourtImageViews.as_view()),

    path('CreateTicket',vv.CreateTicketViews.as_view()),
    path('GetTicket',vv.GetTicketViews.as_view()),
    path('GetTicketById',vv.GetTicketByIdViews.as_view()),
    path('UpdateTicket',vv.UpdateTicketViews.as_view()),

    path('GetBooking',vv.GetBookingViews.as_view()),
    path('GetBookingById',vv.GetBookingByIdViews.as_view()),
    path('UpdateBookingStatus',vv.UpdateBookingStatusViews.as_view()),

    path('GetNotification',vv.GetNotificationViews.as_view()),
]
