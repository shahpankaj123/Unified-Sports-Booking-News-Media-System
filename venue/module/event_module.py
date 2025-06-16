from mainapp.selectors.common_functions import message
from mainapp.selectors import selector as sc
from venue import models as vmd

from django.db.models import F

class EventModule:

    def __init__(self ,data):
        self.data = data

    def create_events(self):
        try:
            court_id = self.data['courtId'] 
            max_seat = self.data['maxSeat']
            date = self.data['date']
            time = self.data['time']
            title = self.data['title']

            court = sc.get_court_from_id(court_id=court_id)

            vmd.Event.objects.create(Court = court,MaximunSeat = max_seat , Date = date ,Time = time,EventTitle = title)
            return message('Event Created Successfully') ,201

        except KeyError as k:
            return message(f'{k} is Missing') ,404  
        except Exception as e:
            return message('Internal Server Error') ,500  

    def get_all_event(self):
        try:
            court_id = self.data['courtId'] 
            return vmd.Event.objects.filter(Court__CourtID = court_id).values(eventId = F('EventId') ,maxSeat =F('MaximunSeat'),date =F('Date') ,time =F('Time'),title = F('EventTitle')).order_by('-CreatedAt') ,200
        except KeyError as k:
            return message(f'{k} is Missing') ,404  
        except Exception as e:
            return message('Internal Server Error') ,500    

    def get_event_by_id(self):
        try:
            event_id = self.data['eventId'] 
            return vmd.Event.objects.values(eventId = F('EventId') ,maxSeat =F('MaximunSeat'),date =F('Date') ,time =F('Time'),title = F('EventTitle')).get(EventId = event_id) ,200
        except KeyError as k:
            return message(f'{k} is Missing') ,404  
        except Exception as e:
            return message('Internal Server Error') ,500  

    def update_event(self):
        try:
            event_id = self.data['eventId']
            max_seat = self.data['maxSeat']
            date = self.data['date']
            time = self.data['time'] 
            title = self.data['title']

            event = vmd.Event.objects.get(EventId = event_id)
            event.MaximunSeat = max_seat
            event.Date = date
            event.Time = time
            event.EventTitle = title
            event.save()
            return message('Event Updated Successfully') ,200

        except KeyError as k:
            return message(f'{k} is Missing') ,404  
        except Exception as e:
            return message('Internal Server Error') ,500  

    def del_event(self):
        try:
            event_id = self.data['eventId']
            vmd.Event.objects.get(EventId = event_id).delete()
            return message('Event Deleted Successfully') ,200
        except KeyError as k:
            return message(f'{k} is Missing') ,404  
        except Exception as e:
            return message('Internal Server Error') ,500 

    def get_all_user_by_event(self):
        try:
            event_id = self.data['eventId']
            return vmd.EventRegisteredRecord.objects.filter(Event__EventId = event_id).values(firstName = F('User__FirstName') ,lastName =F('User__LastName'),email = F('User__Email')).order_by('-CreatedAt') ,200
        except KeyError as k:
            return message(f'{k} is Missing') ,404  
        except Exception as e:
            return message('Internal Server Error') ,500 



