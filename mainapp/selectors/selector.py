from mainapp import models as md
from venue import models as vmd

from django.core.cache import cache

def get_user_from_id(user_id :str):
    try:
        cache_key = f'user_{user_id}'
        if cache.get(cache_key):
            print("cached data fetch")
            return cache.get(cache_key)
        else:
          usr = md.Users.objects.get(UserID = user_id)
          print("db data fetch")
          cache.set(cache_key, usr, timeout=60 * 60)
          return usr
    except md.Users.DoesNotExist:
        return None 
    
def get_user_from_email(email :str):
    try:
        cache_key = f'user_{email}'
        if cache.get(cache_key):
            print("cached data fetch")
            return cache.get(cache_key)
        else:
          usr = md.Users.objects.get(Email = email)
          print("db data fetch")
          cache.set(cache_key, usr, timeout=60 * 60)
          return usr
    except md.Users.DoesNotExist:
        return None 
    
def get_status_from_id( status_id :str):
    try:
        cache_key = f'status_{status_id}'
        if cache.get(cache_key):
            print("cached data fetch")
            return cache.get(cache_key)
        else:
          status = md.Status.objects.get(StatusID = status_id)
          print("db data fetch")
          cache.set(cache_key, status, timeout=60 * 60)
          return status
    except md.Status.DoesNotExist:
        return None
    
def get_user_type_from_id(user_type_id :str):
    try:
        cache_key = f'user_type_{user_type_id}'
        if cache.get(cache_key):
            print("cached data fetch")
            return cache.get(cache_key)
        else:
          usr_type = md.UserTypes.objects.get(UserTypeID = user_type_id)
          print("db data fetch")
          cache.set(cache_key, usr_type, timeout=60 * 60)
          return usr_type
    except md.UserTypes.DoesNotExist:
        return None   
    
def get_court_from_id(court_id :str):
    try:
        cache_key = f'court_{court_id}'
        if cache.get(cache_key):
            print("cached data fetch")
            return cache.get(cache_key)
        else:
          court = vmd.Court.objects.get(CourtID = court_id)
          print("db data fetch")
          cache.set(cache_key, court, timeout=60 * 60)
          return court
    except vmd.Court.DoesNotExist:
        return None     