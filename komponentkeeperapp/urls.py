# from django.conf.urls import url, include
from django.urls import path, include
from .views import *

app_name = 'komponentkeeperapp'

urlpatterns = [
    path('home', home, name='home'),
    
    path('components/', components_list, name='components'),
    path('components/form', upload_component, name='upload_component'),
    path('components/<int:component_id>/form', edit_component_form, name='edit_component_form'),
    path('components/<int:component_id>/', component_details, name='component'),

    
    path('success', success, name='success'), 
    path('edit_success', success, name='edit_success'), 
    path('fail', fail, name='fail'), 
    
    # * WE ARE HERE
    path('snippets/<int:component_id>/form', snippet_form, name='snippet_form'), # * Added <int:component_id>
    
    path('snippets/<int:component_id>', snippets_list, name='snippets'), 
    path('snippets/<int:code_snippet_id>/form', edit_snippet_form, name='edit_snippet_form'),
    path('snippets/<int:code_snippet_id>/', snippet_details, name='snippet'),
    
    path('accounts/login', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
]