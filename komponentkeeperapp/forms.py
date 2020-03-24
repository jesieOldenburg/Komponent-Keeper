from django.forms import ModelForm
from .models.components import Component

class AddImageForm(ModelForm):
    class Meta:
        model = Component
        fields = ['name', 'image', 'description']

class EditComponentForm(ModelForm):
    class Meta:
        model = Component
        fields = ['name', 'image', 'description']