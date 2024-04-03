from django.db import router

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, BillViewSet

router = DefaultRouter()
router.register(r'items/', ItemViewSet)
router.register(r'bills/', BillViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

