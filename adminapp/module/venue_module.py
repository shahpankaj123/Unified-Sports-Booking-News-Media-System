from mainapp import models as md

from venue import models as smd

from mainapp.selectors.common_functions import message

from django.db.models import F

from django.core.exceptions import ObjectDoesNotExist

class VenueModule:

    def __init__(self ,data):
        self.data = data

    def create_venue(self):
        try:
            owner_email = self.data['ownerEmail']
            name = self.data['name']
            address = self.data['address']
            phoneNumber = self.data['phoneNumber']
            email = self.data['email']
            cityId = self.data['cityId']

            user = md.Users.objects.get(Email = owner_email)
            user.UserType = md.UserTypes.objects.get(UserType = 'VenueUsers')
            user.save()

            city = md.City.objects.get(CityID = cityId)

            smd.Venue.objects.create(Owner = user ,Email = email ,PhoneNumber = phoneNumber,Name = name ,Address = address ,City = city ,IsActive = True)
            return message('Venue Created Sucessfully') ,200
        
        except KeyError as key:
            return message(f'{key} is Missing'),400
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500

    def get_all_venue(self):
        try:
            return smd.Venue.objects.all().values(venueID=F('VenueID'),ownerEmail = F('Owner__Email'),name = F('Name'),address = F('Address'),phoneNumber = F('PhoneNumber'),isActive=F('IsActive'),city = F('City__CityName')).order_by('-CreatedAt') ,200
        except Exception as e:
            print(e) 

    def update_status_venue(self):
        try:
            is_active = self.data['isActive']
            venue_id = self.data['venueId']

            venue_obj = smd.Venue.objects.get(VenueID = venue_id)
            venue_obj.IsActive = is_active
            venue_obj.save()
            return message('Status Updated Successfully'),200
        
        except KeyError as key:
            return message(f'{key} is Missing') ,404
        except smd.Venue.DoesNotExist:
            return message('Venue Not Found') ,404
        except Exception as e:
            print(e)
            return message('Something Went Wrong'),500
        


    def get_venue_details(self,request):
        try:
            venue_id = self.data['venueId']
            venue = smd.Venue.objects.select_related('Owner', 'City').prefetch_related(
                'venue_images',
                'venue__courts_images'  # courts_images from Court
            ).get(VenueID=venue_id)

            # Build response manually
            venue_data = {
                "venueID": str(venue.VenueID),
                "name": venue.Name,
                "address": venue.Address,
                "city": venue.City.CityName if venue.City else None,
                "latitude": float(venue.Latitude) if venue.Latitude else None,
                "longitude": float(venue.Longitude) if venue.Longitude else None,
                "phoneNumber": venue.PhoneNumber,
                "email": venue.Email,
                "description": venue.Description,
                "openingTime": venue.OpeningTime.strftime("%H:%M:%S") if venue.OpeningTime else None,
                "closingTime": venue.ClosingTime.strftime("%H:%M:%S") if venue.ClosingTime else None,
                "isActive": venue.IsActive,
                "createdAt": venue.CreatedAt.strftime("%Y-%m-%d %H:%M:%S"),
                "owner": {
                    "firstName": venue.Owner.FirstName if venue.Owner else None,
                    "lastName": venue.Owner.LastName if venue.Owner else None,
                    "email": venue.Owner.Email if venue.Owner else None,
                },
                "venueImages": [
                    {
                        "imageID": str(img.ImageID),
                        "image": request.build_absolute_uri(img.Image.url) if img.Image else None,
                        "createdAt": img.CreatedAt.strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    for img in venue.venue_images.all()
                ],
                "courts": []
            }

            for court in venue.venue.all():  # related_name='venue'
                court_data = {
                    "courtID": str(court.CourtID),
                    "name": court.Name,
                    "sportCategory": court.SportCategory.SportCategory if court.SportCategory else None,
                    "surfaceType": court.SurfaceType,
                    "capacity": court.Capacity,
                    "hourlyRate": float(court.HourlyRate),
                    "isActive": court.IsActive,
                    "createdAt": court.CreatedAt.strftime("%Y-%m-%d %H:%M:%S"),
                    "courtImages": [
                        {
                            "imageID": str(img.ImageID),
                            "image": request.build_absolute_uri(img.Image.url) if img.Image else None,
                            "createdAt": img.CreatedAt.strftime("%Y-%m-%d %H:%M:%S"),
                        }
                        for img in court.courts_images.all()
                    ]
                }
                venue_data["courts"].append(court_data)

            return venue_data ,200

        except ObjectDoesNotExist:
            return message('Venue Not Found') ,400






