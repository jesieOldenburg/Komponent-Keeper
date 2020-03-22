import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from komponentkeeperapp.models import CodeSnippet


def get_snippets():
    all_snippets = CodeSnippet.objects.all()

@login_required
def snippet_form(request):
    if request.method == 'GET':
        snippets = get_snippets()
        template = 'code_snippets/form.html'
        context = {
            'all_snippets': snippets
        }

        return render(request, template, context)
      
@login_required
def edit_snippet_form(request, code_snippet_id):

    if request.method == 'GET':
        component = get_component(component_id)

        template = 'components/form.html'
        context = {
            'component': component,
        }

        return render(request, template, context)