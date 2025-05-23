from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F

from adds import models as mm
from mainapp import models as mmd

from mainapp.selectors.common_functions import message,is_none

class PostModule:

    def __init__(self, data=None, request=None):
        self.data = data
        self.request = request

    def create_post(self):
        try:
            title = self.data['title']
            description = self.data['description']
            category_id = self.data['categoryId']
            post_image = self.request.FILES['postImage']

            category = mmd.SportCategory.objects.get(SportCategoryID=category_id)
            author = mmd.Users.objects.get(Email = self.request.user)

            mm.Post.objects.create(
                Title=title,
                Description=description,
                Category=category,
                Author=author,
                PostImage=post_image
            )
            return message("Post Created Successfully"), 200
        except KeyError as key:
            return message(f"{key} is missing"), 400
        except Exception as e:
            print(e)
            return message("Something went wrong"), 500

    def get_all_posts(self):
        try:
            posts = mm.Post.objects.select_related('Author', 'Category').filter(Author__Email = self.request.user).order_by('-Date', '-Time')
            post_list = []
            for post in posts:
                post_list.append({
                    "postID": str(post.PostID),
                    "title": post.Title,
                    "description": post.Description,
                    "category": post.Category.SportCategory if post.Category else None,
                    "date": post.Date.strftime("%Y-%m-%d"),
                    "time": post.Time.strftime("%H:%M:%S"),
                    "postImage": "http://127.0.0.1:8000" + post.PostImage.url if post.PostImage else None,
                })
            return post_list, 200
        except Exception as e:
            print(e)
            return message("Failed to retrieve posts"), 500

    def get_post_detail(self):
        try:
            post_id = self.data['postId']
            post = mm.Post.objects.select_related('Author', 'Category').get(PostID=post_id)
            data = {
                "postID": str(post.PostID),
                "title": post.Title,
                "description": post.Description,
                "category": post.Category.SportCategory if post.Category else None,
                "date": post.Date.strftime("%Y-%m-%d"),
                "time": post.Time.strftime("%H:%M:%S"),
                "postImage": "http://127.0.0.1:8000" + post.PostImage.url if post.PostImage else None,
            }
            return data, 200
        except ObjectDoesNotExist:
            return message("Post not found"), 404
        except Exception as e:
            print(e)
            return message("Something went wrong"), 500

    def update_post(self):
        try:
            post_id = self.data['postId']
            title = self.data['title']
            desc = self.data['description']
            category_id = self.data['categoryId']
            post_img = self.request.FILES.get('postImage')

            post = mm.Post.objects.get(PostID=post_id)

            post.Category = mmd.SportCategory.objects.get(SportCategoryID=category_id)
            post.Title = title
            post.Description = desc
            if post_img is not None:
                post.PostImage = post_img
            post.save()
            return message("Post updated successfully"), 200
        
        except KeyError as key:
            return message(f'{key} is Missing'),404
        except ObjectDoesNotExist:
            return message("Post not found"), 404
        except Exception as e:
            print(e)
            return message("Update failed"), 500

    def delete_post(self):
        try:
            post_id = self.data['postId']
            post = mm.Post.objects.get(PostID=post_id)
            post.delete()
            return message("Post deleted successfully"), 200
        except ObjectDoesNotExist:
            return message("Post not found"), 404
        except Exception as e:
            print(e)
            return message("Delete failed"), 500
