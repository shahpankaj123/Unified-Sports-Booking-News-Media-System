from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from mainapp.selectors.common_functions import message

from mainapp.mixins import VenueUserPermissionMixin

from adminapp.module.user_details_module import UserDetailsModule
from adminapp.module.adds_module import PostModule
from venue.module.dashboard_module import DashboardModule
from venue.module.venue_module import VenueModule
from venue.module.court_module import CourtModule
from venue.module.ticket_module import TicketModule

class GetUserDetailsViews(APIView):

    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = UserDetailsModule(data=data ,request=request).get_user_details()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)   

class UpdateUserDetailsViews(APIView):

    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = UserDetailsModule(data=data ,request=request).update_user_details()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)      

class UploadUserProfileImageViews(APIView):

    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status =UserDetailsModule(data=data ,request=request).upload_profile_img()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  
        
        
# post Views
class GetPostViews(APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = PostModule(data=data ,request=request).get_all_posts()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)
        
class CreatePostViews(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = PostModule(data=data ,request=request).create_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class GetPostDetailViews(APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = PostModule(data=data ,request=request).get_post_detail()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class UpdatePostViews(APIView):   
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = PostModule(data=data ,request=request).update_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)
        
class DeletePostViews(APIView):       
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = PostModule(data=data ,request=request).delete_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 
        
class GetDashboardViews(APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = DashboardModule(data=data ,request=request).get_dashboard_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class GetVenueDetailsViews(APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = VenueModule(data=data ,request=request).get_venue_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class UpdateVenueDetailsViews(APIView):       
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = VenueModule(data=data ,request=request).update_venue_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class UploadVenueImageViews(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = VenueModule(data=data ,request=request).upload_venue_image()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class GetCourtViews(APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = CourtModule(data=data ,request=request).get_court_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class GetCourtByIdViews(APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = CourtModule(data=data ,request=request).get_court_data_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)    

class CreateCourtViews(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = CourtModule(data=data ,request=request).create_court_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class UpdateCourtViews(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = CourtModule(data=data ,request=request).update_court_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)
        
class UploadCourtImageViews(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = CourtModule(data=data ,request=request).upload_court_image()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class CreateTicketViews(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = TicketModule(data=data).create_ticket()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class GetTicketViews(APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = TicketModule(data=data).get_all_ticket()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class GetTicketByIdViews(APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = TicketModule(data=data).get_ticket_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class UpdateTicketViews(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = TicketModule(data=data).update_ticket()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)                                                                                                  
                               