from rest_framework.views import APIView
from rest_framework.response import Response

from mainapp.selectors.common_functions import message

from mainapp.mixins import AdminUserPermissionMixin

from adminapp.module.dasboard_module import DashboardModule

class DasboardDataView(AdminUserPermissionMixin ,APIView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        try:
            res_data,res_status = DashboardModule(data=data).get_count_data()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)     