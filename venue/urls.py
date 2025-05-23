from django.urls import path

from venue import views as vv

urlpatterns = [

    path('GetUserDetails',vv.GetUserDetailsViews.as_view()),
    path('UpdateUserDetails',vv.UpdateUserDetailsViews.as_view()),
    path('UploadProfileImage',vv.UploadUserProfileImageViews.as_view()),

]
