from cultureapp.models import Booking, Profile, visitplan, services
from django.contrib import admin

class visitplanAdmin(admin.ModelAdmin):
    filter_horizontal =('service',)

admin.site.register(Profile)
admin.site.register(Booking)
admin.site.register(visitplan,visitplanAdmin)
admin.site.register(services)