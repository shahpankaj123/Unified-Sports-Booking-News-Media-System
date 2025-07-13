
from venue import models as vmd
from mainapp.selectors import selector as sc

class KhaltiPaymentModule:

    def __init__(self ,data):
        self.data = data
        self.khalti_secret_key = sc.get_secret_key(venue_id=self.data['venueId'])

        
