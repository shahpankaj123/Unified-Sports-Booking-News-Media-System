from rest_framework.views import APIView
from rest_framework.response import Response

from mainapp.selectors.common_functions import message

from mainapp.module.account_setup_module import AccountSetupModule

class UserRegistrationView(APIView):

    def post(self,request ,**args):
        data = request.data
        try:
            res_data , res_status = AccountSetupModule(data=data).create_account()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)
        
class LoginView(APIView):

    def post(self,request ,**args):
        data = request.data
        try:
            res_data , res_status = AccountSetupModule(data=data).user_login()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)        
            

