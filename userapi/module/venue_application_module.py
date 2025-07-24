from venue import models as vmd
from mainapp import models as md

from mainapp.selectors.common_functions import message

class VenueApplicationModule:

    def __init__(self ,data):
        self.data = data

    def create_application(self):
        try:
            venue_name = self.data['venueName']
            phone_number = self.data['phoneNumber']
            address = self.data['address']
            city_id = self.data['cityId']
            user_id = self.data['userId']
            email = self.data['email']
            pan_number = self.data['panNumber']

            user = md.Users.objects.get(UserID = user_id)
            city = md.City.objects.get(CityID = city_id)

            venue_app = vmd.VenueApplication.objects.create(Applicant = user ,VenueName = venue_name ,Address = address ,City = city ,PhoneNumber = phone_number ,Email = email ,PanNumber = pan_number)
            return {
                'status' : 'Success',
                'applicationId':venue_app.ID
            } ,201

        except KeyError as k:
            return message(f'{k} is Missing') ,400
        except Exception as e:
            print(e)  
            return message(f'Something Went Wrong') ,500    

    def upload_doc(self ,request):
        try:
            application_id = self.data['applicationId']
            venue_application = vmd.VenueApplication.objects.get(ID = application_id)

            pan_file = request.FILES['panFile']
            gov_file = request.FILES['govFile']
            business_lic = request.FILES['businessFile']

            vmd.VenueApplicationDocument.objects.create(Application = venue_application ,DocumentType = 'PAN Card',DocumentFile = pan_file)
            vmd.VenueApplicationDocument.objects.create(Application = venue_application ,DocumentType = 'Government Approval',DocumentFile = gov_file)
            vmd.VenueApplicationDocument.objects.create(Application = venue_application ,DocumentType = 'Business License',DocumentFile = business_lic)

            return message('Document Uploaded Successfully') ,200

        except KeyError as k:
            return message(f'{k} is Missing') ,400
        except Exception as e:
            print(e)  
            return message(f'Something Went Wrong') ,500  

