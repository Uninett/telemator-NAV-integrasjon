from django.shortcuts import render
from navtelemator import services
import logging

# writes to spam.log in NAV directory
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

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
    version = services.correct_database_version()
    try:
        netbox = get_start_end_netbox(circuitid)
        return render(request,
                      'telemator/circuit_info.html',
                      {
                          'circuit': circuit,
                          'connections': connections,
                          'routingcables': routingcables,
                          'cables': cables,
                          'version': version,
                          'netbox': netbox,
                      }
                      )
    except:
        return render(request,
                      'telemator/circuit_info.html',
                      {
                          'circuit': circuit,
                          'connections': connections,
                          'routingcables': routingcables,
                          'cables': cables,
                          'version': version,
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

def get_start_end_netbox(circuit):
    start_place = services.get_start_end_place_by_circuit(circuit)[0].split('-GW')[0]
    end_place = services.get_start_end_place_by_circuit(circuit)[1].split('-GW')[0]

    start_netbox = None
    end_netbox = None

    netboxes = services.get_connections_by_circuit(circuit)
    for netbox in netboxes:
        if netbox.Connection.End.split('-GW')[0] == start_place:
            start_netbox = netbox.Port
        if netbox.Connection.End.split('-GW')[0] == end_place:
            end_netbox = netbox.Port
    return start_netbox, end_netbox, start_place, end_place


def abc(num, prpos):
    return "%s%s" % (((num-1)/prpos)+1, chr(((num-1) % prpos) + ord("A")))


def abclist(nums, prpos):
    lastcon = 0
    ret = ""
    for n in nums:
        pos = ((n-1)/prpos)+1
        pin = chr(((n-1) % prpos) + ord("A"))

        if pos != lastcon:
            if lastcon != 0:
                ret += "+"
            ret += "%d" % pos
        lastcon = pos

        if prpos > 1:
            ret += pin
    return ret




def get_sorted_cables_by_circuit(circuit):
    start_place = services.get_start_end_place_by_circuit(circuit)[0].split('-GW')[0]
    end_place = services.get_start_end_place_by_circuit(circuit)[1].split('-GW')[0]

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
        # iterates forward
        for cable in cables:
            port_A = services.get_ports_by_circuit(circuit, cable.cable.Cable, 'A')
            port_B = services.get_ports_by_circuit(circuit, cable.cable.Cable, 'B')
            if cable.cable.End_A == start_location and cable.Cable not in [x.Cable for x in end_list]:
                kabter = services.get_kabter_by_cable(cable, port_A.Core, start_location)
                connector = abclist([(port_A.Core % kabter.NumCores), (port_B.Core % kabter.NumCores)], int(kabter.PinPrPos))
                start_list.append(cable.cable)
                if kabter is not None:
                    if kabter.Plinth is not None:
                        start_locations_list.append([str(cable.cable.End_A), str(cable.cable.End_B), str(len(start_list)),
                                                     str(port_A.Core), str(port_B.Core), str(kabter.Plinth), str(connector)])
                    else:
                        start_locations_list.append(
                            [str(cable.cable.End_B), str(cable.cable.End_A), str(len(start_list)),
                             str(port_A.Core), str(port_B.Core)])
                else:
                    start_locations_list.append([str(cable.cable.End_A), str(cable.cable.End_B), str(len(start_list)),
                                                 str(port_A.Core), str(port_B.Core)])
                start_location = cable.cable.End_B
            elif cable.cable.End_B == start_location and cable.Cable not in [x.Cable for x in end_list]:
                kabter = services.get_kabter_by_cable(cable, port_A.Core, start_location)
                connector = abclist([(port_A.Core % kabter.NumCores), (port_B.Core % kabter.NumCores)],
                                    int(kabter.PinPrPos))
                start_list.append(cable.cable)
                if kabter is not None:
                    if kabter.Plinth is not None:
                        start_locations_list.append([str(cable.cable.End_B), str(cable.cable.End_A), str(len(start_list)),
                                                     str(port_A.Core), str(port_B.Core), str(kabter.Plinth), str(connector)])
                    else:
                        start_locations_list.append(
                            [str(cable.cable.End_B), str(cable.cable.End_A), str(len(start_list)),
                             str(port_A.Core), str(port_B.Core)])
                else:
                    start_locations_list.append([str(cable.cable.End_B), str(cable.cable.End_A), str(len(start_list)),
                                                 str(port_A.Core), str(port_B.Core)])
                start_location = cable.cable.End_A
        # iterates backward
        for cable in cables:
            port_A = services.get_ports_by_circuit(circuit, cable.cable.Cable, 'A')
            port_B = services.get_ports_by_circuit(circuit, cable.cable.Cable, 'B')
            if cable.cable.End_A == end_location and cable.Cable not in [x.Cable for x in start_list]:
                kabter = services.get_kabter_by_cable(cable, port_A.Core, end_location)
                connector = abclist([(port_A.Core % kabter.NumCores), (port_B.Core % kabter.NumCores)],
                                    int(kabter.PinPrPos))
                if kabter is not None:
                    if kabter.Plinth is not None:
                        end_locations_list.insert(0, [str(cable.cable.End_B), str(cable.cable.End_A),
                                                      str(number_of_cables - len(end_list)), str(port_A.Core), str(port_B.Core)
                                                      , str(kabter.Plinth), str(connector)])
                    else:
                        start_locations_list.append(
                            [str(cable.cable.End_B), str(cable.cable.End_A), str(len(start_list)),
                             str(port_A.Core), str(port_B.Core)])
                else:
                    end_locations_list.insert(0, [str(cable.cable.End_B), str(cable.cable.End_A),
                                                  str(number_of_cables - len(end_list)), str(port_A.Core),
                                                  str(port_B.Core)])
                end_list.insert(0, cable.cable)
                end_location = cable.cable.End_B
            elif cable.cable.End_B == end_location and cable.Cable not in [x.Cable for x in start_list]:
                kabter = services.get_kabter_by_cable(cable, port_A.Core, end_location)
                if kabter is not None:
                    connector = abclist([(port_A.Core % kabter.NumCores), (port_B.Core % kabter.NumCores)],
                                        int(kabter.PinPrPos))
                    if kabter.Plinth is not None:
                        end_locations_list.insert(0, [str(cable.cable.End_A), str(cable.cable.End_B),
                                                      str(number_of_cables - len(end_list)), str(port_A.Core), str(port_B.Core)
                                                      , str(kabter.Plinth), str(connector)])
                    else:
                        start_locations_list.append(
                            [str(cable.cable.End_B), str(cable.cable.End_A), str(len(start_list)),
                             str(port_A.Core), str(port_B.Core)])
                else:
                    end_locations_list.insert(0, [str(cable.cable.End_A), str(cable.cable.End_B),
                                                  str(number_of_cables - len(end_list)), str(port_A.Core),
                                                  str(port_B.Core)])
                end_list.insert(0, cable.cable)
                end_location = cable.cable.End_A
        # removes ordered cables from list
        for cable in start_list + end_list:
            for routingcable in cables:
                if routingcable.cable == cable:
                    cables.remove(routingcable)
        counter += 1

        if counter > number_of_cables:
            # makes a list of remaining unordered cables
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





