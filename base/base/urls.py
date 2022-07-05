from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from profiles.views import all_profile_view


urlpatterns = [
    # core
    path("admin/", admin.site.urls),
    
    # 3rd parties
    path("accounts/", include("allauth.urls")),  # allauth

    # local
    path("", all_profile_view, name="home"),
    path("m/", include("profiles.urls")),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )