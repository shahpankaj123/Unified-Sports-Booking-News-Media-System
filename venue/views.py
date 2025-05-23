from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from mainapp.selectors.common_functions import message

from mainapp.mixins import VenueUserPermissionMixin

from adminapp.module.user_details_module import UserDetailsModule
from adminapp.module.adds_module import PostModule
from venue.module.dashboard_module import DashboardModule
from venue.module.venue_module import VenueModule

class GetUserDetailsViews(VenueUserPermissionMixin ,APIView):

    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = UserDetailsModule(data=data ,request=request).get_user_details()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)   

class UpdateUserDetailsViews(VenueUserPermissionMixin ,APIView):

    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = UserDetailsModule(data=data ,request=request).update_user_details()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)      

class UploadUserProfileImageViews(VenueUserPermissionMixin ,APIView):

    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status =UserDetailsModule(data=data ,request=request).upload_profile_img()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  
        
        
# post Views
class GetPostViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = PostModule(data=data ,request=request).get_all_posts()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)
        
class CreatePostViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = PostModule(data=data ,request=request).create_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class GetPostDetailViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = PostModule(data=data ,request=request).get_post_detail()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class UpdatePostViews(VenueUserPermissionMixin ,APIView):   
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = PostModule(data=data ,request=request).update_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)
        
class DeletePostViews(VenueUserPermissionMixin ,APIView):       
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = PostModule(data=data ,request=request).delete_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 
        
class GetDashboardViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = DashboardModule(data=data ,request=request).get_dashboard_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class GetVenueDetailsViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = VenueModule(data=data ,request=request).get_venue_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class UpdateVenueDetailsViews(VenueUserPermissionMixin ,APIView):       
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = VenueModule(data=data ,request=request).update_venue_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class UploadVenueImageViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = VenueModule(data=data ,request=request).upload_venue_image()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)                             
                               