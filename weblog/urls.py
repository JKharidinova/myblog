from django.urls import path

from . import views

app_name = 'weblog'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.post_edit, name='edit'),
    path('new/', views.post_edit, name='new'),
]
