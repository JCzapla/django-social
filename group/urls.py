from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'group'

urlpatterns = [
    path('', views.ListGroups.as_view(), name = 'all'),
    path('new/', views.CreateGroup.as_view(), name="create"),
    path('post/in/<slug>/', views.SingleGroup.as_view(), name = 'single'),
    path('join/<slug>/', views.JoinGroup.as_view(), name = 'join'),
    path('leave/<slug>/', views.LeaveGroup.as_view(), name = 'leave'),
]
