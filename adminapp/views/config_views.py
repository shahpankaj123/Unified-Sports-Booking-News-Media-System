from rest_framework.views import APIView
from rest_framework.response import Response

from mainapp.mixins import AdminUserPermissionMixin

from mainapp.selectors.common_functions import message

from adminapp.module.config.user_type_crud_module import UserTypeModule
from adminapp.module.config.city_crud_module import CityModule
from adminapp.module.config.payment_method_crud_module import PaymentTypeModule
from adminapp.module.config.status_crud_module import StatusModule
from adminapp.module.config.sport_category_module import SportCategoryModule
from adminapp.module.config.gender_crud_module import GenderModule


class GetAllUserTypeView(AdminUserPermissionMixin ,APIView):

    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data , res_status = UserTypeModule(data=data).get_all_userType()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 
        
class GetUserTypeByIdView(AdminUserPermissionMixin ,APIView):

    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data , res_status = UserTypeModule(data=data).get_userType_by_id()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)   

class CreateUserTypeView(AdminUserPermissionMixin ,APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data , res_status = UserTypeModule(data=data).create_user_type()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)    

class UpdateUserTypeView(AdminUserPermissionMixin ,APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data , res_status = UserTypeModule(data=data).update_usertype()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class DelUserTypeView(AdminUserPermissionMixin ,APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data , res_status = UserTypeModule(data=data).del_usertype()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)   



class GetAllCityView(AdminUserPermissionMixin, APIView):
    def get(self, request):
        data = request.GET
        try:
            res_data, res_status = CityModule(data=data).get_all_cities()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'), status=500)

class GetCityByIdView(AdminUserPermissionMixin, APIView):
    def get(self, request):
        data = request.GET
        try:
            res_data, res_status = CityModule(data=data).get_city_by_id()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'), status=500)

class CreateCityView(AdminUserPermissionMixin, APIView):
    def post(self, request):
        data = request.data
        try:
            res_data, res_status = CityModule(data=data).create_city()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'), status=500)

class UpdateCityView(AdminUserPermissionMixin, APIView):
    def post(self, request):
        data = request.data
        try:
            res_data, res_status = CityModule(data=data).update_city()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'), status=500)

class DelCityView(AdminUserPermissionMixin, APIView):
    def post(self, request):
        data = request.data
        try:
            res_data, res_status = CityModule(data=data).delete_city()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'), status=500)
        
class GetAllPaymentTypeView(AdminUserPermissionMixin, APIView):
    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data, res_status = PaymentTypeModule(data=data).get_all_payment_types()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class GetPaymentTypeByIdView(AdminUserPermissionMixin, APIView):
    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data, res_status = PaymentTypeModule(data=data).get_payment_type_by_id()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class CreatePaymentTypeView(AdminUserPermissionMixin, APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data, res_status = PaymentTypeModule(data=data).create_payment_type()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class UpdatePaymentTypeView(AdminUserPermissionMixin, APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data, res_status = PaymentTypeModule(data=data).update_payment_type()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class DelPaymentTypeView(AdminUserPermissionMixin, APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data, res_status = PaymentTypeModule(data=data).delete_payment_type()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500) 
        
class GetAllStatusView(AdminUserPermissionMixin, APIView):
    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data, res_status = StatusModule(data=data).get_all_status()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class GetStatusByIdView(AdminUserPermissionMixin, APIView):
    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data, res_status = StatusModule(data=data).get_status_by_id()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class CreateStatusView(AdminUserPermissionMixin, APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data, res_status = StatusModule(data=data).create_status()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class UpdateStatusView(AdminUserPermissionMixin, APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data, res_status = StatusModule(data=data).update_status()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class DelStatusView(AdminUserPermissionMixin, APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data, res_status = StatusModule(data=data).del_status()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)   

class GetAllSportCategoryView(AdminUserPermissionMixin, APIView):
    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data, res_status = SportCategoryModule(data=data).get_all_sport_categories()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class GetSportCategoryByIdView(AdminUserPermissionMixin, APIView):
    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data, res_status = SportCategoryModule(data=data).get_sport_category_by_id()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class CreateSportCategoryView(AdminUserPermissionMixin, APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data, res_status = SportCategoryModule(data=data).create_sport_category()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class UpdateSportCategoryView(AdminUserPermissionMixin, APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data, res_status = SportCategoryModule(data=data).update_sport_category()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class DelSportCategoryView(AdminUserPermissionMixin, APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data, res_status = SportCategoryModule(data=data).delete_sport_category()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)  

class GetAllGenderView(AdminUserPermissionMixin, APIView):
    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data, res_status = GenderModule(data=data).get_all_genders()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class GetGenderByIdView(AdminUserPermissionMixin, APIView):
    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            res_data, res_status = GenderModule(data=data).get_gender_by_id()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class CreateGenderView(AdminUserPermissionMixin, APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data, res_status = GenderModule(data=data).create_gender()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class UpdateGenderView(AdminUserPermissionMixin, APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data, res_status = GenderModule(data=data).update_gender()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)


class DelGenderView(AdminUserPermissionMixin, APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data, res_status = GenderModule(data=data).delete_gender()
            return Response(res_data, res_status)
        except Exception as e:
            print(e)
            return Response(message("Something Went Wrong"), status=500)                   




