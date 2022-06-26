from django.urls import include, path
from rest_framework import routers
from .views import LineOfActionSerializerViewSet, DoctorViewSet

router = routers.DefaultRouter()
router.register(r'line-of-actions', LineOfActionSerializerViewSet)
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
