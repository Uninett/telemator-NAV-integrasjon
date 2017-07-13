# nav-telemator

Contribution for Telemator additions in NAV

## Local files

The following needs to be added to the settings and urls, preferedly in their respective local files.

`etc/python/local_settings.py`

    LOCAL_SETTINGS = True
    from nav.django.settings import *

    TEMPLATE_LOADERS = (
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.filesystem.Loader'
    )

    INSTALLED_APPS += (
        'navtelemator',
    )

`etc/python/local_urls.py`

    from django.conf.urls import url, patterns
    import navtelemator
    urlpatterns = patterns(
        '',
        (r'^telemator/', include('navtelemator.urls')),
    )

### Build

`python ./setup.py build sdist`

### Install

`pip install dist/*`

### Uninstall

`pip uninstall nav-contrib-telemator`
