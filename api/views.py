from rest_framework.views import APIView
from rest_framework.response import Response

from mainapp.selectors.common_functions import message

from mainapp import models as md


from api.module.media_module import SocialMediaModule
from api.module.venue_module import VenueModule
from api.module.extra_module import ExtraModule

from venue.module.ticket_module import TicketModule
from venue.module.event_module import EventModule


class GetPost(APIView):

    def get(self, request, *args, **kwargs):
        try:
            res_data ,res_status = SocialMediaModule(data=None).get_news_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong') ,500 )  
        
class GetPostById(APIView):
    
    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data ,res_status = SocialMediaModule(data=data).get_news_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong') ,500 )   

class GetReel(APIView):

    def get(self, request, *args, **kwargs):
        try:
            res_data ,res_status = SocialMediaModule(data=None).get_reels_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong') ,500 )  
        
class GetReelById(APIView):
    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data ,res_status = SocialMediaModule(data=data).get_reel_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong') ,500 )  

class GetVenue(APIView):

    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data ,res_status = VenueModule(data= data).get_all_venue()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong') ,500 )
        
class GetVenueById(APIView):

    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data ,res_status = VenueModule(data= data).get_venue_details()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong') ,500 )        

class GetCourt(APIView):

    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data ,res_status = VenueModule(data= data).get_all_courts()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong') ,500 )  

class GetCourtById(APIView):

    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data ,res_status = VenueModule(data= data).court_details()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong') ,500 )   

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

class GetEventViews(APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = EventModule(data=data).all_events()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class GetEventByIdViews(APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = EventModule(data=data).get_event_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class GetCountData(APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = ExtraModule(data=data).get_count_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)   

class GetPaymentType(APIView):
    def get(self,request,*args,**kwargs):
        try:
            payment = md.PaymentType.objects.all().values()
            return Response(payment,status = 200)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)                                                                         

