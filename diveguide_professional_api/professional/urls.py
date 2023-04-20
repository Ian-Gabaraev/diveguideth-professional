from django.urls import path

from . import views

app_name = "professionals"

urlpatterns = [
    path(
        "pro/<int:pro_pk>/reviews/",
        views.ProfessionalReviewsView.as_view(),
        name="reviews",
    ),
    path("pro/<int:pk>/", views.ProfessionalDetailView.as_view(), name="professional"),
    path("pro/", views.ProfessionalCreateView.as_view(), name="create_pro"),
    path(
        "pro/<int:pk>/active/",
        views.ProfessionalActiveUpdateView.as_view(),
        name="toggle_active_status",
    ),
    path(
        "pro/<int:pk>/contact_info/",
        views.ProfessionalContactInfoView.as_view(),
        name="contact_info",
    ),
]
