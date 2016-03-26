from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'^connection', views.ConnectionViewSet)
router.register(r'^node', views.NodeMarkerViewSet)
router.register(r'^nodeMarker', views.NodeMarkerViewSet)
router.register(r'update', views.DBChangeViewSet)
router.register(r'load', views.LoadViewSet)
router.register(r'genSynchronous', views.SyncGenViewSet)
router.register(r'bus', views.BusViewSet)
router.register(r'utility', views.UtilityViewSet)
router.register(r'transformer', views.TwoWindingTransformerViewSet)
router.register(r'direct', views.DirectConnectionViewSet)
router.register(r'cable', views.CableViewSet)
router.register(r'overhead', views.OverheadLineViewSet)
router.register(r'wiredata', views.OverheadLineViewSet)
router.register(r'linecode', views.OverheadLineViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
]
