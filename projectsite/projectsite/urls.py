from django.contrib import admin
from django.urls import path
from studentorg.views import (
    HomePageView,
    OrganizationCreateView,
    OrganizationListView,
    OrganizationUpdateView,
    OrganizationDeleteView  # Added import for OrganizationDeleteView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('organization_list/', OrganizationListView.as_view(), name='organization-list'),  # Added trailing slash
    path('organization_list/add/', OrganizationCreateView.as_view(), name='organization-add'),  
    path('organization_list/<int:pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),  # Added trailing slash and name
]
