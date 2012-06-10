from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('JayKanSerachEngine',
    url(r'^$', 'index', name='index'),
)