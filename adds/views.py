from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from adds import models as ad

import pandas as pd
from django.db.models import F
import json

import pickle
import random
import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from mainapp.selectors.common_functions import message,is_none

from mainapp.mixins import AdminUserPermissionMixin

class CreateDataset(APIView):
    def get(self,request,*args,**kwargs):
        news_qs = ad.Post.objects.all().values(id = F('PostID'), desc = F('Description'), category =F('Category__SportCategory'), title = F('Title'),img = F('PostImage'))
        df = pd.DataFrame(news_qs)
        df.to_csv('Recommendation_model/dataset/dataset.csv',index=False)
        return Response([],200)
    
class TrainModels(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        try:
            news_qs = ad.Post.objects.all().values(id = F('PostID'), desc = F('Description'), category =F('Category__SportCategory'), title = F('Title'),img = F('PostImage'))
            df = pd.DataFrame(news_qs)
            df.to_csv('Recommendation_model/dataset/dataset.csv',index=False)
            time.sleep(2)
            df = pd.read_csv('Recommendation_model/dataset/dataset.csv')
            df['content'] = df['title'] + " "  + df['desc'] + " " + df['category']
            tfidf = TfidfVectorizer(stop_words='english')
            tfidf_matrix = tfidf.fit_transform(df['content'])
            cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

            pickle.dump(df,open('Recommendation_model/model/news_list.pkl','wb'))
            pickle.dump(cosine_sim,open('Recommendation_model/model/similarity.pkl','wb'))

            return Response(message('Models Successfully Trained') ,200)

        except Exception as e:
            print(e)  
            return Response(message('Models Trained Failed') ,500)  
    
class GetRecommendNews(APIView):

    def get_recommendations(self ,df ,model ,news_id,top_n):
        indices = pd.Series(df.index, index=df['id'])
        idx = indices[news_id]
        sim_scores = list(enumerate(model[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        news_indices = [i[0] for i in sim_scores]
        return df.iloc[news_indices][['id', 'title','desc', 'category','img']]
    
    def format_data(self,data):
        return data.to_dict(orient='records')

    def get(self,request,*args,**kwargs):
        try:
            id = request.GET.get('postId')
            if is_none(id):
                list_id =["2fe51bee-0af5-4bea-b7b6-e96517f0e373","7841724e-3651-47fc-b922-7ddfd6afcb89","c6e05cef-5237-47b0-af3d-cb4e761993a5","f9b3cafd-353b-4863-bf5f-96ddf0173414"]
                id = random.choice(list_id)
            df = pd.DataFrame(pickle.load(open('Recommendation_model/model/news_list.pkl','rb')))
            model = pd.DataFrame(pickle.load(open('Recommendation_model/model/similarity.pkl','rb')))
            data = self.get_recommendations(df=df ,model=model ,news_id= id ,top_n=5)
            final_data = self.format_data(data=data)
            return Response(final_data,200)
        except Exception as e:
            print(e)
            news_qs = ad.Post.objects.all().values(id = F('PostID'), desc = F('Description'), category =F('Category__SportCategory'), title = F('Title'),img = F('PostImage'))[0:5]
            return Response(news_qs,200)

        


        
