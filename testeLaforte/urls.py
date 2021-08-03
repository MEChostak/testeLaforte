from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from tracking.views import TrackingViewSet

router = DefaultRouter()
router.register(r'tracking', TrackingViewSet, basename='tracking')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    re_path(r'^$', RedirectView.as_view(
        url=reverse_lazy('api-root'), permanent=False)),

]
