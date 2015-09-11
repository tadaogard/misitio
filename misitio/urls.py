
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import patterns, include, url
from app.views import * #hello, current_datetime, hours_ahead, ua_display_good2

from django.contrib import admin
admin.autodiscover()

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^search-form/$', search),
    url(r'^Buscar/$', search),
    url(r'^Registrar/$', registrar),
    url(r'^Contactanos/$', contacto),
    url(r'^Contenido/$', contenido),
    url(r'^Registrando/$', registrando),
    url(r'^$',Base),
    url(r'^', include(router.urls)),
   # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^hello/$', hello),
    url(r'^G/$', ua_display_good2),
    url(r'^Login/$', login),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    
    