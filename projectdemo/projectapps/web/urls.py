from django.conf.urls import url

from projectapps.web import views


urlpatterns = [
    # Homepage
    url(r'^$', views.home, name='serve_home'),
]
