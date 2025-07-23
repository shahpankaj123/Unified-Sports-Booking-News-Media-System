from venue import models as vmd

from mainapp.selectors.common_functions import message

class PaymentSecreatKeyModule:

    def __init__(self ,data):
        self.data = data

    def create(self):
        try:
            secret_key = self.data['secretKey']
            user_id = self.data['userId']

            if vmd.OnlinePaymentKhaltiSecretKey.objects.filter(Venue__Owner__UserID = user_id).exists():
                return message("Secret Key Already Exists") ,400

            venue = vmd.Venue.objects.get(Owner__UserID = user_id)
            vmd.OnlinePaymentKhaltiSecretKey.objects.create(Venue = venue ,PrivateSecretKey = secret_key)
            return message('Created Successfully') ,200
        
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500
        
    def get(self):
        try:
            user_id = self.data['userId']
            return vmd.OnlinePaymentKhaltiSecretKey.objects.values().get(Venue__Owner__UserID = user_id) ,200

        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500  

    def update(self):
        try:
            secret_key = self.data['secretKey']
            secret_id = self.data['secretkeyId']

            data = vmd.OnlinePaymentKhaltiSecretKey.objects.get(id = secret_id)
            data.PrivateSecretKey = secret_key
            data.save()
            return message('Updated Successfully') ,200
        except Exception as e:
            print(e) 
            return message('Something Went Wrong') ,500      
