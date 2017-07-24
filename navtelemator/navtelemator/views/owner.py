from django.shortcuts import get_object_or_404, render

from navtelemator.models import Owner


def render_owner(request, ownerid):
    owner = get_object_or_404(Owner, owner=ownerid)
    return render(request,
                  'telemator/circuit_info.html',
                  {
                      'owner': owner,
                  }
                  )
