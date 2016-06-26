from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.contrib.wagtailapi import urls as wagtailapi_urls

# from projectapps.web import urls as web_urls


urlpatterns = [
    # url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^api/', include(wagtailapi_urls)),

    #  url(r'^admin/dev/', include(coredev_urls)),
    #  url(r'^core/', include(core_urls)),

    #  # Taskss
    #  url(r'^_cron/', include(task_urls)),

    #  # sitemap and robots
    #  url('^sitemap\.xml$', sitemap, name='sitemap'),
    #  url('^robots\.txt$', robots, name='robots'),
    #  url('^404/$', page_not_found, name='404'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    url(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    # Serve static files on debug mode
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

    # Add support for hardcoded urls (/static/core/img/myimage.png)
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns += patterns('',
            url(r'^__debug__/', include(debug_toolbar.urls)),
        )
