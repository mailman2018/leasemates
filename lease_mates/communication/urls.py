from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, AnnouncementViewSet


#create router for default router (standard endpoints)
router = DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'announcements', AnnouncementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
