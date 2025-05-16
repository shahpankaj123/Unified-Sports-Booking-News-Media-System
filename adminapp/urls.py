from django.urls import path

from adminapp.views import config_views as cvw


urlpatterns = [

    # config urls
    path('v1/GetAllUserType',cvw.GetAllUserTypeView.as_view()),
    path('v1/GetUserTypeById',cvw.GetUserTypeByIdView.as_view()),
    path('v1/CreateUserType',cvw.CreateUserTypeView.as_view()),
    path('v1/UpdateUserType',cvw.UpdateUserTypeView.as_view()),
    path('DelUserType',cvw.DelUserTypeView.as_view()),

    path('v1/GetAllCity', cvw.GetAllCityView.as_view()),
    path('v1/GetCityById', cvw.GetCityByIdView.as_view()),
    path('v1/CreateCity', cvw.CreateCityView.as_view()),
    path('v1/UpdateCity', cvw.UpdateCityView.as_view()),
    path('v1/DelCity', cvw.DelCityView.as_view()),

    path('v1/GetAllPaymentType', cvw.GetAllPaymentTypeView.as_view()),
    path('v1/GetPaymentTypeById', cvw.GetPaymentTypeByIdView.as_view()),
    path('v1/CreatePaymentType', cvw.CreatePaymentTypeView.as_view()),
    path('v1/UpdatePaymentType', cvw.UpdatePaymentTypeView.as_view()),
    path('v1/DelPaymentType', cvw.DelPaymentTypeView.as_view()),

    path('v1/GetAllStatus', cvw.GetAllStatusView.as_view()),
    path('v1/GetStatusById', cvw.GetStatusByIdView.as_view()),
    path('v1/CreateStatus', cvw.CreateStatusView.as_view()),
    path('v1/UpdateStatus', cvw.UpdateStatusView.as_view()),
    path('v1/DelStatus', cvw.DelStatusView.as_view()),

    path('v1/GetAllSportCategory', cvw.GetAllSportCategoryView.as_view()),
    path('v1/GetSportCategoryById', cvw.GetSportCategoryByIdView.as_view()),
    path('v1/CreateSportCategory', cvw.CreateSportCategoryView.as_view()),
    path('v1/UpdateSportCategory', cvw.UpdateSportCategoryView.as_view()),
    path('v1/DelSportCategory', cvw.DelSportCategoryView.as_view()),

    path('v1/GetAllGender', cvw.GetAllGenderView.as_view()),
    path('v1/GetGenderById', cvw.GetGenderByIdView.as_view()),
    path('v1/CreateGender', cvw.CreateGenderView.as_view()),
    path('v1/UpdateGender', cvw.UpdateGenderView.as_view()),
    path('v1/DelGender', cvw.DelGenderView.as_view()),

]