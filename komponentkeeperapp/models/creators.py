from django.db import models
from django.contrib.auth.models import User

class Creator(models.Model):
    '''
    description: This class creates a component and its associated data
    author: Jesie Oldenburg
    properties:
        user: This will contain user id's to see which user created it
        username: This will contain the user's username
        first_name: This will contain the user's first name
        last_name: This will contain the user's last name
        email: This will contain the user's email
        role: This will contain the user's role
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=25, default=None, null=True)
    first_name = models.CharField(max_length=50, default=None, null=True)
    last_name = models.CharField(max_length=50, default=None, null=True)
    email = models.CharField(max_length=75, default=None, null=True)
    role = models.CharField(max_length=15, default=None, null=True)
    
    class Meta:
        verbose_name = ("Creator")
        verbose_name_plural = ("Creators")

    def get_absolute_url(self):
        return reverse("Creator", kwargs={"pk": self.pk})
