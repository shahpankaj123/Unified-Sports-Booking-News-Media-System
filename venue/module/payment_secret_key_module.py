from venue import models as vmd

from mainapp.selectors.common_functions import message

class PaymentSecreatKeyModule:

    def __init__(self ,data):
        self.data = data

    def create(self):
        try:
            secret_key = self.data['secretKey']
            venue_id = self.data['venueId']

            if vmd.OnlinePaymentKhaltiSecretKey.objects.filter(Venue__VenueID = venue_id).exists():
                return message("Secret Key Already Exists") ,400

            venue = vmd.Venue.objects.get(VenueID = venue_id)
            vmd.OnlinePaymentKhaltiSecretKey.objects.create(Venue = venue ,PrivateSecretKey = secret_key)
            return message('Created Successfully') ,200
        
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500
        
    def get(self):
        try:
            venue_id = self.data['venueId']
            return vmd.OnlinePaymentKhaltiSecretKey.objects.values().get(Venue__VenueID = venue_id) ,200

        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500    
