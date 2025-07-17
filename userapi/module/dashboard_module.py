from venue import models as vmd
from django.db.models import Sum

from mainapp.selectors.common_functions import message

class DashBoarModule:

    def __init__(self ,data):
        self.data = data

    def get_data(self):
        try:
            user_id = self.data['userId']
            
            booking_count =   vmd.Booking.objects.filter(User__UserID = user_id).count()
            booking_pending_count = vmd.Booking.objects.filter(User__UserID = user_id ,Status__Status = 'Pending').count()
            booking_reject_count = vmd.Booking.objects.filter(User__UserID = user_id ,Status__Status = 'Rejected').count()
            booking_success_count = vmd.Booking.objects.filter(User__UserID = user_id ,Status__Status = 'Success').count()
            total_revenue = vmd.Booking.objects.filter(User__UserID=user_id,Status__Status='Success').aggregate(total=Sum('TotalPrice'))['total'] or 0

            return {
                'booking_count':booking_count,
                'booking_pending_count':booking_pending_count,
                'booking_reject_count':booking_reject_count,
                'booking_success_count':booking_success_count,
                'total_revenue':total_revenue,
            } ,200
        
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500
        