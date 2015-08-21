from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from mezzanine.core.views import direct_to_template
from nx.views import NoteCreate, NeedCreate

admin.autodiscover()

urlpatterns = i18n_patterns("",
    ("^admin/", include(admin.site.urls)),
)

urlpatterns += patterns('nx.views',
    url("^donate/$",NoteCreate.as_view(success_url="/view/"), name="create"),
    url("^donate/(?P<note_id>\d{1,10})", "note", name="note_detail"),
    url("^search-donates/$", "notes", name="note"),
    url("^need/$",NeedCreate.as_view(success_url="/view/"), name="need"),
    url("^need/(?P<need_id>\d{1,10})", "need", name="need_detail"),
    url("^search-needs/$","search_needs", name="search"),
)

urlpatterns += patterns('',
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    (r'^search/', include('haystack.urls')),
    ("^api/", include("api.urls")),
    ("^", include("mezzanine.urls")),
)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
