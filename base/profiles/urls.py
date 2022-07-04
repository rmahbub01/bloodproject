from django.urls import path

from .views import (
                    update_profile_view,
                    public_profile_view,
                    self_profile_view,
                    all_profile_view
                    )

urlpatterns = [
    path("update", update_profile_view, name="profile_update"),
    path("me", self_profile_view, name="profile_self"),
    path("profile/<str:id>", public_profile_view, name="profile_public"),
    path("view/all", all_profile_view, name="profile_all"),
]
 