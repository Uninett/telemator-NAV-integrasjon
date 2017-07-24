from django.shortcuts import render, get_object_or_404

from navtelemator.models import Cable


def render_cable(request, cableid):
    cable = get_object_or_404(Cable, name=cableid)
    return render(request,
                  'telemator/cable_info.html',
                  {
                      'cable': cable,
                  }
                  )
