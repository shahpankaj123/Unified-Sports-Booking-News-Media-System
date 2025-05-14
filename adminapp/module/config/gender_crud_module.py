from mainapp import models as mm
from mainapp.selectors.common_functions import message

from django.db.models import F

class GenderModule:

    def __init__(self, data):
        self.data = data

    def create_gender(self):
        try:
            gender = self.data['gender']
            mm.Gender.objects.create(Gender=gender)
            return message('Gender created successfully'), 201
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500

    def get_all_genders(self):
        return mm.Gender.objects.all().values(genderId=F('GenderID'), gender=F('Gender')), 200

    def get_gender_by_id(self):
        try:
            gender_id = self.data['genderId']
            return mm.Gender.objects.values(genderId=F('GenderID'), gender=F('Gender')).get(GenderID=gender_id), 200
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except mm.Gender.DoesNotExist:
            return message('Gender not found'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500

    def update_gender(self):
        try:
            gender = self.data['gender']
            gender_id = self.data['genderId']

            gender_obj = mm.Gender.objects.get(GenderID=gender_id)
            gender_obj.Gender = gender
            gender_obj.save()

            return message('Gender updated successfully'), 200
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except mm.Gender.DoesNotExist:
            return message('Gender not found'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500

    def delete_gender(self):
        try:
            gender_id = self.data['genderId']
            mm.Gender.objects.get(GenderID=gender_id).delete()
            return message('Gender deleted successfully'), 200
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except mm.Gender.DoesNotExist:
            return message('Gender not found'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500
