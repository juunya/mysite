from django.urls import path
from rest_framework import routers

from todo.views import UserViewSet, EntryViewSet
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user-info', views.user_info, name='user_info'),
    path('top', views.top, name='top'),
    path('test', views.test, name='test'),
]

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)