# nav-telemator

Contribution for Telemator additions in NAV

## Local files

The following needs to be added to the settings and urls, preferedly in their respective local files.

`/etc/nav/python/local_settings.py`

    LOCAL_SETTINGS = True
    from nav.django.settings import *

    TEMPLATE_LOADERS = (
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.filesystem.Loader'
    )

    INSTALLED_APPS += (
        'navtelemator',
    )
        
    # Telemator search providers
    SEARCHPROVIDERS += (
        'navtelemator.search.CableSearchProvider',
        'navtelemator.search.CircuitSearchProvider',
        'navtelemator.search.CWDMSearchProvider',
        'navtelemator.search.OwnerSearchProvider',
    )

    ### Telemator Config ###
    # Server to connect to
    TM_HOST = ''
    # Port number
    TM_PORT = '1433'

    # Username
    TM_USER = ''
    # Password
    TM_PASSWORD = ''

    # Name of database to use
    TM_DBNAME = ''


`/etc/nav/python/local_urls.py`

    from django.conf.urls import url, patterns, include
    import navtelemator
    urlpatterns = patterns(
        '',
        (r'^telemator/', include('navtelemator.urls')),
    )

### Build

`python ./setup.py build sdist`

### Install

`pip install dist/*`

Remember to update the version number, or else `pip` will not do
anything. You can also do

`pip -v install --upgrade dist/*`

to **force** the upgrade, but this will also upgrade dependencies already installed.

### Uninstall

`pip uninstall nav-contrib-telemator`


### Hacks

Because I couldn't get local-files working, I instead added the values to their respective file.

The url include is added on the end of the list with the other includes, and navtelemator was added at the START of the installed apps (it caused a problem when added at the end. Propably because they are loaded in order.
