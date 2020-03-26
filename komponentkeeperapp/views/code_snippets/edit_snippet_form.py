from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from komponentkeeperapp.models import CodeSnippet
# from .details import get_snippet
from django.contrib.auth.decorators import login_required

def get_snippets():
    all_snippets = CodeSnippet.objects.all()
    
def get_snippet(snippet_id):
    return CodeSnippet.objects.get(pk=snippet_id)
    pass
    
# @login_required
def edit_snippet_form(request, snippet_id):
    """This View method will retrieve the snippet form for adding, and editing the snippets
    """
    if request.method == 'GET':
        print('GET IN NEW MODULE %%%%%%%***********#####')
        snippet = get_snippet(snippet_id)

        template = 'code_snippets/editSnippet.html'
        context = {
            'snippet': snippet,
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        print('TEST ::::::::;;;;;;;;;;:::::::::', snippet_id)
        new_snippet = CodeSnippet.objects.create(
            # component = Component.objects.get(pk=component_id), # ! Changed id to component_id
            snippet_language = form_data.get('snippet_language'),
            code_snippet = form_data.get('code_snippet'),
            description = form_data.get('description')
        )
        print('WE ADDED *****************()()()()()()(')
    return redirect(reverse('komponentkeeperapp:components'))