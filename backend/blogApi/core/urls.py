from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core.settings import MEDIA_ROOT, MEDIA_URL, DEBUG

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/posts/", include("posts.urls")),
    
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
