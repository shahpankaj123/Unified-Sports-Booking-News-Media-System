
from mainapp.selectors.common_functions import message
from venue import models as vmd
from adds import models as amd
from django.db.models import Sum ,F

from django.db.models import Count

class DashboardModule:

    def __init__(self,data , request):
        self.data = data
        self.request = request

    def get_dashboard_data(self):
        try:
            user_id = self.data['userId']
            data = {}
            data['total_books'] = vmd.Booking.objects.filter(Availability__Court__Venue__Owner__UserID = user_id ,Status__Status = 'Success').count()
            data['rejected_books'] = vmd.Booking.objects.filter(Availability__Court__Venue__Owner__UserID = user_id ,Status__Status = 'Rejected').count()
            data['pending_books'] = vmd.Booking.objects.filter(Availability__Court__Venue__Owner__UserID = user_id ,Status__Status = 'Pending').count()
            data['total_courts'] = vmd.Court.objects.filter(Venue__Owner__UserID = user_id).count()
            data['total_earnings'] = vmd.PaymentTransaction.objects.filter(Bookings__Availability__Court__Venue__Owner__UserID = user_id ,PaymentStatus__Status = 'Success').aggregate(price = Sum('Amount'))['price']

            data['post_statics']=amd.Post.objects.values(category = F('Category__SportCategory')).annotate(post_count=Count('PostID'))
            data['reel_statics']=amd.Reel.objects.values(category = F('Category__SportCategory')).annotate(post_count=Count('ReelID'))

            return data , 200
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500 