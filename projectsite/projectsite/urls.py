from django.contrib import admin
from django.urls import path, include
from studentorg.views import HomePageView, OrganizationListView  # Import the OrganizationListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),  # URL for the home page
    path('organizations/', OrganizationListView.as_view(), name='organization-list'),  # URL for organization list
    # You can add other URL patterns as needed
]
