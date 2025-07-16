from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView

from userapi.module.payment_service_module import KhaltiPaymentModule

from mainapp.selectors.common_functions import message

# Create your views here.
class CreateTicketView(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = KhaltiPaymentModule(data=data).booking_ticket()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  
        
class VerifyPaymentView(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        try:
            res_data,res_status = KhaltiPaymentModule(data=data).verify_payment()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class GetBookingData(APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = KhaltiPaymentModule(data=data).get_user_booking_details()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

