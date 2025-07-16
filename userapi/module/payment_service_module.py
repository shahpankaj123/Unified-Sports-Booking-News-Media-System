
from venue import models as vmd
from mainapp import models as md
from mainapp.selectors import selector as sc
from mainapp.selectors.common_functions import message

from django.db import transaction
from datetime import datetime

import requests
import json

class KhaltiPaymentModule:

    def __init__(self ,data):
        self.data = data
        court_id = self.data['courtId']
        self.khalti_secret_key = sc.get_secret_key(court_id = court_id)
        self.headers = {'Authorization': f'Key {self.khalti_secret_key}','Content-Type': 'application/json'}

    def booking_ticket(self):
        try:
            user_id = self.data['userId']
            payment_method = self.data['paymentTypeId']
            total_price = self.data['totalPrice']
            self.ticket_id = self.data['ticketId']

            self.usr = sc.get_user_from_id(user_id=user_id)
            self.status = sc.get_status_from_name(status='Pending')
            self.pay_method = sc.get_payment_method_from_id(payment_method_id = payment_method)

            if vmd.Availability.objects.filter(ID__in = self.ticket_id ,IsActive = 0).exists():
                return message('Ticket Already Booked') ,400
            
            book_list = []

            for t in self.ticket_id:
                with transaction.atomic():
                    self.ticket_data = vmd.Availability.objects.get(ID = t)
                    book = vmd.Booking.objects.create(User = self.usr ,Availability = self.ticket_data , Status = self.status ,PaymentMethod = self.pay_method ,TotalPrice = self.ticket_data.SpecialRate)   
                    book_list.append(book)   
                
            with transaction.atomic():
                payment =vmd.PaymentTransaction.objects.create(Amount = total_price ,PaymentStatus = self.status ,PaymentMethod = self.pay_method)
                payment.Bookings.set(book_list)

            if self.pay_method.PaymentTypeName == 'Online':
                url = "https://dev.khalti.com/api/v2/epayment/initiate/"

                payload = json.dumps({
                        "return_url": f"http://localhost:3000/payment/success?courtId={payment.Bookings.first().Availability.Court.CourtID}",
                        "website_url": "http://localhost:3000",
                        "amount": float(payment.Amount) * 100.0,
                        "purchase_order_id": str(payment.PaymentTransactionID),
                        "purchase_order_name": self.ticket_data.Court.Name + ' - ' + 'Slot',
                        "customer_info": {
                        "name": self.usr.FirstName + ' ' + self.usr.LastName,
                        "email": self.usr.Email,
                        "phone": self.usr.PhoneNumber
                        },
                    })
                
                print(payload)
                
                response = requests.request("POST", url, headers= self.headers, data=payload)
                
                print(response)

                return response.json(), 200 

            return { 
                'bookId' : str(payment.PaymentTransactionID),
                'price' : payment.Amount,
                'status' : True,
                'paymentStatus' : 'Pending'
            } ,200
        
        except KeyError as k:
            return message(f'{k} is Missing') ,400
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500       

    def verify_khalti_payment(self ,pidx):
        try:
            url = "https://dev.khalti.com/api/v2/epayment/lookup/"
            payload = json.dumps({"pidx": pidx})
            response = requests.post(url, data=payload ,headers=self.headers)
            print(response)
            return response.json()
        except Exception as e:
            print(e)

    def verify_payment(self):
        try:
            pidx = self.data['pidx']
            purchase_order_id = self.data['purchaseOrderId']
            user_id = self.data['userId']
            res = self.verify_khalti_payment(pidx=pidx)
            usr = sc.get_user_from_id(user_id = user_id)

            payment =vmd.PaymentTransaction.objects.get(PaymentTransactionID = purchase_order_id)

            ticket_list = [x.Availability.ID for x in payment.Bookings.all()]

            if vmd.Availability.objects.filter(ID__in = ticket_list ,IsActive = 0).exists():
                res['status'] = 'Rejected'

            if res['status'] == 'Completed':
                with transaction.atomic():
                    self.status = sc.get_status_from_name(status='Success')
                    payment.PaymentStatus = self.status

                    for booking in payment.Bookings.all():
                        booking.Availability.IsActive = 0
                        booking.Availability.save()

                        booking.Status = self.status
                        booking.save()

                    payment.save()
                    md.Notification.objects.create(Message = f'{payment.Bookings.first().Availability.Court.Name} Ticket has Been Booked Successfully',User = usr , Date = datetime.now().date())

                return message('Payment Verified Success') ,200    

            else:
                with transaction.atomic():
                    self.status = sc.get_status_from_name(status='Rejected')
                    payment.PaymentStatus = self.status

                    for booking in payment.Bookings.all():
                        booking.Status = self.status
                        booking.save()

                    payment.save()
                    md.Notification.objects.create(Message = f'{payment.Bookings.first().Availability.Court.Name} Ticket has Been Rejected',User = usr , Date = datetime.now().date())

                return message('Payment Verified Failed') ,400
            
        except vmd.PaymentTransaction.DoesNotExist:
            return message('Data Not Found') ,400  
        except KeyError as k:
            return message(f'{k} is Missing') ,400
        except Exception as e:
            print(e)  
            return message('Something Went Wrong') ,500  
        
    def get_user_booking_details(self):
        try:
            user_id = self.data['userId']
            return vmd.Booking.objects.filter(User__UserID = user_id).values().order_by('-UpdatedAt') ,200
        except KeyError as k:
            return message(f'{k} is Missing') ,400
        except Exception as e:
            print(e)  
            return message('Something Went Wrong') ,500     





