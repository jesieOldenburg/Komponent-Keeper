import sqlite3
from django.shortcuts import render, redirect, reverse
from komponentkeeperapp.models import Component
# from ...forms import AddComponentForm
# from django.contrib.auth.decorators import login_required

def components_list(request):
    # Check if the request made is a GET request
    if request.method == 'GET':
        # Assign all of the requested items to a variable
        all_components = Component.objects.all()
        
        # Then store each of the requested resource's values in a variable named after the keys in the model
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