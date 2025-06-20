from mainapp.selectors.common_functions import message
from mainapp.selectors import selector as sc
from venue import models as vmd

from django.db.models import F,Value,CharField
from django.db.models.functions import Concat

from django.core.cache import cache

class EventModule:

    def __init__(self ,data):
        self.data = data

    def create_events(self ,request):
        try:
            court_id = self.data['courtId'] 
            max_seat = self.data['maxSeat']
            date = self.data['date']
            time = self.data['time']
            title = self.data['title']
            image = request.FILES['image']

            court = sc.get_court_from_id(court_id=court_id)

            vmd.Event.objects.create(Court = court,MaximunSeat = max_seat , Date = date ,Time = time,EventTitle = title , Image = image)
            return message('Event Created Successfully') ,201

        except KeyError as k:
            return message(f'{k} is Missing') ,404  
        except Exception as e:
            print(e)
            return message('Internal Server Error') ,500  

    def get_all_event(self):
        try:
            court_id = self.data['courtId'] 
            return vmd.Event.objects.filter(Court__CourtID = court_id).values(image =Concat(Value('http://127.0.0.1:8000/media/'),F('Image'),output_field=CharField()),eventId = F('EventId') ,maxSeat =F('MaximunSeat'),date =F('Date') ,time =F('Time'),title = F('EventTitle')).order_by('-created_at') ,200
        except KeyError as k:
            return message(f'{k} is Missing') ,404  
        except Exception as e:
            print(e)
            return message('Internal Server Error') ,500    

    def get_event_by_id(self):
        try:
            event_id = self.data['eventId'] 
            if cache.get(f'event_{event_id}'):
                return cache.get(f'event_{event_id}') ,200
            data = vmd.Event.objects.values(image =Concat(Value('http://127.0.0.1:8000/media/'),F('Image'),output_field=CharField()),eventId = F('EventId') ,maxSeat =F('MaximunSeat'),date =F('Date') ,time =F('Time'),title = F('EventTitle')).get(EventId = event_id)
            cache.set(f'event_{event_id}' ,data ,timeout=60)
            return data ,200
        except KeyError as k:
            return message(f'{k} is Missing') ,404  
        except vmd.Event.DoesNotExist:
            return message('Data Not Found') ,400
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
        except vmd.Event.DoesNotExist:
            return message('Data Not Found') ,400
        except KeyError as k:
            return message(f'{k} is Missing') ,404  
        except Exception as e:
            return message('Internal Server Error') ,500  

    def del_event(self):
        try:
            event_id = self.data['eventId']
            vmd.Event.objects.get(EventId = event_id).delete()
            return message('Event Deleted Successfully') ,200
        except vmd.Event.DoesNotExist:
            return message('Data Not Found') ,400
        except KeyError as k:
            return message(f'{k} is Missing') ,404  
        except Exception as e:
            return message('Internal Server Error') ,500 

    def get_all_user_by_event(self):
        try:
            event_id = self.data['eventId']
            if cache.get(f'event_user_{event_id}'):
                return cache.get(f'event_user_{event_id}') ,200
            data = vmd.EventRegisteredRecord.objects.filter(Event__EventId = event_id).values(firstName = F('User__FirstName') ,lastName =F('User__LastName'),email = F('User__Email')).order_by('-created_at')
            cache.set(f'event_user_{event_id}' ,data ,timeout=60)
            return data ,200
        except KeyError as k:
            return message(f'{k} is Missing') ,404  
        except Exception as e:
            print(e)
            return message('Internal Server Error') ,500 
        
    def all_events(self):
        if cache.get('events'):
            return cache.get('events') ,200
        else:
            data =  vmd.Event.objects.all().values(image =Concat(Value('http://127.0.0.1:8000/media/'),F('Image'),output_field=CharField()),eventId = F('EventId') ,maxSeat =F('MaximunSeat'),date =F('Date') ,time =F('Time'),title = F('EventTitle')).order_by('-created_at') 
            cache.set('events' ,data , timeout=60)
            return data ,200




