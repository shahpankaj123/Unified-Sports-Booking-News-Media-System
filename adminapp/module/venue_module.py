from mainapp import models as md

from venue import models as smd

from mainapp.selectors.common_functions import message

from django.db.models import F

class VenueModule:

    def __init__(self ,data):
        self.data = data

    def create_venue(self):
        try:
            owner_email = self.data['ownerEmail']
            name = self.data['name']
            address = self.data['address']
            city = self.data['cityId']
            phoneNumber = self.data['phoneNumber']
            email = self.data['email']
            cityId = self.data['cityId']

            user = md.Users.objects.get(Email = owner_email)
            user.UserType = md.UserTypes.objects.get(UserType = 'VenueUsers')
            user.save()

            city = md.City.objects.get(CityID = cityId)

            smd.Venue.objects.create(Owner = user ,Email = email ,PhoneNumber = phoneNumber,Name = name ,Address = address ,City = city ,IsActive = True)
            return message('Venue Created Sucessfully') ,200

        except Exception as e:
            print(e)

    def get_all_venue(self):
        try:
            return smd.Venue.objects.all().values(ownerEmail = F('Owner__Email'),name = F('Name'),address = F('Address'))

        except Exception as e:
            print(e)    



