from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BotUserViewset,Change,ImageViewset
router = DefaultRouter()
router.register('botuser',BotUserViewset)
router.register('image',ImageViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('change/<str:id>/<str:lang>/',Change.as_view())
]