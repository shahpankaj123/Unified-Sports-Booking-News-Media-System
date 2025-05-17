from mainapp import models as mm
from mainapp.selectors.common_functions import message

from django.db.models import F

class StatusModule:

    def __init__(self ,data):
        self.data = data

    def create_status(self):
        try:
            status = self.data['status']
            mm.Status.objects.create(Status= status)
            return message('status Created Successfully') ,201
        except KeyError as key:
            return message(f'{key} is Missing') ,404
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500 

    def get_all_status(self):
        return mm.Status.objects.all().values(statusId = F('StatusID') ,status = F('Status')) , 200
    
    def get_status_by_id(self):
        try:
            status_id = self.data['statusId']
            return mm.Status.objects.values(statusId = F('StatusID') ,status = F('Status')).get(StatusID = status_id) ,200
        except KeyError as key:
            return message(f'{key} is Missing') ,404
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500 
        
    def update_status(self):
        try:
            status = self.data['status']
            status_id = self.data['statusId']

            status_obj = mm.Status.objects.get(StatusID = status_id)
            status_obj.Status = status
            status_obj.save()

            return message('status Updated Successfully') ,200
        except KeyError as key:
            return message(f'{key} is Missing') ,404
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500 

    def del_status(self):
        try:
            status_id = self.data['statusId']

            mm.Status.objects.get(StatusID = status_id).delete()
            
            return message('status Deleted Successfully') ,200
        except KeyError as key:
            return message(f'{key} is Missing') ,404
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500    