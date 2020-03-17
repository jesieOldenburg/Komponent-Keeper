from django.db import models

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

    user_id = models.models.ForeignKey("users",  on_delete=models.CASCADE)
    snippet_language = models.CharField(max_length=50, default=None, null=True)
    code_snippet = models.CharField( max_length=500)
    description = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = ("CodeSnippet")
        verbose_name_plural = ("CodeSnippets")

    def get_absolute_url(self):
        return reverse("CodeSnippet_details", kwargs={"pk": self.pk})
