from django.shortcuts import render
from navtelemator import services
from django.conf import settings

def render_owner(request, ownerid):
    owner = services.get_owner_by_id(ownerid)
    return render(request,
                  'telemator/owner_info.html',
                  {
                      'owner': owner,
                      'cmdb_orgbyname_url': getattr(settings, 'TM_CMDB_ORGBYNAME_URL', None),
                  }
                  )
