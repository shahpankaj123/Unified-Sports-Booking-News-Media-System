from mainapp.selectors.common_functions import message
from venue import models as vmd

from threading import Thread

from django.db.models import F,Q

class TicketModule:

    def __init__(self ,data):
        self.data = data

    def create_ticket(self):
        try:
            court_id = self.data['courtId']
            date = self.data['date']
            ticket_list = self.data['ticketList']
            court = vmd.Court.objects.get(CourtID = court_id)

            if vmd.Availability.objects.filter(Court__CourtID = court_id ,Date = date).exists():
                return message('Ticket Already Issued for Given Date') ,400
            
            thread = Thread(target=self.__create_ticket , args=(ticket_list ,court ,date))
            thread.start()
            return message('Ticket Created Successfully') ,201
        except KeyError as k:
            return message(f'{k} is Missing') ,404
        except vmd.Court.DoesNotExist:
            return message('Court Not Found') ,400
        except Exception as e:
            print(e)
            return message('Somthing Went Wrong') ,500   

    def __create_ticket(self ,ticket_list ,court ,date):
        try:
            for ticket in ticket_list:
                special_price = ticket['specialPrice'] if ticket['specialPrice'] is not None else court.HourlyRate
                vmd.Availability.objects.create(Court = court ,Date = date ,StartTime = ticket['startTime'] ,EndTime =ticket['endTime'] , SpecialRate = special_price)

        except Exception as e:
            print(e)
            pass  

    def get_all_ticket(self):
        try:
            date = self.data['date']
            court_id = self.data['courtId']

            return vmd.Availability.objects.filter(Court__CourtID = court_id ,Date = date).values(id = F('ID') ,date = F('Date') ,startTime = F('StartTime') ,endTime = F('EndTime') ,isActive = F('IsActive') ,rate =F('SpecialRate')).order_by('-CreatedAt') ,200
        
        except Exception as e:
            print(e)
            return message('Somthing Went Wrong') ,500 
        
    def get_ticket_by_id(self):
        try:
            id = self.data['ticketId']
            return vmd.Availability.objects.values(id = F('ID') ,date = F('Date') ,startTime = F('StartTime') ,endTime = F('EndTime') ,isActive = F('IsActive') ,rate =F('SpecialRate')).get(ID = id) ,200
        except Exception as e:
            print(e)
            return message('Somthing Went Wrong') ,500 
        
    def update_ticket(self):
        try:
            id = self.data['ticketId']
            court_id = self.data['courtId']
            start_time = self.data['startTime']
            end_time = self.data['endTime']
            date = self.data['date']
            rate = self.data['rate']
            is_active = self.data['isActive']

            if vmd.Availability.objects.filter(Court__CourtID = court_id ,Date = date ,IsActive = True).exclude(ID = id).filter(Q(StartTime__lt=end_time) & Q(EndTime__gt=start_time)).exists():
                return message('Time slot overlaps with existing availability'), 400

            ticket = vmd.Availability.objects.get(ID = id)

            ticket.StartTime = start_time
            ticket.EndTime = end_time
            ticket.Date = date
            ticket.SpecialRate = rate
            ticket.IsActive = is_active
            ticket.save()
            return message('Update Data Successfully') ,200
        
        except vmd.Availability.DoesNotExist:
            return message('Ticket Not Found') ,400
        except Exception as e:
            print(e)
            return message('Somthing Went Wrong') ,500     



        

