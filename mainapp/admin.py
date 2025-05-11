from django.contrib import admin

from mainapp import models as md

# Register your models here.

admin.site.register(md.Users)
admin.site.register(md.OTPData)
admin.site.register(md.Gender)
admin.site.register(md.PaymentType)
admin.site.register(md.Status)
admin.site.register(md.UserTypes)
admin.site.register(md.City)
