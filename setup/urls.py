"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tarefa.views import TarefaViewSet, TagViewSet, CommentViewSets, NotificationViewSets, ListCommentsViewSets, ListTagViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Tarefa', TarefaViewSet, basename='Tarefa')
router.register('Tag', TagViewSet, basename='Tag')
router.register('Comment', CommentViewSets, basename='Comment')
router.register('Notification', NotificationViewSets, basename='Notification')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
    path('task/<int:pk>/comments/', ListCommentsViewSets.as_view()),
    path('task/<int:pk>/tags/', ListTagViewSets.as_view()),
    # path('tag/', TagViewSet.as_view({'get': 'list'}), name='tags'),
    # path('comment', CommentViewSets.as_view({'get': 'list'}), name='comments'),
    # path('notification', NotificationViewSets.as_view({'get': 'list'}), name='notifications'),
   
]
