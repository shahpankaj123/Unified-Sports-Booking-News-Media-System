from venue import models as vmd
from mainapp import models as md

from mainapp.selectors.common_functions import message

from django.db.models import F

class VenueModule:
    
    def __init__(self , data, request):
        self.request = request
        self.data = data

    def get_venue_data(self):
        try:
            venue_obj = vmd.Venue.objects.get(Owner__Email = self.request.user)
            venue_img = venue_obj.venue_images.all()
            data = vmd.Venue.objects.values(venueId = F('VenueID') , venueName = F('Name'),address = F('Address'),cityName = F('City__CityName'), latitude =F('Latitude'), longitude =F('Longitude'),phoneNumber = F('PhoneNumber'),email = F('Email'),desc = F('Description'),openingTime = F('OpeningTime'),closingTime =F('ClosingTime'),isActive = F('IsActive')).get(Owner__Email = self.request.user)
            data['venueImage'] = ["http://127.0.0.1:8000/media/" + x['Image'] for x in  venue_img.values('Image')]
            return data , 200
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500  

    def update_venue_data(self):
        try:
            venue_name  = self.data['venueName']
            address = self.data['address']
            city_id = self.data['cityId']
            latitude = self.data['latitude']
            longitude = self.data['longitude']
            phone_number = self.data['phoneNumber']
            email = self.data['email']
            desc = self.data['desc']
            opening_time = self.data['openingTime']
            closing_time = self.data['closingTime']
            is_active = self.data['isActive']

            venue = vmd.Venue.objects.get(Owner__Email = self.request.user)

            venue.Name = venue_name
            venue.Address = address
            venue.City = md.City.objects.get(CityID = city_id)
            venue.Latitude = latitude
            venue.Longitude = longitude
            venue.PhoneNumber = phone_number
            venue.Email = email
            venue.Description = desc
            venue.OpeningTime =opening_time
            venue.ClosingTime = closing_time
            venue.IsActive = is_active
            venue.save()
            return message('Venue Updated Successfully'), 200
        
        except vmd.Venue.DoesNotExist:
            return message('Venue Not Found'), 404
        except md.City.DoesNotExist:        
            return message('City Not Found'), 404
        except KeyError as k:
            return message(f'{k} is Missing'), 400
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500 

    def upload_venue_image(self):   
        try:
            image = self.request.FILES['image']
            venue = vmd.Venue.objects.get(Owner__Email = self.request.user)
            vmd.VenueImages.objects.create(Venue = venue , Image = image)
            return message('Venue Image Uploaded Successfully'), 200
        except vmd.Venue.DoesNotExist:
            return message('Venue Not Found'), 404
        except KeyError as k:
            return message(f'{k} is Missing'), 400
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500     