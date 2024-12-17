from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from salesitems.views import SalesItemViewSet

router=routers.DefaultRouter(trailing_slash=False)
router.register('sales-items',SalesItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
