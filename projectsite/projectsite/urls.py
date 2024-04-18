from django.contrib import admin
from django.urls import path
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView
OrganizationUpdateViews

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'),  
    path('organization_list/<pk>',OrganizationUpdateView.as_view(), name='organization-update'),

]
