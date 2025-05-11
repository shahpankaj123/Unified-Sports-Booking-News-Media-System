from mainapp.selectors.common_functions import message,is_none

from mainapp import models as md

from django.db.models import Q,F
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from django.http import HttpResponseRedirect

import random
from django.utils import timezone 
from datetime import timedelta

class AccountSetupModule:

    def __init__(self,data):
        self.data = data
        self.now = timezone.now()
        self.date = timezone.now().date()
        self.time = timezone.now().time()

    def create_account(self):
        try:
            first_name = self.data['firstName']
            last_name = self.data['lastName']
            email = self.data['email']
            phone_number = self.data['phoneNumber']
            user_name = self.data['userName']
            password = self.data['password']

            if md.Users.objects.filter(Email = email).exists():
                return message('Email Already Exists') ,400
            
            if md.Users.objects.filter(PhoneNumber = phone_number).exists():
                return message('Phone Number Already Exists') ,400
            
            if md.Users.objects.filter(UserName = user_name).exists():
                return message('UserName Already Exists') ,400
            
            user = md.Users(FirstName = first_name , LastName = last_name , UserName = user_name ,Email = email ,PhoneNumber = phone_number , IsActive = False , UserType = md.UserTypes.objects.get(UserType = 'NormalUsers'))
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_url = 'http://127.0.0.1:8000/web/api/v1/account/user/activate/'+ uid + '/' + token
            print(activation_url)
            # send_activation_email.delay(user.email, activation_url)
            user.set_password(password)
            user.save()
            return message('Account Created Successfully.Please Check Mail for Activating Account !') ,201
        
        except KeyError as key:
            return message(f'{key} is Missing') , 404
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500   

    def activate_user_account(self, id, token):
        if is_none(id)  or is_none(token):
            return message('UnAuthorized Requests') ,402
        
        id=force_str(urlsafe_base64_decode(id))
        user = md.Users.objects.get(UserID = id)

        if default_token_generator.check_token(user, token):
            if user.is_active:
                return False , 400
            user.IsActive = True
            user.save()
            return True , 200
        else:
            return False , 400    

    def user_login(self,request):
        try:
            email = self.data['email']
            password = self.data['password']

            user = md.Users.objects.get(Email = email)    
            if authenticate(request, username=email, password=password):
                if user.IsActive:
                    login(request,user)
                    token, created = Token.objects.get_or_create(user=user)  
                    user_details = {
                        'token' : token.key,
                        'email' : user.Email,
                        'userName' : user.UserName ,
                        'fullName' : user.FirstName + ' ' + user.LastName ,
                        'phoneNumber' : user.PhoneNumber,
                        'userType': user.UserType.UserType
                    }
                    user.LoginStatus = 'Login'
                    user.LoginTry = user.LoginTry + 1
                    user.save()
                    return user_details , 200
                return message('User Account is InActive.') , 402 
            return message('Invalid Email or Password') ,400
        except KeyError as key:
            return message(f'{key} is Missing') ,404
        except md.Users.DoesNotExist:
            return message(f'User Not Found') ,404
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500  
        
    def send_otp_for_password_change(self):
        valid_datetime = self.now + timedelta(minutes=5)
        valid_time = valid_datetime.time()
        try:
            email = self.data['email']
            if is_none(email):
                return message('Invalid Email'), 404
            user = md.Users.objects.get(Email=email)
            if user is not None:
                otp = int(random.randint(1000,10000))
                md.OTPData.objects.create(OTP = otp , OTPUser = user , ValidDateTill = self.date , ValidTimeTill = valid_time)
                print(otp)
                # send_reset_password_email.delay(email,otp)
                return message('Please check your mail for OTP')  ,200 
            return message('User Not Found') ,400
        except KeyError as key:
            return message(f'{key} is Missing') ,404
        except md.Users.DoesNotExist:
            return message(f'User Not Found') ,404
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500  

    def verify_otp_for_password_change(self):
        try:
            email=self.data['email']
            otp=str(self.data['otp'])

            if is_none(email):
                return message('Email Not Found') ,404
            if is_none(otp):
                return message('OTP Not Found') ,404
    
            user = md.Users.objects.get(Email=email)
            otp_data = md.OTPData.objects.get(OTPUser = user , IsValid = True , ValidDateTill = self.date)
            print(otp , otp_data.OTP ,self.time ,otp_data.ValidTimeTill)

            if self.time <= otp_data.ValidTimeTill:
                if str(otp_data.OTP) == str(otp):
                    otp_data.IsValid = False
                    otp_data.save()
                    return message('OTP Verified Successfully') ,200
                return message('OTP Not Matched') , 400
            return message('OTP Experified') , 400
        except KeyError as key:
            return message(f'{key} is Missing') ,404
        except md.Users.DoesNotExist:
            return message(f'User Not Found') ,404
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500  
        
    def change_password(self):
        email=self.data.get('email')
        passsword=self.data.get('password')
        password1=self.data.get('password1')

        if is_none(email):
            return message('Email Not Found') ,404
        
        if is_none(passsword) and is_none(password1):
            return message('Password Not Found') ,404
        
        if passsword != password1:
            return message('Password and Confirm Password donot Match') ,400
        
        try:    
            user =md.Users.objects.get(Email=email)
        except md.Users.DoesNotExist:
            return message('User Not Found') ,400

        user.set_password(passsword)
        user.save()
        return message('Password Changed Successfully') ,200
    
    def logout_usr(self ,request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            user = md.Users.objects.get(Email = request.user)
            user.LoginStatus = 'LogOut'
            user.save()
            logout(request)
            return message('Logout Successfully'), 200   
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500     




      