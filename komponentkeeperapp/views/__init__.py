from .components.list import components_list
from .components.details import component_details# * remove add snippet
from .components.form import component_form
from .components.image_form import upload_component, success, edit_component_form, fail, edit_success

from .code_snippets.list import snippets_list
from .code_snippets.details import snippet_details
from .code_snippets.form import snippet_form 
from .code_snippets.edit_snippet_form import edit_snippet_form 

from .home import home
from .auth.register import register_user
from .auth.logout import logout_user