from django.conf.urls import url

import urlcutsite.views

from django.conf import settings

MIN_LEN, MAX_LEN = settings.SHORT_URL_LENGTH_BOUNDS
 
urlpatterns = [
    # 'urlcutsite.views',
    url(r'^$', urlcutsite.views.index, name='home'),
    url(
        r'^!(?P<short_id>\w{'+str(MIN_LEN)+','+str(MAX_LEN)+'})$',
        urlcutsite.views.show_stats, name='showstats'
    ),
    url(
        r'^(?P<short_id>\w{'+str(MIN_LEN)+','+str(MAX_LEN)+'})$',
        urlcutsite.views.redirect_original, name='redirectoriginal'
    ),
    url(r'^makeshort/$', urlcutsite.views.shorten_url, name='shortenurl'),
]