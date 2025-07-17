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
        
    def get_court_data_by_id(self):
        try:
            court_id = self.data['courtId']
            court = smd.Court.objects.get(CourtID = court_id)
            court_img = court.courts_images.all()
            data = smd.Court.objects.values(courtId = F('CourtID') ,courtName = F('Name'),courtType = F('CourtType'),courtCategory = F('SportCategory__SportCategory'),hourlyRate = F('HourlyRate'),isActive = F('IsActive')).get(CourtID = court)
            data['courtImage'] = ["http://127.0.0.1:8000/media/" + x['Image'] for x in  court_img.values('Image')]
            return data , 200
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500   

    def update_court_data(self): 
        try:
            court_id = self.data['courtId']
            court_name = self.data['courtName']
            court_category = self.data['courtCategoryId']
            hourly_rate = self.data['hourlyRate']
            capacity = self.data['capacity']
            surface_type = self.data['surfaceType']
            desc = self.data['desc']
            is_active = self.data['isActive']

            court = smd.Court.objects.get(CourtID = court_id)

            court.Name = court_name
            court.Description = desc
            court.SurfaceType = surface_type
            court.Capacity = capacity
            court.HourlyRate = hourly_rate
            court.IsActive = is_active
            court.SportCategory = md.SportCategory.objects.get(SportCategoryID = court_category)
            court.save()
            return message('Court Updated Successfully'), 200
        
        except smd.Court.DoesNotExist:
            return message('Court Not Found'), 404
        except md.SportCategory.DoesNotExist:
            return message('Sport Category Not Found'), 404
        except KeyError as k:
            return message(f'{k} is Missing'), 400 
        except Exception as e:
            print(e)
            return message('Something Went Wrong'), 500   

    def get_venue_payment_method_data(self):
        try:
            final_data = []
            venue = smd.Venue.objects.all()
            for v in venue:
                try:
                    venue_payment_secret_data = smd.OnlinePaymentKhaltiSecretKey.objects.get(Venue__VenueID = v.VenueID)
                    if venue_payment_secret_data.PrivateSecretKey is not None:
                        final_data.append({'venueId': str(v.VenueID),'venueName': v.Name,'status': True})
                except Exception as e:
                    final_data.append({'venueId': str(v.VenueID),'venueName': v.Name,'status': False})
            return final_data, 200        
        except Exception as e:
            print(e)
            return message('Something Went Wrong'), 500          






