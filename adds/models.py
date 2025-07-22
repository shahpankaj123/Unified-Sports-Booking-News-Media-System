from django.db import models
import uuid

from mainapp import models as mm

# Create your models here.

class Post(models.Model):

    class Meta:
        db_table = 'Post'

    PostID=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Category = models.ForeignKey(mm.SportCategory, on_delete=models.SET_NULL,null=True)
    Date = models.DateField(auto_now_add =True)
    Time=models.TimeField(auto_now_add = True)
    Author = models.ForeignKey(mm.Users, on_delete=models.SET_NULL,null=True)
    PostImage = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return self.Title
    
    
class Reel(models.Model):

    class Meta:
        db_table = 'Reel'

    ReelID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Title = models.CharField(max_length=100)
    Description = models.TextField(blank=True, null=True)
    Category = models.ForeignKey(mm.SportCategory, on_delete=models.SET_NULL, null=True)
    Video = models.FileField(upload_to='reels_videos/')
    Thumbnail = models.ImageField(upload_to='reels_thumbnails/', null=True, blank=True)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    Author = models.ForeignKey(mm.Users, on_delete=models.SET_NULL, null=True)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.Title    
