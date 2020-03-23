from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from komponentkeeperapp.models import Component
from ...forms import AddImageForm

def success(request): 
    return HttpResponseRedirect(reverse('komponentkeeperapp:components')) 

def upload_component(request):
    context = {}
    if request.method == 'POST':
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            component = form.save(commit=False)
            component.creator_id = request.user.id
            print(request.user.id)
            component.save()
            return redirect('komponentkeeperapp:success')
            pass
            # creator_id = Component.objects.get(pk=creator_id)
            # name = form.cleaned_data.get('name')
            # image = form.cleaned_data.get('image')
            # description = form.cleaned_data.get('description')
            # component_to_save = Component.objects.create(
            #     creator_id = creator_id,
            #     name = name,
            #     image = image,
            #     description = description
            # )
            
            # component_to_save.save()
            # print('COMPONENT :::', component_to_save)
    else:
        form = AddImageForm()
    context['form'] = form
    return render(request, 'components/form.html', context)