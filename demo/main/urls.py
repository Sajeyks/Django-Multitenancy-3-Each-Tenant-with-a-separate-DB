from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import customerViewSet, rocketViewSet, payloadViewSet, launchViewSet
from .views import api_root

router = DefaultRouter()

router.register(r'customer', customerViewSet, basename='customer')
router.register(r'rocket', rocketViewSet, basename='rocket')
router.register(r'payload', payloadViewSet, basename='payload')
router.register(r'launch', launchViewSet, basename='launch')


urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
 ]