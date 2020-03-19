from django.conf.urls import url
from django.urls import path
from .views import *

app_name = 'komponentkeeperapp'

urlpatterns = [
    path('', components_list, name='home'),
    path('components/', components_list, name='components')
]