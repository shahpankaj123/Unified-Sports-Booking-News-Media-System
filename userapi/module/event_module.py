from venue import models as vmd
from mainapp import models as md
from django.db.models import Sum

from mainapp.selectors.common_functions import message

from django.db.models import F,Value,CharField
from django.db.models.functions import Concat

import random

class EventModule:

    def __init__(self ,data):
        self.data = data

    def registered_event(self):
        try:
            user_id = self.data['userId']
            event_id = self.data['eventId']

            event = vmd.Event.objects.get(EventId = event_id)
            user = md.Users.objects.get(UserID = user_id)
            token = random.randint(1,10000)

            if vmd.EventRegisteredRecord.objects.filter(Event__EventId = event_id).count() >= event.MaximunSeat:
                return message('Seat are Packed !sorry') ,400

            vmd.EventRegisteredRecord.objects.create(Event= event,User = user ,Token = token)
            return message('Event Created Successfully') ,201
        except KeyError as k:
            return message(f'{k} is Missing') ,400
        except Exception as e:
            print(e)  
            return message('Something Went Wrong') ,500  
        
    def get_registered_details(self):
        try:
            user_id = self.data['userId']
            return vmd.EventRegisteredRecord.objects.filter(User__UserID = user_id).values(coutName = F('Event__Court__Name'),eventName = F('Event__EventTitle'),date = F('Event__Date'),time = F('Event__Time'),token = F('Token')) ,200
        except KeyError as k:
            return message(f'{k} is Missing') ,400
        except Exception as e:
            print(e)  
            return message('Something Went Wrong') ,500 
