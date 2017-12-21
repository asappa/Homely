from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """ User Profile for Home owner account, Renter Account
        diffrenciate using User Groups (owner, renter)
    """
    user = models.ForeignKey(User)
    # user contains, first_name, last_name, email, username and password
    phone = models.CharField(max_length=14, blank=True, null=True)
    address = models.TextField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.user.username


class HomeDetails(models.Model):
    """ Details of Home
    """
    def home_image(self, filename):
        """ image handling function
        """
        url = "uploads/users/%s/%s" % (self.owner.username, filename)
        return url
    owner = models.ForeignKey(User)
    rent = models.FloatField(default=0.0)
    title = models.CharField(max_length=64, null=True)
    description = models.TextField(max_length=256, null=True, blank=True)
    image = models.ImageField(upload_to=home_image, blank=True, null=True)

    def __str__(self):
        return self.title


class HomeRentDetails(models.Model):
    """ Model contains rent out details of home with
        rentout dates and price
    """
    home = models.ForeignKey(HomeDetails)
    renter = models.ForeignKey(UserProfile, related_name='renter')
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.TextField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.home.title




