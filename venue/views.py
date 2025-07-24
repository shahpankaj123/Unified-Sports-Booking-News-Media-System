from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from mainapp import models as md

from mainapp.selectors.common_functions import message

from mainapp.mixins import VenueUserPermissionMixin

from adminapp.module.user_details_module import UserDetailsModule
from venue.module.adds_module import PostModule
from adminapp.module.reels_module import ReelModule
from adminapp.module.config.sport_category_module import SportCategoryModule

from venue.module.dashboard_module import DashboardModule
from venue.module.venue_module import VenueModule
from venue.module.court_module import CourtModule
from venue.module.ticket_module import TicketModule
from venue.module.Booking_module import BookingModule
from venue.module.notification_module import NotificationModule
from venue.module.event_module import EventModule
from venue.module.payment_secret_key_module import PaymentSecreatKeyModule


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
        
class CreateReelViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = ReelModule(data=data ,request=request).create_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class GetReelViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = ReelModule(data=data ,request=request).get_all_posts()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class GetReelByIdViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = ReelModule(data=data ,request=request).get_post_detail()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class UpdateReelViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = ReelModule(data=data ,request=request).update_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class DelReelViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = ReelModule(data=data ,request=request).delete_post()
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
        
class DeleteVenueImageViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = VenueModule(data=data ,request=request).remove_venue_image()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)          

class GetCourtViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = CourtModule(data=data ,request=request).get_court_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class GetCourtByIdViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = CourtModule(data=data ,request=request).get_court_data_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)    

class CreateCourtViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = CourtModule(data=data ,request=request).create_court_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class UpdateCourtViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = CourtModule(data=data ,request=request).update_court_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)
        
class UploadCourtImageViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = CourtModule(data=data ,request=request).upload_court_image()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class CreateTicketViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = TicketModule(data=data).create_ticket()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class GetTicketViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = TicketModule(data=data).get_all_ticket()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class GetTicketByIdViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = TicketModule(data=data).get_ticket_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class UpdateTicketViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = TicketModule(data=data).update_ticket()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class GetBookingViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = BookingModule(data=data).get_all_booking()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)    


class GetBookingByIdViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = BookingModule(data=data).get_booking_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)      

class UpdateBookingStatusViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = BookingModule(data=data).update_booking_details()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class GetNotificationViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = NotificationModule(data=data).get_all_notification()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)   

class GetNotificationByIdViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = NotificationModule(data=data).get_notification_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class CreateEventViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = EventModule(data=data).create_events(request=request)
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class GetEventViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = EventModule(data=data).get_all_event()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class GetEventByIdViews(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = EventModule(data=data).get_event_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class UpdateEventViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = EventModule(data=data).update_event()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class DeleteEventViews(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = EventModule(data=data).del_event()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class GetRegisteredEventsUsers(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = EventModule(data=data).get_all_user_by_event()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)   

class GetSportCategory(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = SportCategoryModule(data=data).get_all_sport_categories()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 
        
class CreateSecreteKey(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = PaymentSecreatKeyModule(data=data).create()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 
        
class UpdateSecreteKey(VenueUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = PaymentSecreatKeyModule(data=data).update()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)         

class GetSecreteKey(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = PaymentSecreatKeyModule(data=data).get()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)     

class GetCity(VenueUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = md.City.objects.all().values() ,200
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)                         

                                                                                                                                                                
                               