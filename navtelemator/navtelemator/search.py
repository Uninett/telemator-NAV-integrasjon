from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Row, Column, Submit, Field
from django.core.urlresolvers import reverse
from django.db.models import Q, Count
from collections import namedtuple

from IPy import IP

from nav.models.manage import (Room, Netbox, Interface, Vlan,
                               UnrecognizedNeighbor, NetboxGroup)
from nav.util import is_valid_ip
from nav.web.ipdevinfo.views import is_valid_hostname
from nav.web.info.prefix.views import get_query_results as get_prefix_results


class SearchForm(forms.Form):
    """The searchform used for base searches"""
    query = forms.CharField(max_length=100, label='', required=False)

    def __init__(self, *args, **kwargs):
        self.helper = get_formhelper(kwargs.pop('form_action', ''),
                                     kwargs.pop('placeholder', 'Search'))
        super(SearchForm, self).__init__(*args, **kwargs)

    def clean_query(self):
        """Remove whitespace from searchterm"""
        return self.cleaned_data['query'].strip()


def get_formhelper(form_action, placeholder='Search'):
    """Create a default form layout for a search form"""
    helper = FormHelper()
    helper.form_action = form_action
    helper.form_method = 'GET'
    helper.form_class = 'search-form'
    helper.layout = Layout(
        Row(
            Column(Field('query', placeholder=placeholder),
                   css_class='medium-9'),
            Column(Submit('submit', 'Search', css_class='postfix'),
                   css_class='medium-3'),
            css_class='collapse'
        )
    )
    return helper


SearchResult = namedtuple("SearchResult", ['href', 'inst'])


class SearchProvider(object):
    """Searchprovider interface

    name: displayed as table caption
    headers: object attrs to display as headers and cell content
    headertext: text lookup for headers
    link: attr to create a link on
    """
    name = "SearchProvider"
    headers = ['id']
    headertext = {'id': 'Id'}
    link = 'id'

    def __init__(self, query=""):
        self.results = []
        self.query = query
        self.fetch_results()

    def fetch_results(self):
        """ Fetch results for the query """
        pass


class CircuitSearchProvider(SearchProvider):
    """Searchprovider for rooms"""
    name = "Circuits"
    headers = [
        ('Circuit', 'name'),
        ('Alias', 'reference')
    ]
    link = 'Roomid'

    def fetch_results(self):
        results = Room.objects.filter(id__icontains=self.query).order_by("id")
        for result in results:
            self.results.append(SearchResult(
                reverse('room-info', kwargs={'roomid': result.id}),
                result)
            )