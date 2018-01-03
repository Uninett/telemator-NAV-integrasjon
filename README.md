# Usage

To simplify installing and running this, I have made a installer-script in telemator-export.
This assumes a built package of navtelemator is available in a `dist` folder and that the db-settings has been entered correctly.
It also assumes that it is being run on a debian based distro, with superuser privileges (for package installation).

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
        'navtelemator.search.CircuitSearchProvider',
        'navtelemator.search.CableSearchProvider',
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

To both install and extract the data from Telemator, copy
telemator_export to your nav-installation, and the dist-folder from
the build process inside it.  Then, edit db.py to have the correct
values for both databases (NAV in docker uses postgres as hostname)
and run install.sh which will both install necessary packages, and
export and import the telemator data

Remember to update the version number, or else `pip` will not do
anything. You can also do

`pip -v install --upgrade dist/*`

to **force** the upgrade

### Uninstall

`pip uninstall nav-contrib-telemator`


### Hacks

Because I couldn't get local-files working, I instead added the values to their respective file.

The url include is added on the end of the list with the other includes, and navtelemator was added at the START of the installed apps (it caused a problem when added at the end. Propably because they are loaded in order.

# telemator-export

Script for exporting data from telemator and inserting it into another database.

## Issues

Sometimes it returns a KeyError. This is most like because of a race condiction or such, as often the next try will run just fine.

## Choices made along the way

One of the largest decision I made when writing the export script was to use pandas, a library for data processing, instead of an ordinary SQL and/or ORM library.
This was deemed necessary when SQLAlchemy began complaining about collation in the database. For those of you who don't know, collation is what kind of sorting to use in the database.
MS SQL has no collation in common with postgres, and I found no way to address the issue when searching for a solution. Luckily for me, using pandas was not an unwise choice.
It allows me to not worry about the SQL-specifics, as pandas chooses the appropiate field settings by looking at the data it extracted from Telemator.
One issue with using pandas is that the version in debian repositories is really old, so I need to build it in the docker container. This takes an absurdly long time, probably because of numpy.
Expect to wait 5-10 minutes at least for it to build. This can luckily be dealt with when our docker container upgrades it debian version.
