from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from mainapp.selectors.common_functions import message

from mainapp.mixins import VenueUserPermissionMixin

from adminapp.module.user_details_module import UserDetailsModule


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
