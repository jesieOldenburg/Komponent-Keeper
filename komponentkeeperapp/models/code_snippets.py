from django.db import models
from .creators import Creator

class CodeSnippet(models.Model):
    '''
    description: This class creates a component and its associated data
    author: Jesie Oldenburg
    properties:
        user_id: This will contain user id's to see which user created the snippet
        snippet_language: This will contain a string describing the language of the snipped
        code_snippet: This will contain a code snippet for a component
        description: This will contain any notes about the snippet
    '''

    creator = models.ForeignKey("Creator",  on_delete=models.SET_NULL, null=True)
    snippet_language = models.CharField(max_length=50, default=None, null=True)
    code_snippet = models.TextField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = ("CodeSnippet")
        verbose_name_plural = ("CodeSnippets")

    def get_absolute_url(self):
        return reverse("CodeSnippet_details", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f'creator :: {self.creator}'
