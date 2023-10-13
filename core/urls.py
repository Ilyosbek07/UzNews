from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("news/", include("apps.news.urls")),
    path("user/", include("apps.users.urls")),
    path("common/", include("apps.common.urls")),
    path("interview/", include("apps.interview.urls")),
    path("photo-report/", include("apps.photoreport.urls")),
    path("back-office/", include("apps.back_office.urls")),
    path("review/", include("apps.review.urls")),
]

urlpatterns += swagger_urlpatterns
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
