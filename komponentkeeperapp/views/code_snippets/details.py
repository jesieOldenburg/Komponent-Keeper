import sqlite3
from django.shortcuts import render, redirect, reverse
from komponentkeeperapp.models import CodeSnippet
from django.contrib.auth.decorators import login_required
# from ...forms import AddComponentForm

def get_snippet(snippet_id):
    return CodeSnippet.objects.get(pk=snippet_id)
    pass

@login_required
def snippet_details(request, snippet_id):
    if request.method == 'GET':
        snippet = get_snippet(snippet_id)
        template = 'code_snippets/details.html'
        context = {
            'snippet': snippet
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # if the POST request is for editing a snippet...
        if ( "actual_method" in form_data and form_data["actual_method"] == "PUT" ):

            # get a the snippet to edit
            snippet_to_edit = CodeSnippet.objects.get(pk=snippet_id)

            # store the values to edit
            snippet_to_edit.snippet_language = form_data['snippet-language']
            snippet_to_edit.description = form_data['description']
            snippet_to_edit.code_snippet = form_data['snippet-input']

            # and save the changes to the database
            snippet_to_edit.save()

            return redirect(reverse('komponentkeeperapp:components'))

        # if the POST is a DELETE request...
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
                
            snippet = CodeSnippet.objects.get(pk=snippet_id)
            snippet.delete()

            return redirect(reverse('komponentkeeperapp:components'))