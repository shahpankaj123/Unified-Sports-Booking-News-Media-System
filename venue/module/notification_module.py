from mainapp import models as md

from django.utils import timezone
from datetime import timedelta

from mainapp.selectors.common_functions import message

class NotificationModule:
    def __init__(self , data ,request):
        self.data = data
        self.request = request

    def get_all_notification(self):
        try:
            user_id = self.data['userId']
            queryset = md.Notification.objects.filter(User__UserID = user_id).values().order_by('-CreatedAt')
            count = md.Notification.objects.filter(User__UserID = user_id ,IsRead = False).count()
            response = {
                'count': count,
                'notifications': queryset
            }
            return response, 200

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500  

    def get_notification_by_id(self):
        try:
            notification_id = self.data['notificationId'] 
            query  = md.Notification.objects.get(NotificationID = notification_id)
            query.IsRead = True
            query.save()
            return md.Notification.objects.values().get(NotificationID = notification_id) ,200
        
        except md.Notification.DoesNotExist:
            return message('Data Not Found') ,400
        except KeyError as k:
            return message(f'{k} is Missing'),404
            