from django.contrib import admin
from django.urls import path
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView  # Import OrganizationUpdateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('organization_list/add/', OrganizationCreateView.as_view(), name='organization-add'),  
    path('organization_list/<int:pk>/', OrganizationUpdateView.as_view(), name='organization-update'),  # Corrected path
]
