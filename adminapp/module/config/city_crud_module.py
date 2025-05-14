from mainapp import models as mm
from mainapp.selectors.common_functions import message

from django.db.models import F

class CityModule:

    def __init__(self, data):
        self.data = data

    def create_city(self):
        try:
            city_name = self.data['cityName']
            mm.City.objects.create(CityName=city_name)
            return message('City created successfully'), 201
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500

    def get_all_cities(self):
        return mm.City.objects.all().values(cityId=F('CityID'), cityName=F('CityName')), 200

    def get_city_by_id(self):
        try:
            city_id = self.data['cityId']
            return mm.City.objects.values(cityId=F('CityID'), cityName=F('CityName')).get(CityID=city_id), 200
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except mm.City.DoesNotExist:
            return message('City not found'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500

    def update_city(self):
        try:
            city_name = self.data['cityName']
            city_id = self.data['cityId']

            city_obj = mm.City.objects.get(CityID=city_id)
            city_obj.CityName = city_name
            city_obj.save()

            return message('City updated successfully'), 200
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except mm.City.DoesNotExist:
            return message('City not found'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500

    def delete_city(self):
        try:
            city_id = self.data['cityId']
            mm.City.objects.get(CityID=city_id).delete()
            return message('City deleted successfully'), 200
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except mm.City.DoesNotExist:
            return message('City not found'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500
