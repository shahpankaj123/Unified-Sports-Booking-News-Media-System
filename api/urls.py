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
]