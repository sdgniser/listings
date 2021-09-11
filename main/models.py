from django.db import models
from django.utils.timezone import now
from django.urls import reverse

class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location


class Condition(models.Model):
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.condition

class ListingType(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Listing Title')
    category = models.ForeignKey(ListingType, verbose_name = 'Category',
                                 on_delete = models.CASCADE)
    price = models.IntegerField(verbose_name = 'Price (in Rupees)')
    location = models.ForeignKey(Location, on_delete = models.CASCADE, 
                                 verbose_name = 'Location')
    condition = models.ForeignKey(Condition, on_delete = models.CASCADE, 
                                  verbose_name = 'Item Condition')
    description = models.TextField(verbose_name = 'Description')
    photo = models.ImageField(upload_to='images')

    sold = models.BooleanField(default = False)

    op = models.CharField(max_length = 200, verbose_name = 'Your Name')
    email = models.EmailField(verbose_name = 'Your Email Address')
    phone = models.BigIntegerField(verbose_name = 'Contact Number (optional)',
                                   blank = True, null = True)

    created = models.DateTimeField(default = now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def name(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('main:listing', kwargs = {'pk': self.pk})
