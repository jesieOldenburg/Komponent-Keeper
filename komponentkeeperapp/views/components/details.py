import sqlite3
from django.shortcuts import render, redirect, reverse
from komponentkeeperapp.models import Component, CodeSnippet
from django.contrib.auth.decorators import login_required
# from ...forms import AddComponentForm

def get_component(component_id):
    return Component.objects.get(pk=component_id)
    pass

def get_snippet(component_id):
    return CodeSnippet.objects.get(id=component_id)


@login_required
def component_details(request, component_id):
    if request.method == 'GET':
        # get snippet details
        snippet = get_snippet(component_id)
        snippet_language = snippet.snippet_language
        code_snippet = snippet.code_snippet
        description = snippet.description
        # print('SNIPPET============>>>>>', snippet_desc)

        component = get_component(component_id)
        template = 'components/details.html'
        context = {
            'component': component,
            'snippet': snippet
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # if the POST request is for editing a component...
        if ( "actual_method" in form_data and form_data["actual_method"] == "PUT" ):

            # get a the component to edit
            component_to_edit = Component.objects.get(pk=component_id)

            # store the values to edit
            component_to_edit.name = form_data['name']
            component_to_edit.description = form_data['description']
            component_to_edit.image = form_data['image']

            # and save the changes to the database
            component_to_edit.save()

            return redirect(reverse('komponentkeeperapp:components'))

        # if the POST is a DELETE request...
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
                
            component = Component.objects.get(pk=component_id)
            component.delete()

            return redirect(reverse('komponentkeeperapp:components'))