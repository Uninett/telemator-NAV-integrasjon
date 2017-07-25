from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from navtelemator.search import CircuitSearchProvider, SearchForm
from nav.web.utils import create_title

# def index(request):
#     # room = get_object_or_404(Room, id=roomid)
#     #circuit_details = CircuitDetail.objects.filter(end=roomid)
#     # cables = Cable.objects.all()
#     # cables = [{id: "Kabel1"}, {id:"Kabel2"}]
#     return render(request,
#                   'telemator/index.html',
#                   {
#                   }
#                   )


def get_path():
    """Get the path for this subsystem"""
    return [('Home', '/'), ('Search', reverse('info-search'))]


def index(request):
    """Main controller"""

    searchproviders = []

    navpath = [('Home', '/'), ('Search', reverse('info-search'))]
    titles = navpath

    if "query" in request.GET:
        form = SearchForm(request.GET, auto_id=False)
        if form.is_valid():
            titles.append(('Search for "%s"' % request.GET["query"],))
            searchproviders = process_form(form)
            if has_only_one_result(searchproviders):
                return HttpResponseRedirect(searchproviders[0].results[0].href)
    else:
        form = SearchForm()

    return render_to_response("info/base.html",
                              {"form": form,
                               "searchproviders": searchproviders,
                               "navpath": navpath,
                               "title": create_title(titles)},
                              context_instance=RequestContext(request))


def process_form(form):
    """Processor for searchform on main page"""
    query = form.cleaned_data['query']

    if not query:
        return []

    searchproviders = [CircuitSearchProvider(query)]
    providers_with_result = has_results(searchproviders)

    return providers_with_result


def has_results(searchproviders):
    """Check if any of the searchproviders has any results"""
    providers_with_result = []
    for searchprovider in searchproviders:
        if searchprovider.results:
            providers_with_result.append(searchprovider)

    return providers_with_result


def has_only_one_result(searchproviders):
    """Check if searchproviders has one and only one result"""
    results = 0
    for provider in searchproviders:
        results += len(provider.results)
    return results == 1
