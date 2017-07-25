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
from navtelemator.models import Circuit, Cable


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
    """Searchprovider for circuits"""
    name = "Circuits"
    headers = [
        ('Circuit', 'name'),
        ('Alias', 'alias')
    ]
    link = 'Circuit'

    def fetch_results(self):
        results = Circuit.objects.filter(
            Q(alias__icontains=self.query) |
            Q(name__icontains=self.query) )
        for result in results:
            self.results.append(SearchResult(
                reverse('circuit-info', kwargs={'circuitid': result.id}),
                result)
            )

class CableSearchProvider(SearchProvider):
    """Searchprovider for circuits"""
    name = "Cables"
    headers = [
        ('Cable', 'name'),
        ('End A', 'end_a'),
        ('End B', 'end_b')
    ]
    link = 'Cable'

    def fetch_results(self):
        results = Cable.objects.filter(
            Q(name__icontains=self.query) |
            Q(end_a__name__icontains=self.query) |
            Q(end_b__name__icontains=self.query))

        for result in results:
            self.results.append(SearchResult(
                reverse('circuit-info', kwargs={'circuitid': result.id}),
                result)
            )
