from mainapp.selectors.common_functions import message
from mainapp.selectors import selector as sc

from venue import models as vmd
from mainapp import models as md

from threading import Thread

from django.db.models import F,Q,Value,CharField
from django.db.models.functions import Concat

from datetime import datetime

class BookingModule:

    def __init__(self ,data):
        self.data = data

    def get_all_booking(self):
        try:
            date = self.data['date']
            return vmd.Booking.objects.filter(CreatedAt__date = date).values(coutName = F('Availability__Court__Name'),venueName = F('Availability__Court__Venue__Name'),bookingId = F('BookingID'),BookerName = Concat(F('User__FirstName'),Value(' ') ,F('User__LastName')),status = F('Status__Status'),paymentMethod = F('PaymentMethod__PaymentTypeName'),totalPrice = F('TotalPrice'),bookDate = F('Availability__Date'),timeSlot =Concat(F('Availability__StartTime'),Value(' - '),F('Availability__EndTime'),output_field=CharField()),) ,200
        except KeyError as k:
            return message(f'{k} is Missing') ,404
        except Exception as e:
            print(e)  
            return message('Something Went Wrong') ,500