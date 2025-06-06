from mainapp.selectors.common_functions import message
from mainapp.selectors import selector as sc

from venue import models as vmd
from mainapp import models as md

from threading import Thread

from django.db.models import F,Q
from datetime import datetime

class BookingModule:

    def __init__(self ,data):
        self.data = data

    def get_all_booking(self):
        try:
            court_id = self.data['courtId']
            start_date = self.data['startDate']
            end_date = self.data['endDate']
            return vmd.Booking.objects.filter(Availability__Court__CourtID = court_id , Availability__Date__range =(start_date,end_date)).values() ,200
        except Exception as e:
            print(e)  

    def get_booking_by_id(self):
        try:
            booking_id = self.data['bookingId']
            return vmd.Booking.objects.values().get(BookingID = booking_id) ,200
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500

    def update_booking_details(self):
        try:
            status_id = self.data['statusId']
            booking_id = self.data['bookingId']

            booking = vmd.Booking.objects.get(BookingID = booking_id)
            status = sc.get_status_from_id(status_id= status_id)
            booking.Status = status
            booking.save()
            md.Notification.objects.create(User =  booking.User , message = f"Your Booking for Ticket {booking.Availability.StartTime} to {booking.Availability.EndTime} on {booking.Availability.Date} Status Changed to {status.Status}",Date = datetime.now().date())
            return message('Booking Status Updated Successfully') ,200
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500                  
            