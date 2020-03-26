import sqlite3
from django.shortcuts import render, redirect, reverse
from komponentkeeperapp.models import Component, CodeSnippet
from django.contrib.auth.decorators import login_required
# from ..code_snippets.form import snippet_form

def get_component(component_id):
    return Component.objects.get(pk=component_id)
    pass

def get_snippet(component_id):
    if CodeSnippet.objects.filter(component=component_id).exists(): # This evaluates to True
        return CodeSnippet.objects.filter(component=component_id) # And this returns
    else:
        return None

@login_required
def component_details(request, component_id):
    if request.method == 'GET':
        snippet_assigned = None
        snippet_assigned = get_snippet(component_id)
        if snippet_assigned is not None and component_id:
            snippet = get_snippet(component_id)
            # get snippet details
            for s in snippet:
                snippet_language = s.snippet_language
                print(snippet_language)
                code_snippet = s.code_snippet
                description = s.description

            component = get_component(component_id)
            template = 'components/details.html'
            context = {
                'snippet': snippet,
                'component': component
            }
            return render(request, template, context)
        
        elif snippet_assigned == None and component_id:
            print("No render context for you")
            component = get_component(component_id)
            template = 'components/details.html'
            context = {
                'component': component
            }
            return render(request, template, context)

    elif request.method == 'POST':
        print('*******************^^^^^^^^^^^^^^^^^************POST in component details')
        pass
        form_data = request.POST

        # # if the POST request is for editing a component...
        # if ( "actual_method" in form_data and form_data["actual_method"] == "PUT" ):
            
        #     snippet_to_add = CodeSnippet.objects.create(
        #         component_id = Component.objects.get(pk=component_id),
        #         snippet_language = form_data.get('snippet_language'),
        #         code_snippet = form_data.get('code_snippet'),
        #         description = form_data.get('description')
        #     )
        #     # get a the component to edit
        #     # component_to_edit = Component.objects.get(pk=component_id)

        #     # # store the values to edit
        #     # component_to_edit.name = form_data['name']
        #     # component_to_edit.description = form_data['description']
        #     # component_to_edit.image = form_data['image']

        #     # # and save the changes to the database
        #     # component_to_edit.save()

        #     return redirect(reverse('komponentkeeperapp:snippet_form'))

        # if the POST is a DELETE request...
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
                
            component = Component.objects.get(pk=component_id)
            component.delete()

            return redirect(reverse('komponentkeeperapp:components'))