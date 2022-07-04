import imp
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.core_api.api.viewsets import StudentViewSet
from apps.core_api import views

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('docs/', views.documentation, name='documentation'),
]
 