import sys
import os
import django

sys.path.append('listings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'listings.settings'
django.setup()

from main.models import Condition, Location, ListingType

conditions = ['Like New', 'Very Good', 'Good', 'Acceptable']

if not Condition.objects.all():
    print("Adding Conditions in the database:")
    for condition in conditions:
        Condition(condition = condition)c.save()
        print(f"\tAdded {condition}")
        
else:
    print('There are already some Condition objects in the database. Skipping...')

locations = [
    'Krishna Hostel (DoH 1)',
    'Bhagirathi Hostel (DoH 2)',
    'Brahmaputra Hostel (DoH 3)',
    'Ganga Hostel (DoH 4)',
    'Mahanadi Hostel (SoH 1)',
    'Rushikulya Hostel (SoH 2)',
    'Daya Hostel (SoH 3)',
    'Kaveri Hostel (SoH 4)',
    'Yamuna Hostel (SoH 5)',
]

if not Location.objects.all():
    print("Adding Locations in the database:")
    for location in locations:
        Location(location = location).save()
        print(f"\tAdded {location}")
else:
    print('There are already some Location objects in the database. Skipping...')


categories = [
    'Bags/Luggage',
    'Bicycles',
    'Books',
    'Electronics',
    'Furniture',
    'Gym Equipment',
    'Musical Instruments',
    'Pillow/Mattresses',
    'Sports Equipment',
    'Stationary'
]

if not ListingType.objects.all():
    print("Adding ListingTypes in the database:")
    for category in categories:
        ListingType(name = category).save()
        print(f"\tAdded {category}")
else:
    print('There are already some ListingType objects in the database. Skipping...')

