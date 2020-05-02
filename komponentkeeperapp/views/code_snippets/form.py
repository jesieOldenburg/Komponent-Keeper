from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from komponentkeeperapp.models import CodeSnippet, Component
from .details import get_snippet

from django.contrib.auth.decorators import login_required

def get_snippets():
    all_snippets = CodeSnippet.objects.all()

# @login_required
def snippet_form(request, component_id):
    """This View method will retrieve the snippet form for adding, and editing the snippets
    """

    if request.method == 'GET':
        print('COMPONENT ID ::::::::::::::     :::::::::::', component_id)
        # snippets = get_snippets()
        component = Component.objects.get(pk=component_id)
        # components = Component.objects.all()
        template = 'code_snippets/form.html'
        context = {
            # 'all_snippets': snippets,
            'component': component
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        print('TEST ::::::::;;;;;;;;;;:::::::::', component_id)
        new_snippet = CodeSnippet.objects.create(
            component = Component.objects.get(pk=component_id), # ! Changed id to component_id
            snippet_language = form_data.get('snippet_language'),
            code_snippet = form_data.get('code_snippet'),
            description = form_data.get('description')
        )
    return redirect(reverse('komponentkeeperapp:component_details')) # ! redirect back to the component detail

# @login_required
# def edit_snippet_form(request, code_snippet_id):

#     if request.method == 'GET':
#         snippet = get_snippet(code_snippet_id)

#         template = 'code_snippets/form.html'
#         context = {
#             'snippet': snippet,
#         }

#         return render(request, template, context)