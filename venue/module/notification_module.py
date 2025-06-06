from mainapp import models as md

from django.utils import timezone
from datetime import timedelta

class NotificationModule:
    def __init__(self , data ,request):
        self.data = data
        self.request = request

    def get_all_notification(self):
        try:
            today = timezone.now().date()
            three_days_ago = today - timedelta(days=3)

            queryset = md.Notification.objects.filter(
                User=self.request.user,
                Date__range=(three_days_ago, today)
            ).values()

            data = list(queryset) 
            response = {
                'count': len(data),
                'notifications': data
            }
            return response, 200

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500    