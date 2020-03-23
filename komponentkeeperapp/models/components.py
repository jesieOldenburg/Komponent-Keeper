from django.db import models
from .creators import Creator

class Component(models.Model):
    '''
    description: This class creates a component and its associated data
    author: Jesie Oldenburg
    properties:
        creator: This will contain user id's to see which user created it
        name: this will contain the name of the component
        image: This property will contain a path to an image file
        description: this property will contain a description of the component
    '''

    creator = models.ForeignKey("Creator",  on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True, default=None)
    # upload_to tells the model where to store the image, by default images/ will go to the media directory
    image = models.ImageField(upload_to='images/', null=True)
    description = models.CharField( max_length=200, null=True, default=None)

    class Meta:
        verbose_name = ("Component")
        verbose_name_plural = ("Components")

    def get_absolute_url(self):
        return reverse("component_detail", kwargs={"pk": self.pk})
