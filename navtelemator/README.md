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

### Hacks

Because I couldn't get local-files working, I instead added the values to their respective file.

The url include is added on the end of the list with the other includes, and navtelemator was added at the START of the installed apps (it caused a problem when added at the end. Propably because they are loaded in order.
