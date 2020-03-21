import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from komponentkeeperapp.models import Component


def get_components():
    all_components = Component.objects.all()

@login_required
def component_form(request):
    if request.method == 'GET':
        components = get_components()
        template = 'components/form.html'
        context = {
            'all_components': components
        }

        return render(request, template, context)
      
# @login_required
# def edit_component_form(request, component_id):

#     if request.method == 'GET':
#         component = get_component(component_id)

#         template = 'components/form.html'
#         context = {
#             'component': component,
#         }

#         return render(request, template, context)