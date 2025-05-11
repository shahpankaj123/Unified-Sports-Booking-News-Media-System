from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny

from mainapp.selectors.common_functions import message

from django.http import HttpResponseRedirect
from django.contrib.auth import logout

from mainapp.module.account_setup_module import AccountSetupModule

class UserRegistrationView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data , res_status = AccountSetupModule(data=data).create_account()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)
        
class LoginView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data , res_status = AccountSetupModule(data=data).user_login(request=request)
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500) 

class ActivateUsersView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, id , token ,*args, **kwargs):
        print(id,token)
        try:
            res_data , res_status = AccountSetupModule(data=None).activate_user_account(id=id ,token=token)
            if res_data and res_status == 200:
                return HttpResponseRedirect('http://localhost:5173/verify-email')
            return HttpResponseRedirect('http://localhost:5173/valid-error') 
        except Exception as e:
            print(e)
            return HttpResponseRedirect('http://localhost:5173/valid-error')   

class SendOTPView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        try:
            res_data , res_status = AccountSetupModule(data=data).send_otp_for_password_change()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  

class VerifySendOTPView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data , res_status = AccountSetupModule(data=data).verify_otp_for_password_change()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)   

class ChangePasswordView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data , res_status = AccountSetupModule(data=data).change_password()
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)   


class UserLogoutView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            res_data , res_status = AccountSetupModule(data=data).logout_usr(request=request)
            return Response(res_data,res_status)
        except Exception as e:
            print(e)
            return Response(message('Something Went Wrong'),status=500)  
                                             
            

