import debug_toolbar
from django.urls import include, path


urlpatterns = [
    path("branches/", include('api.branch.branch_urls')),
    path("__debug__/", include(debug_toolbar.urls)),
]