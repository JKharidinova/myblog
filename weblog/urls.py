from django.urls import path

from . import views

app_name = 'weblog'
urlpatterns = [
    path('', views.BlogsView.as_view(), name='index'),
    path('<pk>/', views.PostsView.as_view(), name='detail'),
    path('new/', views.post_new, name='post_new'),
]
