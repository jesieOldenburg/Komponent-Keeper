from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from komponentkeeperapp.models import Component
from .details import get_snippet, get_component
from ...forms import AddImageForm, EditComponentForm

def success(request): 
    return HttpResponseRedirect(reverse('komponentkeeperapp:components')) 

def fail(request):
    return HttpResponseRedirect(reverse('FAILED POST REQUEST'))

def upload_component(request):
    context = {}
    if request.method == 'POST':
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            component = form.save(commit=False)
            component.creator_id = request.user.id
            # * print(request.user.id)
            component.save()
            return redirect('komponentkeeperapp:success')
    else:
        form = AddImageForm()
    context['form'] = form
    return render(request, 'components/add_component_form.html', context)

def edit_component_form(request, component_id):
    context = {}
    # Get the instance of the component
    component_to_edit = get_component(component_id)

    if request.method == 'GET':
        # Instantiate the new form, passing in the instance to edit
        form = EditComponentForm(instance=component_to_edit)
        print('ERORRS FORM ***********$$$$$$$$*******$$$$$$$$******$$$$$$$**$**$**$**$**$*$*', form.errors)
        context['form'] = form
        return render(request, 'components/edit_component_form.html', context)

    if request.method == 'POST':
        form = EditComponentForm(request.POST, instance=component_to_edit)
        if form.is_valid():
            print('we valid homie')
            form = form.save(commit=False)
            form.save()
            context['form'] = form
            return redirect('komponentkeeperapp:success')
            pass
    
    else:
        form = EditComponentForm()
        return fail(request)
    
    context['form'] = form
    return render(request, 'components/edit_component_form.html', context)
