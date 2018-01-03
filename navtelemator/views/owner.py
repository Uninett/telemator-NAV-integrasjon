from django.shortcuts import get_object_or_404, render

from navtelemator.models import Owner
from navtelemator import services


def render_owner(request, ownerid):
    #owner = get_object_or_404(Owner, owner=ownerid)
    owner = services.get_owner_by_id(ownerid)
    return render(request,
                  'telemator/owner_info.html',
                  {
                      'owner': owner,
                  }
                  )
