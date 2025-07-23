from django.urls import path

from adds import views as vv

urlpatterns = [

    path('CreateDataset',vv.CreateDataset.as_view()),
    path('TrainModels',vv.TrainModels.as_view()),
    path('GetRecommendationNews',vv.GetRecommendNews.as_view()),

]