from django.shortcuts import render, get_object_or_404

from navtelemator.models import Cable, RoutingCable


def render_cable(request, cableid):
    cable = get_object_or_404(Cable, name=cableid)
    routingcables = RoutingCable.objects.filter(cable=cableid) & RoutingCable.objects.filter(core=1)
    return render(request,
                  'telemator/cable_info.html',
                  {
                      'cable': cable,
                      'routingcables': routingcables
                  }
                  )

def room_cables(request, roomid):
    #room = get_object_or_404(Room, id=roomid)
    cables = Cable.objects.filter(end_a=roomid) | Cable.objects.filter(end_b=roomid)
    #cables = Cable.objects.all()
    #cables = [{id: "Kabel1"}, {id:"Kabel2"}]
    return render(request,
                  'info/room/roominfo_cables.html',
                  {
                      'cables': cables,
                      'roomid': roomid
                  }
                  )
