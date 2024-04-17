from django.contrib import admin
from django.urls import path
from studentorg.views import HomePageView, OrganizationList  # Import OrganizationList

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('organizations/', OrganizationList.as_view(), name='organization-list'),  # Use OrganizationList
    # Other URL patterns
]
