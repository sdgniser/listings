from django.contrib import admin

from .models import Location, Condition, Listing, ListingType

admin.site.register(Location)
admin.site.register(Condition)
admin.site.register(ListingType)
admin.site.register(Listing)
