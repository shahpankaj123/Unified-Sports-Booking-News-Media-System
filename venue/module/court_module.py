from mainapp.selectors.common_functions import message

from venue import models as vmd
from mainapp import models as md

from django.db.models import F
class CourtModule:

    def __init__(self ,data , request):
        self.data = data
        self.request = request

    def get_court_data(self):
        try:
            court_obj = vmd.Court.objects.filter(Venue__Owner__Email = self.request.user)
            data = []
            for court in court_obj:
                court_img = court.courts_images.all()
                data = vmd.Court.objects.values(courtId = F('CourtID') ,courtName = F('Name'),courtType = F('CourtType'),courtCategory = F('SportCategory__SportCategory'),hourlyRate = F('HourlyRate'),isActive = F('IsActive')).get(CourtID = court)
                data['courtImage'] = ["http://127.0.0.1:8000/media/" + x['Image'] for x in  court_img.values('Image')]
                data.append(data)
            return data , 200
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500 
        
    def get_court_data_by_id(self):
        try:
            court_id = self.data['courtId']
            court = vmd.Court.objects.get(CourtID = court_id)
            court_img = court.courts_images.all()
            data = vmd.Court.objects.values(courtId = F('CourtID') ,courtName = F('Name'),courtType = F('CourtType'),courtCategory = F('SportCategory__SportCategory'),hourlyRate = F('HourlyRate'),isActive = F('IsActive')).get(CourtID = court)
            data['courtImage'] = ["http://127.0.0.1:8000/media/" + x['Image'] for x in  court_img.values('Image')]
            return data , 200
        except vmd.Court.DoesNotExist:
            return message('Court Not Found'), 404
        except KeyError as k:
            return message(f'{k} is Missing'), 400
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500     

    def create_court_data(self):
        try:
            court_name = self.data['courtName']
            court_category = self.data['courtCategoryId']
            hourly_rate = self.data['hourlyRate']
            capacity = self.data['capacity']
            surface_type = self.data['surfaceType']
            desc = self.data['desc']

            court = vmd.Court(
                Name = court_name,
                Description = desc,
                SurfaceType = surface_type,
                Capacity = capacity,
                Venue = vmd.Venue.objects.get(Owner__Email = self.request.user),
                SportCategory = md.SportCategory.objects.get(SportCategoryID = court_category),
                HourlyRate = hourly_rate,
            )
            court.save()
            return message('Court Created Successfully'), 200
        except md.SportCategory.DoesNotExist:
            return message('Sport Category Not Found'), 404
        except KeyError as k:
            return message(f'{k} is Missing'), 400 
        except Exception as e:
            print(e)
            return message('Something Went Wrong'), 500     
        

    def update_court_data(self): 
        try:
            court_id = self.data['courtId']
            court_name = self.data['courtName']
            court_category = self.data['courtCategoryId']
            hourly_rate = self.data['hourlyRate']
            capacity = self.data['capacity']
            surface_type = self.data['surfaceType']
            desc = self.data['desc']
            is_active = self.data['isActive']

            court = vmd.Court.objects.get(CourtID = court_id)

            court.Name = court_name
            court.Description = desc
            court.SurfaceType = surface_type
            court.Capacity = capacity
            court.HourlyRate = hourly_rate
            court.IsActive = is_active
            court.SportCategory = md.SportCategory.objects.get(SportCategoryID = court_category)
            court.save()
            return message('Court Updated Successfully'), 200
        
        except vmd.Court.DoesNotExist:
            return message('Court Not Found'), 404
        except md.SportCategory.DoesNotExist:
            return message('Sport Category Not Found'), 404
        except KeyError as k:
            return message(f'{k} is Missing'), 400 
        except Exception as e:
            print(e)
            return message('Something Went Wrong'), 500    

    def upload_court_image(self):
        try:
            court_id = self.data['courtId']
            court = vmd.Court.objects.get(CourtID = court_id)
            image = self.request.FILES['image']
            vmd.CourtImages.objects.create(
                Court = court,
                Image = image
            )
            return message('Court Image Uploaded Successfully'), 200
        except vmd.Court.DoesNotExist:
            return message('Court Not Found'), 404
        except KeyError as k:
            return message(f'{k} is Missing'), 400 
        except Exception as e:
            print(e)
            return message('Something Went Wrong'), 500        