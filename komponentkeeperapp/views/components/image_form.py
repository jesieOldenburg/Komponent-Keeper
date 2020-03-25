from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from komponentkeeperapp.models import Component, CodeSnippet
from .details import get_snippet, get_component
from ...forms import AddImageForm, EditComponentForm
from django.contrib.auth.decorators import login_required

def success(request): 
    return HttpResponseRedirect(reverse('komponentkeeperapp:components')) 

def edit_success(request, component_id):
    return HttpResponseRedirect(reverse('komponentkeeperapp:component component.id'))

def fail(request):
    return HttpResponseRedirect(reverse('FAILED POST REQUEST'))

def upload_component(request):
    context = {}
    if request.method == 'POST':
        context = {}
        form = AddImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            form_data = request.POST
            component = form.save(commit=False)
            component.creator_id = request.user.id
            component.save()

            new_snippet = CodeSnippet.objects.create(
                component_id = component.id,
                snippet_language = form_data.get('snippet_language'),
                code_snippet = form_data.get('code_snippet'),
                description = form_data.get('description')
            )

            return redirect('komponentkeeperapp:success')
    else:
        form = AddImageForm()
    context['form'] = form
    return render(request, 'components/add_component_form.html', context)

    

# TODO refactor this to make more dry
def edit_component_form(request, component_id):
    # Define the context dictionary globally so conditionals can access
    context = {}
    # Get the instance of the component
    component_to_edit = get_component(component_id)

    # When the user requests the form via a GET request
    if request.method == 'GET':
        # Instantiate the new form, passing in the instance to edit
        form = EditComponentForm(instance=component_to_edit)
        # Assign the edit form instance to the context dictionary
        context['form'] = form
        # Render the form to the user so they can make changes.
        return render(request, 'components/edit_component_form.html', context)

    # When the user hits the submit button on the form after making changes
    if request.method == 'POST':
        # Pass in the user edited data via the resquest.POST param, and any media files via request.FILES (i.e. docs, imgs, etc.) while ensuring the correct instance is being updated
        form = EditComponentForm(request.POST, request.FILES, instance=component_to_edit)
        
        # Ensure form validation is complete and the correct data is being passed back to the server
        if form.is_valid():
            # Save the changes to the database
            form.save()
            # Redirect the user to the success HttpResponse method, which sends 
            return redirect('komponentkeeperapp:edit_success')
    else:
        form = EditComponentForm()
        return fail(request)
    
    context['form'] = form
    return render(request, 'components/edit_component_form.html', context)
