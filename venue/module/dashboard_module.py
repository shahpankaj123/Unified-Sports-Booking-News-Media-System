
from mainapp.selectors.common_functions import message
from venue import models as vmd

from django.db.models import Sum

class DashboardModule:

    def __init__(self,data , request):
        self.data = data
        self.request = request

    def get_dashboard_data(self):
        try:
            data = {}
            data['total_books'] = vmd.Booking.objects.filter(Availability__Court__Venue__Owner__Email = self.request.user ,Status__Status = 'Success').count()
            data['rejected_books'] = vmd.Booking.objects.filter(Availability__Court__Venue__Owner__Email = self.request.user ,Status__Status = 'Rejected').count()
            data['pending_books'] = vmd.Booking.objects.filter(Availability__Court__Venue__Owner__Email = self.request.user ,Status__Status = 'Pending').count()
            data['total_courts'] = vmd.Court.objects.filter(Venue__Owner__Email = self.request.user).count()
            data['total_earnings'] = vmd.Booking.objects.filter(Availability__Court__Venue__Owner__Email = self.request.user ,Status__Status = 'Success').aggregate(Sum('TotalPrice'))['TotalPrice__sum']

            return data , 200
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500 