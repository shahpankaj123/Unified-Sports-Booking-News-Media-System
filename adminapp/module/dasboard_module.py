
from mainapp import models as md

from venue import models as smd
from adds import models as amd

from django.db.models import Sum

from mainapp.selectors.common_functions import message

class DashboardModule:

    def __init__(self ,data):
        self.data = data

    def get_count_data(self):
        try:
            normal_user_count = md.Users.objects.filter(UserType__UserType = 'NormalUsers').count()
            venue_user_count = md.Users.objects.filter(UserType__UserType = 'VenueUsers').count()
            admin_user_count = md.Users.objects.filter(UserType__UserType = 'Admin').count()

            venue_count = smd.Venue.objects.all().count()
            court_count = smd.Court.objects.all().count()

            venue_application_count = smd.VenueApplication.objects.all().count()
            news_count = amd.Post.objects.all().count()
            booking_count = smd.Booking.objects.filter(Status__Status = 'Success').count()
            reels_count = 0

            total_income =  smd.PaymentTransaction.objects.filter(PaymentStatus__Status = 'Success').aggregate(total = Sum('Amount'))['total']

            data = {
                'normal_user_count':normal_user_count,
                'venue_user_count':venue_user_count,
                'admin_user_count':admin_user_count,
                'venue_count':venue_count,
                'court_count':court_count,
                'venue_application_count':venue_application_count,
                'news_count': news_count,
                'reels_count': reels_count,
                'booking_count':booking_count,
                'total_income':total_income
            }

            return data ,200

        except Exception as e:
            print(e) 
            return message('Something went Wrong') ,500   
