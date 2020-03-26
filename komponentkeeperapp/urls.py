# from django.conf.urls import url, include
from django.urls import path, include
from django.conf.urls import url
from .views import *

app_name = 'komponentkeeperapp'

urlpatterns = [
    path('accounts/login', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # * Here is the edit   
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
    
    path('home', home, name='home'),
    path('components/', components_list, name='components'),
    # url(r'^components/(?P<pk>.*)', components_list, name='components'),

    path('components/<int:component_id>/', component_details, name='component'),
    path('components/form', upload_component, name='upload_component'),
    path('components/<int:component_id>/form', edit_component_form, name='edit_component_form'),

    path('success', success, name='success'), 
    path('edit_success', success, name='edit_success'), 
    path('fail', fail, name='fail'), 

    # Snippet related routes
    path('snippets/<int:component_id>/form', snippet_form, name='snippet_form'), # * Added <int:component_id>    
    path('snippets/<int:component_id>', snippets_list, name='snippets'), 
    path('snippets/<int:snippet_id>/form', edit_snippet_form, name='edit_snippet_form'),
    path('snippets/<int:snippet_id>/editSnippet', edit_snippet_form, name='edit_snippet_form'),
    path('snippets/<int:snippet_id>/', snippet_details, name='snippet'),
    
]