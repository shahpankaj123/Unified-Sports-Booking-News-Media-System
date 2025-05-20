from mainapp import models as md

from venue import models as smd

from mainapp.selectors.common_functions import message

from django.db.models import F
from django.utils import timezone


class VenueApplicationModule:

    def __init__(self ,data):
        self.data = data

    def get_all_venue_application(self):

        try:
            return smd.VenueApplication.objects.all().values() ,200

        except Exception as e:
            print(e)
            return message('Somethign Went Wrong'),500
        
    def get_venue_application_by_id(self):
        try:
            appication_id = self.data['applicationId']
            doc_list = []
            application_data = smd.VenueApplication.objects.get(ID = appication_id)
            application_data.reviewed_at = timezone.now()
            application_data.save()
            doc_data = application_data.documents.all()
            data = smd.VenueApplication.objects.values().get(ID = appication_id)
            for d in doc_data:
                doc_list.append({"file":"http://127.0.0.1:8000" + d.DocumentFile.url , "docType" : d.DocumentType})
            data['document'] = doc_list
            return data ,200
        except KeyError as key:
            return message(f'{key} is Missing')
        except Exception as e:
            print(e)
            return message('Somethign Went Wrong'),500  

    def update_status_application(self):
        try:
            appication_id = self.data['applicationId']
            status = self.data['status']

            application_data = smd.VenueApplication.objects.get(ID = appication_id)
            application_data.Status = status
            application_data.save()

            return message('Application Status Updated'),200
        except KeyError as key:
            return message(f'{key} is Missing')
        except Exception as e:
            print(e)
            return message('Somethign Went Wrong'),500  

