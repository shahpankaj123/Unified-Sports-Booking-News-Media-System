from mainapp import models as mm
from mainapp.selectors.common_functions import message

from django.db.models import F

class UserTypeModule:

    def __init__(self ,data):
        self.data = data

    def create_user_type(self):
        try:
            user_type = self.data['userType']
            mm.UserTypes.objects.create(UserType = user_type)
            return message('UserType Created Successfully') ,201
        except KeyError as key:
            return message(f'{key} is Missing') ,404
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500 

    def get_all_userType(self):
        return mm.UserTypes.objects.all().values(userTypeId = F('UserTypeID') ,userType = F('UserType')) , 200
    
    def get_userType_by_id(self):
        try:
            user_type_id = self.data['userTypeId']
            return mm.UserTypes.objects.values(userTypeId = F('UserTypeID') ,userType = F('UserType')).get(UserTypeID = user_type_id)
        except KeyError as key:
            return message(f'{key} is Missing') ,404
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500 
        
    def update_usertype(self):
        try:
            user_type_id = self.data['userTypeId']
            user_type = self.data['userType']

            user_type_obj = mm.UserTypes.objects.get(UserTypeID = user_type_id)
            user_type_obj.UserType = user_type
            user_type_obj.save()

            return message('UserType Updated Successfully') ,200
        except KeyError as key:
            return message(f'{key} is Missing') ,404
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500 

    def del_usertype(self):
        try:
            user_type_id = self.data['userTypeId']

            mm.UserTypes.objects.get(UserTypeID = user_type_id).delete()
            
            return message('UserType Deleted Successfully') ,200
        except KeyError as key:
            return message(f'{key} is Missing') ,404
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500       
