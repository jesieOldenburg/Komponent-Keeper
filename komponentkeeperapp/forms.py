from django.forms import ModelForm
from .models.components import Component

class AddImageForm(ModelForm):
    class Meta:
        model = Component
        fields = ['name', 'image', 'description']
    # name = forms.TextInput()
    # image = forms.ImageField()
    # description = forms.Textarea()