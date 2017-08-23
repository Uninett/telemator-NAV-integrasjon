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
