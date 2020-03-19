from django.conf.urls import url, include
from django.urls import path
from .views import *

app_name = 'komponentkeeperapp'

urlpatterns = [
    path('', home, name='home'),
    path('components/', components_list, name='components'),
    path('snippets/', snippets_list, name='snippets')
]