from django.shortcuts import render
from navtelemator import services


def room_circuits(request, roomid):
    circuit_details = services.get_circuit_details_by_room(roomid)
    return render(request,
                  'info/room/roominfo_circuits.html',
                  {
                      'circuit_details': circuit_details
                  }
                  )


def netbox_circuits(request, netbox_sysname):
    circuit_details = services.get_circuit_details_by_netbox(netbox_sysname)
    return render(request,
                  'ipdevinfo/frag-circuits.html',
                  {
                      'circuit_details': circuit_details
                  }
                  )


def render_circuit(request, circuitid):
    circuit = services.get_circuit_by_id(circuitid)
    routingcables = services.get_routingcables_by_circuit(circuitid)
    # circuit_details = CircuitDetail.objects.filter(circuit=circuitid)
    return render(request,
                  'telemator/circuit_info.html',
                  {
                      'circuit': circuit,
                      # 'circuit_details': circuit_details,
                      'routingcables': routingcables,
                  }
                  )


def render_circuits(request):
    circuits = services.get_circuits()
    return render(request,
                  'telemator/circuit_list.html',
                  {
                      'circuits': circuits
                  }
                  )
