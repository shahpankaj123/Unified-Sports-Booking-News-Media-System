from venue import models as vmd
from django.db.models import Sum

from mainapp.selectors.common_functions import message

from django.db.models import F,Value,CharField
from django.db.models.functions import Concat

class DashBoarModule:

    def __init__(self ,data):
        self.data = data

    def get_user_booking_details(self):
        try:
            user_id = self.data['userId']
            return vmd.Booking.objects.filter(User__UserID = user_id).values(bookingId = F('BookingID') ,userName = Concat(F('User__FirstName'),Value(' '),F('User__LastName')), ticket = Concat(F('Availability__StartTime'),Value(' - '),F('Availability__EndTime'),output_field=CharField()),status=F('Status__Status'),paymentMethod = F('PaymentMethod__PaymentTypeName'),price =F('TotalPrice')).order_by('-UpdatedAt') ,200
        except KeyError as k:
            return message(f'{k} is Missing') ,400
        except Exception as e:
            print(e)  
            return message('Something Went Wrong') ,500      

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
        