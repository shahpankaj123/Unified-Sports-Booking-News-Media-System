
from venue import models as vmd
from mainapp.selectors import selector as sc
from mainapp.selectors.common_functions import message

from django.db import transaction

import requests
import json

class KhaltiPaymentModule:

    def __init__(self ,data):
        self.data = data
        self.ticket_id = self.data['ticketId']
        self.ticket = vmd.Availability.objects.get(ID = self.ticket_id[0])
        self.khalti_secret_key = sc.get_secret_key(venue_id= self.ticket.Court.Venue.VenueID)
        self.headers = {'Authorization': f'key {self.khalti_secret_key}','Content-Type': 'application/json'}


    def booking_ticket(self):
        try:
            user_id = self.data['userId']
            payment_method = self.data['paymentTypeId']
            total_price = self.data['totalPrice']

            self.usr = sc.get_user_from_id(user_id=user_id)
            self.status = sc.get_status_from_name(status='Pending')
            self.pay_method = sc.get_payment_method_from_id(payment_method_id = payment_method)

            if self.ticket.IsActive == 0:
                return message('Ticket Already Booked') ,400

            with transaction.atomic():
                self.ticket.IsActive = 0
                self.ticket.save()
                book = vmd.Booking.objects.create(User = self.usr ,Availability = self.ticket , Status = self.status ,PaymentMethod = self.pay_method ,TotalPrice = total_price)
                payment =vmd.PaymentTransaction.objects.create(Amount = total_price ,PaymentStatus = self.status ,PaymentMethod = self.pay_method)
                payment.Bookings.set([book])

            if self.pay_method.PaymentTypeName == 'Online':
                url = "https://dev.khalti.com/api/v2/epayment/initiate/"

                payload = json.dumps({
                        "return_url": "http://127.0.0.1:3000",
                        "website_url": "http://127.0.0.1:3000",
                        "amount": book.TotalPrice,
                        "purchase_order_id": str(book.BookingID),
                        "purchase_order_name": self.ticket.Court.Name + ' ' + str(self.ticket.StartTime) + ' - ' + str(self.ticket.EndTime)+ 'Slot',
                        "customer_info": {
                        "name": self.usr.FirstName + ' ' + self.usr.LastName,
                        "email": self.usr.Email,
                        "phone": self.usr.PhoneNumber
                        }
                    })
                response = requests.request("POST", url, headers= self.headers, data=payload)
                
                print(response)

                return response.json(), 200 

            return { 
                'bookId' : str(book.BookingID),
                'price' : book.TotalPrice,
                'status' : True,
                'paymentStatus' : 'Pending'
            } ,200
        
        except KeyError as k:
            return message(f'{k} is Missing') ,400
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500       

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
        try:
            pass

        except Exception as e:
            print(e)    



