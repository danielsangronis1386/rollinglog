from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from catalog import views as catalog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')), #directs traffic to catalog app
    path('account/signup/', catalog_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


