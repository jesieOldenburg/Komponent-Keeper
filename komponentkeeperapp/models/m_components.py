from django.db import models

class Component(models.Model):
    '''
    description: This class creates a component and its associated data
    author: Jesie Oldenburg
    properties:
        user_id: This will contain user id's to see which user created it
        image: This property will contain a path to an image file
        description: this property will contain a description of the component
    '''

    user_id = models.models.ForeignKey("users",  on_delete=models.CASCADE)
    image = models.CharField( max_length=150, null=True, default=None)
    description = models.CharField( max_length=200, null=True, default=None)

    class Meta:
        verbose_name = ("Component")
        verbose_name_plural = ("Components")

    def get_absolute_url(self):
        return reverse("component_detail", kwargs={"pk": self.pk})