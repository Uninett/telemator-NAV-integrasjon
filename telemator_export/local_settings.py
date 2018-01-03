LOCAL_SETTINGS = True
from nav.django.settings import *

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader'
)

INSTALLED_APPS += (
    'navtelemator',
)

SEARCHPROVIDERS += ['navtelemator.search.CircuitSearchProvider',
                       'navtelemator.search.CableSearchProvider',
                       'navtelemator.search.OwnerSearchProvider']

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
