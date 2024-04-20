from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization
from studentorg.forms import OrganizationForm
from django.urls import reverse_lazy
from typing import Any
from django.db.model.query import QuerySet
from django.db.models import Q

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    template_name = 'org_list.html'
    context_object_name = 'organization'
    paginate_by=5

    def get_queryset(self,*args, **kwargs):
        qs=super(OrganizationList, self). get_queryset(*args, **kwargs)
        if self.request.GET.get("q") !=None:
            query=self.request.GET.get('q')
            qs= qs.filter(Q(name_icontains=query) | Q(description_icontains=query))

            return qs


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')  
    
class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_update.html'  # Update this with your template name
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')  # Corrected success_url
