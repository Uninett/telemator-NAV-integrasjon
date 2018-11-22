from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Row, Column, Submit, Field
from django.core.urlresolvers import reverse
from collections import namedtuple
from navtelemator.models import Circuit, Cable, Owner, End
from navtelemator import services
from sqlalchemy import or_
from sqlalchemy import exc


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


class CableSearchProvider(SearchProvider):
    """Searchprovider for cables"""
    name = "Cables"
    headers = [
        ('Cable', 'Cable'),
        ('End A', 'End_A'),
        ('End B', 'End_B')
    ]
    link = 'Cable'

    def fetch_results(self):
        try:
            results = services.session.query(Cable).filter(
                or_(Cable.Cable.ilike(u'%{}%'.format(self.query)), Cable.End_A.ilike(u'%{}%'.format(self.query)),
                    Cable.End_B.ilike(u'%{}%'.format(self.query))))

            for result in results:
                self.results.append(SearchResult(
                    reverse('cable-info', kwargs={'cableid': result.Cable}),
                    result)
                )
        except exc.OperationalError:
            return None


class CircuitSearchProvider(SearchProvider):
    """Searchprovider for circuits"""
    name = "Circuits"
    headers = [
        ('Circuit', 'Circuit'),
        ('Alias', 'Reference')
    ]
    link = 'Circuit'

    def fetch_results(self):
        try:
            results = services.session.query(Circuit).filter(
                or_(Circuit.Circuit.ilike(u'%{}%'.format(self.query)), Circuit.Reference.ilike(u'%{}%'.format(self.query)),
                    Circuit.Owner.ilike(u'%{}%'.format(self.query))))
            for result in results:
                self.results.append(SearchResult(
                    reverse('circuit-info', kwargs={'circuitid': result.Circuit}),
                    result)
                )
        except exc.OperationalError:
            return None


class CWDMSearchProvider(SearchProvider):
    """Searchprovider for circuits"""
    name = "CWDM"
    headers = [
        ('Netbox', 'End'),
        ('Alias', 'Reference')
    ]
    link = 'Netbox'

    def fetch_results(self):
        try:
            results = services.session.query(End).filter(End.End.ilike(u'%{}%'.format(self.query)))
            for result in results:
                self.results.append(SearchResult(
                    reverse('telemator-netbox-info', kwargs={'netbox_sysname': result.End}),
                    result)
                )
        except exc.OperationalError:
            return None


class OwnerSearchProvider(SearchProvider):
    """Searchprovider for owners"""
    name = "Owners"
    headers = [
        ('Owner', 'Name'),
        ('ID', 'Owner')
    ]
    link = 'Owner'

    def fetch_results(self):
        try:
            results = services.session.query(Owner).filter(
                or_(Owner.Owner.ilike(u'%{}%'.format(self.query)), Owner.Name.ilike(u'%{}%'.format(self.query))))

            for result in results:
                self.results.append(SearchResult(
                    reverse('owner-info', kwargs={'ownerid': result.Owner}),
                    result)
                )
        except exc.OperationalError:
            return None
