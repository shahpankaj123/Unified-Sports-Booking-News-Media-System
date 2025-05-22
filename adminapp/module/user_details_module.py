from mainapp import models as md
from django.db.models import F,Value,CharField
from django.db.models.functions import Concat

from mainapp.selectors.common_functions import message

class UserDetailsModule:

    def __init__(self ,data):
        self.data = data

    def get_user_details(self):
        try:
            user_id = self.data['userId']
            
            user_data = md.Users.objects.values(
                firstName=F('FirstName'),
                lastName=F('LastName'),
                profileImage=Concat(
                    Value('http://127.0.0.1:8000/media/'),
                    F('ProfileImage'),
                    output_field=CharField()
                ),
                email=F('Email'),
                userName=F('UserName'),
                phoneNumber=F('PhoneNumber')
            ).get(UserID=user_id)

            return user_data, 200

        except md.Users.DoesNotExist:
            return message('User Not Found'), 404
        except Exception as e:
            return message('Something Went Wrong'), 500
        
        
    def update_user_details(self):
        try:
            user_id = self.data['userId']
            first_name = self.data['firstName']
            last_name = self.data['lastName']
            usr_name = self.data['userName']
            phone_number = self.data['phoneNumber']

            if md.Users.objects.filter(PhoneNumber = phone_number).exists():
                return message('Phone Number Already Exists'),400
            
            if md.Users.objects.filter(UserName = usr_name).exists():
                return message('UserName Already Exists'),400
            
            usr = md.Users.objects.get(UserID = user_id) 
            usr.FirstName = first_name
            usr.LastName = last_name
            usr.UserName = usr_name
            usr.PhoneNumber = phone_number
            usr.save()

            return message('User Data Updated Successfully'),200
        except KeyError as k:
            return message(f'{k} is Missing') ,400
        except md.Users.DoesNotExist:
            return message('User Not Foound'),404
        except Exception as e:
            return message('Something Went Wrong'),500   

    def upload_profile_img(self,request):
        try:
            profile_img = request.FILES['profileImage']
            user_id = self.data['userId']

            usr = md.Users.objects.get(UserID = user_id) 
            usr.ProfileImage = profile_img
            usr.save()
            return message('Profile Image Uploaded Successfully'),200

        except KeyError as k:
            return message(f'{k} is Missing') ,400
        except md.Users.DoesNotExist:
            return message('User Not Foound'),404
        except Exception as e:
            return message('Something Went Wrong'),500      



      