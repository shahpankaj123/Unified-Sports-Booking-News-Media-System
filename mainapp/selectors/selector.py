from mainapp import models as md

from django.core.cache import cache

def get_status_from_id( status_id :str):
    try:
        cache_key = f'status_{status_id}'
        if cache.get(cache_key):
            return cache.get(cache_key)
        else:
          status = md.Status.objects.get(StatusID = status_id)
          cache.set(cache_key, status, timeout=60 * 60)
          return status
    except md.Status.DoesNotExist:
        return None