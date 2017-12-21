from django.contrib import admin

from .models import (
    UserProfile, HomeDetails,
    HomeRentDetails
)
admin.site.register(UserProfile)
admin.site.register(HomeDetails)
admin.site.register(HomeRentDetails)
