


from django.urls import path,include
from rest_framework import routers
from .views import mainaiViewSet


router = routers.DefaultRouter()
router.register(r'mainai', mainaiViewSet)

urlpatterns = [
    path('', include(router.urls))
]
