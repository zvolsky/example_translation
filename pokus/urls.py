from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path


# this is probably obsolete
# it was used together with path(.., .., js_info_dict, name=..) but this doesn't work now (js is dead)
#   https://code.djangoproject.com/ticket/5494
#   https://stackoverflow.com/questions/1963517/how-to-give-package-names-to-django-javascript-catalog-view
#   https://stackoverflow.com/questions/19625102/django-javascript-translation-not-working
'''
js_info_dict = {
    'domain': 'djangojs',
    'packages': ('pokus1',),  # ('pokus1', 'pokus2')
}
'''

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include(('pokus1.urls', 'pokus1'), namespace='pokus1')),
    path('europe', include(('pokus2.urls', 'pokus2'), namespace='pokus2')),
)
