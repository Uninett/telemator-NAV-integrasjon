from django.shortcuts import get_object_or_404, render

from navtelemator.models import CircuitDetail, Circuit, CircuitEnd


def room_circuits(request, roomid):
    #room = get_object_or_404(Room, id=roomid)
    circuit_details = CircuitDetail.objects.filter(end=roomid)
    #cables = Cable.objects.all()
    #cables = [{id: "Kabel1"}, {id:"Kabel2"}]
    return render(request,
                  'info/room/roominfo_circuits.html',
                  {
                      'circuit_details': circuit_details
                  }
                  )


def render_circuit(request, circuitid):
    circuit = get_object_or_404(Circuit, name=circuitid)
    circuit_details = CircuitDetail.objects.filter(circuit=circuitid)
    return render(request,
                  'telemator/circuit_info.html',
                  {
                      'circuit': circuit,
                      'circuit_details': circuit_details
                  }
                  )


def render_circuits(request):
    circuit_ends = CircuitEnd.objects.all()
    circuits = Circuit.objects.all()
#    result = {}
#    for circuit in circuits:
#        result[circuit] = []
#    for circuit_end in circuit_ends:
#        if circuit_end['parallel'] == 1:
#            result[circuit_end['circuit']][0] = circuit_end['end']
#        elif circuit_end['parallel'] == 2:
#            result[circuit_end['circuit']][1] = circuit_end['end']
    return render(request,
                  'telemator/circuit_list.html',
                  {
                      'circuits': circuits
                  }
                  )
