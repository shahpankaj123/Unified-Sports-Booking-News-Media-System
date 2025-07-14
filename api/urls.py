from django.urls import path
from api import views as v


urlpatterns = [
    path('GetPost', v.GetPost.as_view()),
    path('GetPostById', v.GetPostById.as_view()),

    path('GetReel', v.GetReel.as_view()),
    path('GetReelById', v.GetReelById.as_view()),

    path('GetVenue',v.GetVenue.as_view()),
    path('GetVenueById',v.GetVenueById.as_view()),

    path('GetCourt',v.GetCourt.as_view()),
    path('GetCourtById',v.GetCourtById.as_view()),

    path('GetTicket',v.GetTicketViews.as_view()),
    path('GetTicketById',v.GetTicketByIdViews.as_view()),

    path('GetEvent',v.GetEventViews.as_view()),
    path('GetEventById',v.GetEventByIdViews.as_view()),

    path('GetCountData',v.GetCountData.as_view()),

    path('GetPaymentType',v.GetPaymentType.as_view()),
]