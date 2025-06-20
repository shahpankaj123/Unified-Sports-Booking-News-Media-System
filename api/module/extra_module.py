from venue import models as md
from mainapp import models as d

from django.core.cache import cache

class ExtraModule:

    def __init__(self ,data):
        self.data = data

    def get_count_data(self):
        try:
            if cache.get('extra'):
                return cache.get('extra') ,200
            
            normal_user_count = d.Users.objects.filter(UserType__UserType = 'NormalUsers').count()
            booking_count = md.Booking.objects.all().count()
            venue_count = md.Venue.objects.all().count()
            court_count = md.Court.objects.all().count()
            avg_rating = 4.5

            data = {
                'normal_user_count':normal_user_count,
                'booking_count':booking_count,
                'venue_count':venue_count,
                'court_count':court_count,
                'avg_rating': avg_rating
            } 
            cache.set('extra' , data , timeout=60)
            return data ,200
        
        except Exception as e:
            print(e)  
            return {} ,200      