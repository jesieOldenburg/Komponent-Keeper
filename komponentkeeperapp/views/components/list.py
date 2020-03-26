import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from komponentkeeperapp.models import Component

@login_required
def components_list(request, pk=None):
    # Check if the request made is a GET request
    if request.method == 'GET':
        pk = None
        # Assign all of the requested items to a variable
        all_components = Component.objects.all()
        
        # Then store each of the requested resource's values in a variable named after the keys in the model
        name = request.GET.get('name')
        creator = request.GET.get('creator')
        image = request.GET.get('image')
        description = request.GET.get('description')
        
        template = 'components/list.html'
        context = {
            'all_components': all_components
        }

        # return the render method passing in request, template and context as params
        return render(request, template, context)
        
        pass
    # elif request.method == 'POST':
    #     form_data = request.POST
        
    #     new_component = Component(
    #         creator_id = request.user.id,
    #         name = form_data['name'],
    #         image = upload_component(request),
    #         description = form_data['description']
    #     )

    #     print(new_component.name)
    #     new_component.save()
    #     return redirect(reverse('komponentkeeperapp:components'))
    
    
    
    
    
    
    
    
    
    
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