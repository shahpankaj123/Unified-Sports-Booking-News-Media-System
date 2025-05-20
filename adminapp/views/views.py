from rest_framework.views import APIView
from rest_framework.response import Response

from mainapp.selectors.common_functions import message

from mainapp.mixins import AdminUserPermissionMixin

from adminapp.module.dasboard_module import DashboardModule
from adminapp.module.venue_module import VenueModule
from adminapp.module.adds_module import PostModule
from adminapp.module.venue_application_module import VenueApplicationModule

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
        

