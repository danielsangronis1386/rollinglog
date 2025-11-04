from django.contrib import admin
from django.urls import path, include
from catalog import views as catalog_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')), #directs traffic to catalog app
    path('account/signup/', catalog_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]


