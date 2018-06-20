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
    connections = services.get_connections_by_circuit(circuitid)
    routingcables = services.get_routingcables_by_circuit(circuitid)
    cables = get_sorted_cables_by_circuit(circuitid)
    return render(request,
                  'telemator/circuit_info.html',
                  {
                      'circuit': circuit,
                      # 'circuit_details': circuit_details,
                      'connections': connections,
                      'routingcables': routingcables,
                      'cables': cables,
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


def get_sorted_cables_by_circuit(circuit):
    start_place = services.get_start_end_place_by_circuit(circuit)[0]
    end_place = services.get_start_end_place_by_circuit(circuit)[1]

    cables = services.get_routingcables_by_circuit(circuit)
    number_of_cables = len(cables)
    result = []
    start_end_order = []

    start_list = []
    start_locations_list = []

    end_list = []
    end_locations_list = []

    remainder_list = []
    remainder_locations_list = []

    start_location = start_place
    end_location = end_place
    counter = 0

    while True:
        for cable in cables:
            port_A = services.get_ports_by_circuit(circuit, cable.cable.Cable, 'A')
            port_B = services.get_ports_by_circuit(circuit, cable.cable.Cable, 'B')
            if cable.cable.End_A == start_location and cable.Cable not in [x.Cable for x in end_list]:
                start_list.append(cable.cable)
                start_locations_list.append([str(cable.cable.End_A), str(cable.cable.End_B), str(len(start_list)),
                                             str(port_A.Core), str(port_B.Core)])
                start_location = cable.cable.End_B
            elif cable.cable.End_B == start_location and cable.Cable not in [x.Cable for x in end_list]:
                start_list.append(cable.cable)
                start_locations_list.append([str(cable.cable.End_B), str(cable.cable.End_A), str(len(start_list)),
                                             str(port_A.Core), str(port_B.Core)])
                start_location = cable.cable.End_A
        for cable in cables:
            port_A = services.get_ports_by_circuit(circuit, cable.cable.Cable, 'A')
            port_B = services.get_ports_by_circuit(circuit, cable.cable.Cable, 'B')
            if cable.cable.End_A == end_location and cable.Cable not in [x.Cable for x in start_list]:
                end_locations_list.insert(0, [str(cable.cable.End_B), str(cable.cable.End_A),
                                              str(number_of_cables - len(end_list)), str(port_A.Core), str(port_B.Core)])
                end_list.insert(0, cable.cable)
                end_location = cable.cable.End_B
            elif cable.cable.End_B == end_location and cable.Cable not in [x.Cable for x in start_list]:
                end_locations_list.insert(0, [str(cable.cable.End_A), str(cable.cable.End_B),
                                              str(number_of_cables - len(end_list)), str(port_A.Core), str(port_B.Core)])
                end_list.insert(0, cable.cable)
                end_location = cable.cable.End_A

        for cable in start_list + end_list:
            for routingcable in cables:
                if routingcable.cable == cable:
                    cables.remove(routingcable)
        counter += 1

        if counter > number_of_cables:
            remaining_cables = [cable.cable for cable in cables]
            for remainder in remaining_cables:
                port_A = services.get_ports_by_circuit(circuit, remainder.Cable, 'A')
                port_B = services.get_ports_by_circuit(circuit, remainder.Cable, 'B')
                remainder_locations_list.append([str(remainder.End_A), str(remainder.End_B), '?',
                                                 str(port_A.Core), str(port_B.Core)])
                # result = start_list + remaining_cables + end_list
            remainder_list = zip(remaining_cables, remainder_locations_list)
            # start_end_order = start_locations_list + remaining_start_end + end_locations_list
            break
        if len(cables) is 0:
            result = start_list + end_list
            start_end_order = start_locations_list + end_locations_list
            break

    result = [zip(start_list, start_locations_list), zip(end_list, end_locations_list), remainder_list]
    return result

