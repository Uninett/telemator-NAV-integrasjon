from django.shortcuts import render
from navtelemator import services


def render_netbox(request, netbox_sysname):
    circuit_details = services.get_circuit_details_by_netbox(netbox_sysname)
    netbox = services.get_end_by_id(netbox_sysname)
    return render(request,
                  'telemator/netbox_info.html',
                  {
                      'circuit_details': circuit_details,
                      'netbox': netbox,
                  }
                  )