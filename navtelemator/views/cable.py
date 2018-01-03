from django.shortcuts import render
from navtelemator import services


def render_cable(request, cableid):
    cable = services.get_cable_by_id(cableid)
    routingcables = services.get_routingcables_by_cable(cableid)
    return render(request,
                  'telemator/cable_info.html',
                  {
                      'cable': cable,
                      'routingcables': routingcables
                  }
                  )

def room_cables(request, roomid):
    cables = services.get_cables_by_end(roomid)
    return render(request,
                  'info/room/roominfo_cables.html',
                  {
                      'cables': cables,
                      'roomid': roomid
                  }
                  )
