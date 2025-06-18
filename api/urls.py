from django.urls import path
from api import views as v


urlpatterns = [
    path('GetPost', v.GetPost.as_view()),
    path('GetPostById', v.GetPostById.as_view()),

    path('GetReel', v.GetReel.as_view()),
    path('GetReelById', v.GetReelById.as_view()),
]