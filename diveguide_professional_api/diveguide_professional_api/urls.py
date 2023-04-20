from django.contrib import admin
from django.urls import include, path, re_path

admin.site.site_header = "DiveGuide@Thailand Professionals Database"

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^api/", include("professional.urls", namespace="professionals")),
]
