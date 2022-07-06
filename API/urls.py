from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('todos', views.ToDoViewSet, basename='Todos')

# URLConf
urlpatterns = [
   path('', include(router.urls)),
]