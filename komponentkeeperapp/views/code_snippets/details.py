import sqlite3
from django.shortcuts import render, redirect, reverse
from komponentkeeperapp.models import CodeSnippet
from django.contrib.auth.decorators import login_required
# from ...forms import AddComponentForm

def get_snippet(code_snippet_id):
    print('\n ID ++++++++', code_snippet_id)
    return CodeSnippet.objects.get(pk=code_snippet_id)
    pass

@login_required
def snippet_details(request, code_snippet_id):
    if request.method == 'GET':
        snippet = get_snippet(code_snippet_id)
        template = 'code_snippets/details.html'
        context = {
            'snippet': snippet
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # if the POST request is for editing a book...
        if ( "actual_method" in form_data and form_data["actual_method"] == "PUT" ):

            # get a the snippet to edit
            snippet_to_edit = CodeSnippet.objects.get(pk=code_snippet_id)

            # store the values to edit
            snippet_to_edit.language = form_data['language']
            snippet_to_edit.description = form_data['description']
            snippet_to_edit.snippet = form_data['snippet']

            # and save the changes to the database
            snippet_to_edit.save()

            return redirect(reverse('komponentkeeperapp:snippets'))

        # if the POST is a DELETE request...
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
                
            snippet = CodeSnippet.objects.get(pk=code_snippet_id)
            snippet.delete()

            return redirect(reverse('komponentkeeperapp:snippets'))