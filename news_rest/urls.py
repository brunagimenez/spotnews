from django.urls import path, include

from rest_framework import routers
from news_rest.views.category_view import CategoryViewSet
from news_rest.views.user_view import UserViewSet

router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]