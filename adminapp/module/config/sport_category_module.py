from mainapp import models as mm
from mainapp.selectors.common_functions import message
from django.db.models import F

class SportCategoryModule:

    def __init__(self, data):
        self.data = data

    def create_sport_category(self):
        try:
            sport_category = self.data['sportCategory']
            mm.SportCategory.objects.create(SportCategory=sport_category)
            return message('Sport category created successfully'), 201
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500

    def get_all_sport_categories(self):
        return mm.SportCategory.objects.all().values(
            sportCategoryId=F('SportCategoryID'),
            sportCategory=F('SportCategory')
        ), 200

    def get_sport_category_by_id(self):
        try:
            sport_category_id = self.data['sportCategoryId']
            return mm.SportCategory.objects.values(
                sportCategoryId=F('SportCategoryID'),
                sportCategory=F('SportCategory')
            ).get(SportCategoryID=sport_category_id), 200
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except mm.SportCategory.DoesNotExist:
            return message('Sport category not found'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500

    def update_sport_category(self):
        try:
            sport_category = self.data['sportCategory']
            sport_category_id = self.data['sportCategoryId']

            sport_category_obj = mm.SportCategory.objects.get(SportCategoryID=sport_category_id)
            sport_category_obj.SportCategory = sport_category
            sport_category_obj.save()

            return message('Sport category updated successfully'), 200
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except mm.SportCategory.DoesNotExist:
            return message('Sport category not found'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500

    def delete_sport_category(self):
        try:
            sport_category_id = self.data['sportCategoryId']
            mm.SportCategory.objects.get(SportCategoryID=sport_category_id).delete()
            return message('Sport category deleted successfully'), 200
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except mm.SportCategory.DoesNotExist:
            return message('Sport category not found'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500
