from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F

from adds import models as mm
from mainapp import models as mmd

from mainapp.selectors.common_functions import message,is_none

class ReelModule:

    def __init__(self, data=None, request=None):
        self.data = data
        self.request = request

    def create_post(self):
        try:
            title = self.data['title']
            description = self.data['description']
            category_id = self.data['categoryId']
            video = self.request.FILES['video']

            category = mmd.SportCategory.objects.get(SportCategoryID=category_id)
            author = mmd.Users.objects.get(Email = self.request.user)

            mm.Reel.objects.create(
                Title=title,
                Description=description,
                Category=category,
                Author=author,
                Video = video,
            )
            return message("Post Created Successfully"), 200
        except KeyError as key:
            return message(f"{key} is missing"), 400
        except Exception as e:
            print(e)
            return message("Something went wrong"), 500

    def get_all_posts(self):
        try:
            posts = mm.Reel.objects.select_related('Author', 'Category').filter(Author__Email = self.request.user).order_by('-Date', '-Time')
            post_list = []
            for post in posts:
                post_list.append({
                    "reelId": str(post.ReelID),
                    "title": post.Title,
                    "description": post.Description,
                    "category": post.Category.SportCategory if post.Category else None,
                    "date": post.Date.strftime("%Y-%m-%d"),
                    "time": post.Time.strftime("%H:%M:%S"),
                    "video": "http://127.0.0.1:8000" + post.Video.url if post.Video else None,
                })
            return post_list, 200
        except Exception as e:
            print(e)
            return message("Failed to retrieve posts"), 500

    def get_post_detail(self):
        try:
            reel_id = self.data['reelId']
            post = mm.Reel.objects.select_related('Author', 'Category').get(ReelID=reel_id)
            data = {
                "postID": str(post.ReelID),
                "title": post.Title,
                "description": post.Description,
                "category": post.Category.SportCategory if post.Category else None,
                "date": post.Date.strftime("%Y-%m-%d"),
                "time": post.Time.strftime("%H:%M:%S"),
                "postImage": "http://127.0.0.1:8000" + post.Video.url if post.Video else None,
            }
            return data, 200
        except ObjectDoesNotExist:
            return message("Post not found"), 404
        except Exception as e:
            print(e)
            return message("Something went wrong"), 500

    def update_post(self):
        try:
            reel_id = self.data['reelId']
            title = self.data['title']
            desc = self.data['description']
            category_id = self.data['categoryId']
            video = self.request.FILES.get('video')

            post = mm.Reel.objects.get(ReelID=reel_id)

            post.Category = mmd.SportCategory.objects.get(SportCategoryID=category_id)
            post.Title = title
            post.Description = desc
            if video is not None:
                post.Video = video
            post.save()
            return message("Reel updated successfully"), 200
        
        except KeyError as key:
            return message(f'{key} is Missing'),404
        except ObjectDoesNotExist:
            return message("Reel not found"), 404
        except Exception as e:
            print(e)
            return message("Update failed"), 500

    def delete_post(self):
        try:
            post_id = self.data['reelId']
            post = mm.Reel.objects.get(ReelID=post_id)
            post.delete()
            return message("Reel deleted successfully"), 200
        except ObjectDoesNotExist:
            return message("Reel not found"), 404
        except Exception as e:
            print(e)
            return message("Delete failed"), 500