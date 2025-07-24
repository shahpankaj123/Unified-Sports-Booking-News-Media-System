from venue import models as smd
from django.db.models import F

from mainapp.selectors.common_functions import message

from django.core.cache import cache

class VenueModule:

    def __init__(self ,data):
        self.data = data

    def get_all_venue(self):
        if cache.get('venue_all'):
            print("cached data")
            return cache.get('venue_all') ,200
        final_data = []
        venue = smd.Venue.objects.filter(IsActive = True).select_related('Owner', 'City').prefetch_related('venue_images','venue__courts_images')  
        for d in venue:
            venue_data = {
                "venueID": str(d.VenueID),
                "name": d.Name,
                "address": d.Address,
                "city": d.City.CityName if d.City else None,
                "latitude": float(d.Latitude) if d.Latitude else None,
                "longitude": float(d.Longitude) if d.Longitude else None,
                "phoneNumber": d.PhoneNumber,
                "email": d.Email,
                "description": d.Description,
                "openingTime": d.OpeningTime.strftime("%H:%M:%S") if d.OpeningTime else None,
                "closingTime": d.ClosingTime.strftime("%H:%M:%S") if d.ClosingTime else None,
                "isActive": d.IsActive,
                "createdAt": d.CreatedAt.strftime("%Y-%m-%d %H:%M:%S"),
                "owner": {
                    "firstName": d.Owner.FirstName if d.Owner else None,
                    "lastName": d.Owner.LastName if d.Owner else None,
                    "email": d.Owner.Email if d.Owner else None,
                },
                "venueImages": [
                    {
                        "imageID": str(img.ImageID),
                        "image": "http://127.0.0.1:8000/media/" + str(img.Image) if img.Image else None,
                    }
                    for img in d.venue_images.all()
                ]
            }  
            final_data.append(venue_data)  
        cache.set('venue_all' , final_data ,30)  
        return final_data ,200
    
    def get_all_courts(self):
        if cache.get('courts_all'):
            print("cached data")
            return cache.get('courts_all') ,200
        final_data = []
        court = smd.Court.objects.filter(Venue__IsActive = True,IsActive= True)
        for c in court:
            court_data = {
                    "courtID": str(c.CourtID),
                    "name": c.Name,
                    "sportCategory": c.SportCategory.SportCategory if c.SportCategory else None,
                    "surfaceType": c.SurfaceType,
                    "capacity": c.Capacity,
                    "hourlyRate": float(c.HourlyRate),
                    "isActive": c.IsActive,
                    "createdAt": c.CreatedAt.strftime("%Y-%m-%d %H:%M:%S"),
                    "courtImages": [
                        {
                            "imageID": str(img.ImageID),
                            "image": "http://127.0.0.1:8000/media/" + str(img.Image) if img.Image else None,
                        }
                        for img in c.courts_images.all()
                    ]
                }
            final_data.append(court_data)
        cache.set('courts_all' , final_data ,30)  
        return final_data ,200 

    def get_venue_details(self):
        try: 
            try:
                venue_id = self.data['venueId']
            except KeyError as k:
                return message(f'{k} is Missing') ,404 
            
            if cache.get(f'venue_{venue_id}'):
                print("cached data")
                return cache.get(f'venue_{venue_id}') ,200 
            
            try:
                venue = smd.Venue.objects.select_related('Owner', 'City').prefetch_related(
                    'venue_images',
                    'venue__courts_images'  # courts_images from Court
                ).get(VenueID=venue_id)
            except smd.Venue.DoesNotExist:
                return message('Venue Not Found') ,200   

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
                        "image": "http://127.0.0.1:8000/media/" + str(img.Image) if img.Image else None,
                        "createdAt": img.CreatedAt.strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    for img in venue.venue_images.all()
                ],
                "courts": []
            }

            for court in venue.venue.all():
                if court.IsActive:  
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
                                "image": "http://127.0.0.1:8000/media/" + str(img.Image) if img.Image else None,
                                "createdAt": img.CreatedAt.strftime("%Y-%m-%d %H:%M:%S"),
                            }
                            for img in court.courts_images.all()
                        ]
                    }
                    venue_data["courts"].append(court_data)
            cache.set(f'venue_{venue_id}',venue_data,timeout=30)
            return venue_data ,200

        except smd.Venue.DoesNotExist:
            return message('Venue Not Found') ,400  

    def court_details(self):
        try:
            court_id = self.data['courtId']
        except KeyError as k:
            return message(f'{k} is Missing') ,404  

        if cache.get(f'cout_{court_id}'):
            print('cached court data fectch')
            return cache.get(f'cout_{court_id}') ,200
        
        try:
            court = smd.Court.objects.get(CourtID = court_id ,IsActive = 1) 
        except smd.Court.DoesNotExist:
            return message('Court Not Found') ,200    

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
                            "image": "http://127.0.0.1:8000/media/" + str(img.Image) if img.Image else None,
                        }
                        for img in court.courts_images.all()
                    ]
                }
        cache.set(f'cout_{court_id}',court_data,timeout=30)
        return court_data ,200    