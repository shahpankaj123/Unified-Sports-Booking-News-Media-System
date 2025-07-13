
from venue import models as vmd
from mainapp.selectors import selector as sc
from mainapp.selectors.common_functions import message

from django.db import transaction

import requests

class KhaltiPaymentModule:

    def __init__(self ,data):
        self.data = data
        self.khalti_secret_key = sc.get_secret_key(venue_id=self.data['venueId'])
        self.headers = { "Authorization": f"Key {self.khalti_secret_key}"}

    def booking_ticket(self):
        try:
            user_id = self.data['userId']
            ticket_id = self.data['ticketId']
            payment_method = self.data['paymentTypeId']
            total_price = self.data['totalPrice']

            self.usr = sc.get_user_from_id(user_id=user_id)
            self.ticket = vmd.Availability.objects.get(ID = ticket_id)
            self.status = sc.get_status_from_name(status='Pending')
            self.pay_method = sc.get_payment_method_from_id(payment_method_id = payment_method)

            if self.ticket.IsActive == 0:
                return message('Ticket Already Booked') ,400

            with transaction.atomic():
                self.ticket.IsActive = 0
                self.ticket.save()
                book = vmd.Booking.objects.create(User = self.usr ,Availability = self.ticket , Status = self.status ,PaymentMethod = self.pay_method ,TotalPrice = total_price)
                vmd.PaymentTransaction.objects.create(Bookings = book ,Amount = total_price ,PaymentStatus = self.status ,PaymentMethod = self.pay_method)

            return { 
                'bookId' : str(book.BookingID),
                'price' : book.TotalPrice
            } ,200

        except Exception as e:
            print(e)
            pass        

    def verify_khalti_payment(self ,token, amount):
        try:
            url = "https://khalti.com/api/v2/payment/verify/"
            payload = {"token": token,"amount": amount}
            response = requests.post(url, data=payload, headers=self.headers)
            print(response)
            return response
        except Exception as e:
            print(e)

    def verify_payment(self):
        pass



