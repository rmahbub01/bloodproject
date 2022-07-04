from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # core
    path("admin/", admin.site.urls),
    
    # 3rd parties
    path("accounts/", include("allauth.urls")),  # allauth

    # local
    path("m/", include("profiles.urls")),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )