from rest_framework.views import APIView
from rest_framework.response import Response

from mainapp.selectors.common_functions import message


from api.module.media_module import SocialMediaModule

from api.module.venue_module import VenueModule

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

