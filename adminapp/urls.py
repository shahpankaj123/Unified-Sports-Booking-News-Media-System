from django.urls import path

from adminapp.views import config_views as cvw


urlpatterns = [

    # config urls
    path('GetAllUserType',cvw.GetAllUserTypeView.as_view()),
    path('GetUserTypeById',cvw.GetUserTypeByIdView.as_view()),
    path('CreateUserType',cvw.CreateUserTypeView.as_view()),
    path('UpdateUserType',cvw.UpdateUserTypeView.as_view()),
    path('DelUserType',cvw.DelUserTypeView.as_view()),

    path('GetAllCity', cvw.GetAllCityView.as_view()),
    path('GetCityById', cvw.GetCityByIdView.as_view()),
    path('CreateCity', cvw.CreateCityView.as_view()),
    path('UpdateCity', cvw.UpdateCityView.as_view()),
    path('DelCity', cvw.DelCityView.as_view()),

    path('GetAllPaymentType', cvw.GetAllPaymentTypeView.as_view()),
    path('GetPaymentTypeById', cvw.GetPaymentTypeByIdView.as_view()),
    path('CreatePaymentType', cvw.CreatePaymentTypeView.as_view()),
    path('UpdatePaymentType', cvw.UpdatePaymentTypeView.as_view()),
    path('DelPaymentType', cvw.DelPaymentTypeView.as_view()),

    path('GetAllStatus', cvw.GetAllStatusView.as_view()),
    path('GetStatusById', cvw.GetStatusByIdView.as_view()),
    path('CreateStatus', cvw.CreateStatusView.as_view()),
    path('UpdateStatus', cvw.UpdateStatusView.as_view()),
    path('DelStatus', cvw.DelStatusView.as_view()),

    path('GetAllSportCategory', cvw.GetAllSportCategoryView.as_view()),
    path('GetSportCategoryById', cvw.GetSportCategoryByIdView.as_view()),
    path('CreateSportCategory', cvw.CreateSportCategoryView.as_view()),
    path('UpdateSportCategory', cvw.UpdateSportCategoryView.as_view()),
    path('DelSportCategory', cvw.DelSportCategoryView.as_view()),

    path('GetAllGender', cvw.GetAllGenderView.as_view()),
    path('GetGenderById', cvw.GetGenderByIdView.as_view()),
    path('CreateGender', cvw.CreateGenderView.as_view()),
    path('UpdateGender', cvw.UpdateGenderView.as_view()),
    path('DelGender', cvw.DelGenderView.as_view()),

]