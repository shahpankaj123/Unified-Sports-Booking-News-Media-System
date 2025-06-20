from django.core.cache import cache
from adds import models as amd
from django.db.models import F,Value,CharField
from django.db.models.functions import Concat

from mainapp.selectors.common_functions import message

class SocialMediaModule:

    def __init__(self ,data):
        self.data = data

    def get_news_data(self):
        try:
            cache_key = "post_news"
            if cache.get(cache_key):
                print("Cached data")
                return cache.get(cache_key) ,200
            else:
                post_data = amd.Post.objects.all().values(postId = F('PostID') ,title =F('Title') ,description =F('Description') ,date = F('Date') ,time=F('Time'),postImage = Concat(Value('http://127.0.0.1:8000/media/') ,F('PostImage'),output_field=CharField()),category= F('Category__SportCategory'),author = Concat(F('Author__FirstName'),Value(' '),F('Author__LastName'))).order_by('-Date')
                cache.set(cache_key,post_data,timeout=60)
                return post_data ,200
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500 

    def get_news_by_id(self):
        try:
            post_id = self.data['postId']
            cache_key = f"post_news__{post_id}"
            if cache.get(cache_key):
                print("Cached data")
                return cache.get(cache_key) ,200
            else:
                post_data = amd.Post.objects.values(postId = F('PostID') ,title =F('Title') ,description =F('Description') ,date = F('Date') ,time=F('Time'),postImage = Concat(Value('http://127.0.0.1:8000/media/') ,F('PostImage'),output_field=CharField()),category= F('Category__SportCategory'),author = Concat(F('Author__FirstName'),Value(' '),F('Author__LastName'))).get(PostID = post_id)
                cache.set(cache_key,post_data,timeout=60)
                return post_data ,200 
        except KeyError as k:
            return message(f'{k} is Missing') ,404    
        except amd.Post.DoesNotExist:
            return message('Post Doesnot Exists') ,400   
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500 

    def get_reels_data(self):
        try:
            cache_key = "reels"
            if cache.get(cache_key):
                print("Cached data")
                return cache.get(cache_key) ,200
            else:
                reel_data = amd.Reel.objects.all().values(reelId = F('ReelID') ,title =F('Title') ,description =F('Description') ,date = F('Date') ,time=F('Time'),video_url = Concat(Value('http://127.0.0.1:8000/media/') ,F('Video'),output_field=CharField()),category= F('Category__SportCategory'),author = Concat(F('Author__FirstName'),Value(' '),F('Author__LastName'))).order_by('-Date')
                cache.set(cache_key,reel_data,timeout=60)
                return reel_data ,200
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500 

    def get_reel_by_id(self):
        try:
            reel_id = self.data['reelId']
            cache_key = f"reel__{reel_id}"
            if cache.get(cache_key):
                print("Cached data")
                return cache.get(cache_key) ,200
            else:
                reel_data = amd.Reel.objects.values(reelId = F('ReelID') ,title =F('Title') ,description =F('Description') ,date = F('Date') ,time=F('Time'),video_url = Concat(Value('http://127.0.0.1:8000/media/') ,F('Video'),output_field=CharField()),category= F('Category__SportCategory'),author = Concat(F('Author__FirstName'),Value(' '),F('Author__LastName'))).get(ReelID = reel_id)
                cache.set(cache_key,reel_data,timeout=60)
                return reel_data ,200
        except KeyError as k:
            return message(f'{k} is Missing') ,404        
        except amd.Reel.DoesNotExist:
            return message('Reel Doesnot Exists') ,400      
        except Exception as e:
            print(e)
            return message('Something Went Wrong') ,500                  