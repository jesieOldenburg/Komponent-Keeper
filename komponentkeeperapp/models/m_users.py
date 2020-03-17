from django.db import models

class User(models.Model):
    '''
    description: This class creates a component and its associated data
    author: Jesie Oldenburg
    properties:
        user_id: This will contain user id's to see which user created it
        username: This will contain the user's username
        first_name: This will contain the user's first name
        last_name: This will contain the user's last name
        email: This will contain the user's email
        role: This will contain the user's role
    '''

    user_id = models.models.ForeignKey("users",  on_delete=models.CASCADE)
    username = models.CharField(max_length=25, default=None, null=True)
    first_name = models.CharField(max_length=50, default=None, null=True)
    last_name = models.CharField(max_length=50, default=None, null=True)
    email = models.CharField(max_length=75, default=None, null=True)
    role = models.IntegerField()
    
    class Meta:
        verbose_name = ("Computer")
        verbose_name_plural = ("Computers")

    def get_absolute_url(self):
        return reverse("Computer_detail", kwargs={"pk": self.pk})
