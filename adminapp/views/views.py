from rest_framework.views import APIView
from rest_framework.response import Response

from mainapp.selectors.common_functions import message

from mainapp.mixins import AdminUserPermissionMixin

from adminapp.module.dasboard_module import DashboardModule
from adminapp.module.venue_module import VenueModule
from adminapp.module.adds_module import PostModule
from adminapp.module.reels_module import ReelModule
from adminapp.module.venue_application_module import VenueApplicationModule
from adminapp.module.user_details_module import UserDetailsModule
from adminapp.module.booking_module import BookingModule

from venue.module.notification_module import NotificationModule
from venue.module.event_module import EventModule

class DasboardDataView(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = DashboardModule(data=data).get_count_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class CreateVenueViews(AdminUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = VenueModule(data=data).create_venue()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 
        
class GetVenueViews(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = VenueModule(data=data).get_all_venue()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class UpdateVenueStatusViews(AdminUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = VenueModule(data=data).update_status_venue()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class GetVenueDetailsViews(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = VenueModule(data=data).get_venue_details(request=request)
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

# ------- adds views ----------

class CreatePostViews(AdminUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = PostModule(data=data ,request=request).create_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class GetPostViews(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = PostModule(data=data ,request=request).get_all_posts()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class GetPostByIdViews(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = PostModule(data=data ,request=request).get_post_detail()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class UpdatePostViews(AdminUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = PostModule(data=data ,request=request).update_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class DelPostViews(AdminUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = PostModule(data=data ,request=request).delete_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  
        
class CreateReelViews(AdminUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = ReelModule(data=data ,request=request).create_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class GetReelViews(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = ReelModule(data=data ,request=request).get_all_posts()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class GetReelByIdViews(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = ReelModule(data=data ,request=request).get_post_detail()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)

class UpdateReelViews(AdminUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = ReelModule(data=data ,request=request).update_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class DelReelViews(AdminUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = ReelModule(data=data ,request=request).delete_post()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)         

class GetVenueApplicationViews(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = VenueApplicationModule(data=data).get_all_venue_application()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)    

class GetVenueApplicationByIdViews(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = VenueApplicationModule(data=data).get_venue_application_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class UpdateVenueApplicationViews(AdminUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = VenueApplicationModule(data=data).update_status_application()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)       

class GetUserDetailsViews(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = UserDetailsModule(data=data ,request=request).get_user_details()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)   

class UpdateUserDetailsViews(AdminUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = UserDetailsModule(data=data,request=request).update_user_details()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)      

class UploadUserProfileImageViews(AdminUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = UserDetailsModule(data=data,request=request).upload_profile_img()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class GetNotificationViews(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = NotificationModule(data=data,request=request).get_all_notification()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)   

class GetNotificationByIdViews(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = NotificationModule(data=data,request=request).get_notification_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)    

class GetEventViews(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = EventModule(data=data).all_events()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class GetEventByIdViews(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = EventModule(data=data).get_event_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class GetVenuePaymentMethodData(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = VenueModule(data=data).get_venue_payment_method_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)     

class GetBookingViews(APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = BookingModule(data=data).get_all_booking()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)                                                                                                                                             
        

