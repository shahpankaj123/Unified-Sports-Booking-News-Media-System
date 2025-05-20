from mainapp import models as md

from venue import models as smd

from mainapp.selectors.common_functions import message

from django.db.models import F


class VenueApplicationModule:

    def __init__(self ,data):
        self.data = data

    def get_all_venue_application(self):

        try:
            return smd.VenueApplication.objects.all().values() ,200

        except Exception as e:
            print(e)
            return message('Somethign Went Wrong'),500
