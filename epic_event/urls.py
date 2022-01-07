"""epic_event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import routers

from client.views import ClientSet
from contract.views import ContractSet
from event.views import EventSet
from team_user.views import TeamSet


def trigger_error(request):
    division_by_zero = 1 / 0


router = routers.DefaultRouter()
router.register(r'team', TeamSet)
router.register(r'client', ClientSet, basename='client')
router.register(r'contract', ContractSet, basename='contract')
router.register(r'event', EventSet, basename='event')

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # Sentry test installation
                  path('sentry-debug/', trigger_error),
                  # API urls
                  path('api-auth/', include('rest_framework.urls')),
                  # Token API JWT
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  # Spectacular urls
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
              ] + router.urls
