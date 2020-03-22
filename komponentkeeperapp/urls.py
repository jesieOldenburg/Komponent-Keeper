# from django.conf.urls import url, include
from django.urls import path, include
from .views import *

app_name = 'komponentkeeperapp'

urlpatterns = [
    path('home', home, name='home'),
    
    path('components/', components_list, name='components'),
    path('components/form', component_form, name='component_form'),
    path('components/<int:component_id>/', component_details, name='component'),
    
    path('snippets/', snippets_list, name='snippets'),
    path('snippets/form', snippet_form, name='snippet_form'),
    path('snippets/<int:code_snippet_id>/', snippet_details, name='snippet'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
]