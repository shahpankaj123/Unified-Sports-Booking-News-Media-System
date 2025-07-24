from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView

from userapi.module.payment_service_module import KhaltiPaymentModule
from userapi.module.dashboard_module import DashBoarModule

from mainapp.selectors.common_functions import message

from mainapp.mixins import NormalUserPermissionMixin
from venue.module.notification_module import NotificationModule
from userapi.module.event_module import EventModule

# Create your views here.
class GetDashBoardData(NormalUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = DashBoarModule(data=data).get_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  
        
class CreateTicketView(NormalUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = KhaltiPaymentModule(data=data).booking_ticket()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  
        
class VerifyPaymentView(NormalUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        print(data)
        try:
            res_data,res_status = KhaltiPaymentModule(data=data).verify_payment()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class GetBookingData(NormalUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = DashBoarModule(data=data).get_user_booking_details()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 
        
class GetNotificationViews(NormalUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = NotificationModule(data=data).get_all_notification()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)   

class GetNotificationByIdViews(NormalUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = NotificationModule(data=data).get_notification_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)   

class RegisteredEventViews(NormalUserPermissionMixin ,APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = EventModule(data=data).registered_event()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class GetRegisteredEventViews(NormalUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = EventModule(data=data).get_registered_details()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)                        

