from django.contrib import admin
from venue import models as vmd

# Register your models here.
admin.site.register(vmd.Venue)
admin.site.register(vmd.Court)
admin.site.register(vmd.CourtImages)
admin.site.register(vmd.VenueImages)

admin.site.register(vmd.Availability)
admin.site.register(vmd.Booking)
admin.site.register(vmd.PaymentTransaction)

admin.site.register(vmd.VenueApplication)
admin.site.register(vmd.VenueApplicationDocument)

admin.site.register(vmd.Event)
admin.site.register(vmd.EventRegisteredRecord)
