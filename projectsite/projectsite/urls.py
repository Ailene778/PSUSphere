from django.contrib import admin
from django.urls import path, re_path
from studentorg.views import(
    HomePageView, OrganizationList,
    OrganizationCreateView,
    OrganizationUpdateView,
    OrganizationDeleteView  
)
from django.contrib.auth import view as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('organization_list/', OrganizationList.as_view(), name='organization-list'),  
    path('organization_list/add/', OrganizationCreateView.as_view(), name='organization-add'),  
    path('organization_list/<pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),  
    re_path(r'^login/$', auth_views.LoginView.as_view(), name='logout'),
]
