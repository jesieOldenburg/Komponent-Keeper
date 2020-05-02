import sqlite3
from django.shortcuts import render, redirect, reverse
from komponentkeeperapp.models import CodeSnippet, Component
from django.contrib.auth.decorators import login_required
# from ...forms import AddComponentForm

@login_required
def snippets_list(request, component_id):
    # Check if the request made is a GET request
    if request.method == 'GET':
        # Assign all of the requested items to a variable
        all_snippets = CodeSnippet.objects.all()
        # Then store each of the requested resource's values in a variable named after the keys in the model
        creator = request.GET.get('creator')
        snippet = request.GET.get('code_snippet')
        # print(CodeSnippet.objects.all())
        description = request.GET.get('description')
        snippet_lang = request.GET.get('snippet_language')

        template = 'code_snippets/list.html'
        context = {
            'all_snippets': all_snippets,
        }

        # return the render method passing in request, template and context as params
        return render(request, template, context)
        
    # Create a New Snippet
    elif request.method == 'POST':
        print('WE __________-------______ POSTED +++++---------___________-----______')
        form_data = request.POST
        component_to_link = Component.objects.get(pk=component_id)
        component_URL_id = component_to_link.id
        new_snippet = CodeSnippet(
            creator_id = request.user.id,
            component_id = component_to_link.id,
            snippet_language = form_data['snippet-language'],
            code_snippet = form_data['snippet-input'],
            description = form_data['description']
        )

        new_snippet.save()
        return redirect(reverse('komponentkeeperapp:component', kwargs={'component_id': component_URL_id})) # TODO: make this redirect to component detail view to see the newly added snippet.
    
# def component_image_upload(request):
#     # Post an image to the database
#     if request.method == 'POST':
#         # Create a new instance of the component form and pass the posted values, including the files to it.
#         form = AddComponentForm(request.POST, request.FILES)
        
#         # If the form fields are validated
#         if form.is_valid(): 
#             # Save the form to the db
#             form.save() 
#             # And redirect the user to the landing
#             return redirect('success') 
        
#     else:
#         form = AddComponentForm()
#         pass
#     return render(request, 'components:form.html', {'form': form})


# def success(request): 
#     return HttpResponse('successfully uploaded') 