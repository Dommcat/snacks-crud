from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.views.generic import TemplateView

'''
Create SnackListView that extends appropriate generic view
associated url path is an empty string
Create SnackDetailView that extends appropriate generic view
associated url path is <int:pk>/
Create SnackCreateView that extends appropriate generic view
associated url path is create/
Create SnackUpdateView that extends appropriate generic view
associated url path is <int:pk>/update/
Create SnackDeleteView that extends appropriate generic view
associated url path is <int:pk>/delete/
Add urls to support all views, with appropriate names
Add templates to support all views
Add navigation links in appropriate locations to access all pages
Make all necessary changes to project level files for project to run
In other words, make it work
'''
# Create your views here.
class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = 'snack_tracking_project'

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack
    context_object_name = 'detail_snack_tracking_project'
    
class SnackCreateView(CreateView):
    model = Snack
    template_name = 'snacks/snack_create.html'
    fields = ['title', 'purchaser', 'description']

class SnackUpdateView(UpdateView):
    model = Snack
    template_name = 'snacks/snack_update.html'
    fields = ['title', 'purchaser', 'description']

class SnackDeleteView(DeleteView):
    model = Snack
    template_name = 'snacks/snack_delete.html'
    success_url = '/'

class AboutPageView(TemplateView):
    template_name = 'about.html'