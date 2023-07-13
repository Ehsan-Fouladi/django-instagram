from django.contrib import admin
from django.urls import include
from django.conf.urls.static import static
from django.contrib.auth.urls import path
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('post/', include('post.urls')),
    path("", include("home.urls")),
    # path('', include('django.contrib.auth.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
