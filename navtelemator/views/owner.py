from django.shortcuts import render
from navtelemator import services


def render_owner(request, ownerid):
    owner = services.get_owner_by_id(ownerid)
    return render(request,
                  'telemator/owner_info.html',
                  {
                      'owner': owner,
                  }
                  )
