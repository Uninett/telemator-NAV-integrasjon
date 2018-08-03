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

    start_place, end_place, first_netbox, last_netbox = services.get_start_end_place_by_circuit(circuit)

    start_netbox = None
    end_netbox = None

    netboxes = services.get_connections_by_circuit(circuit)

    for netbox in netboxes:
        if netbox.Connection.End == first_netbox.End:
            start_netbox = netbox.Port
        if netbox.Connection.End == last_netbox.End:
            end_netbox = netbox.Port
    return start_netbox, end_netbox, start_place, end_place



def abclist(pins, prpos, initial_port=1):
    lastcon = 0
    ret = ""
    for n in pins:
      pos = ((n-1)/prpos)+1
      pin = chr(((n-1) % prpos) + ord("A"))

      if pos != lastcon:
        if lastcon != 0:
          ret += "+"
        ret += "%d" % (pos+initial_port-1)
      lastcon = pos

      if prpos > 1:
        ret += pin
    return ret


def get_slices(connections):
    """
   Find connections between nodes in the patch
       Returns a list of paths with all paths in it
   """
    # Start with a emptly slice list
    slices = []

    for current in connections:
        # Get list of all slices matching current block
        # Looping trough all objects in all slices and
        #   returns all slice indexes that match
        inslice = []
        for (index, slice) in enumerate(slices):
            for c in slice:
                if current[0] in c or current[1] in c:
                    inslice.append(index)

        if len(inslice) == 0:
            # Slice matching did not find current block in any slices
            # Add it as a new slice
            slices.append([current])

        elif len(inslice) == 1:
            # Slice matching returned ONE element
            # Adding it to the correct slice
            slices[inslice[0]].append(current)

        elif len(inslice) == 2:
            # Slice matching returned TWO elements
            # Wee need to merge both slices and add current element
            slices[inslice[0]].append(current)
            slices[inslice[0]] += slices[inslice[1]]
            del slices[inslice[1]]
        else:
            raise (Exception("Unfindable element in table, this shuld not happen.."))

    return (slices)

def get_startstop_slice(slices, start, stop):
  out = {}
  for (index, slice) in enumerate(slices):
    # Find start slice
    for b in slice:
      if start in b:
        out["start"] = index
      if stop in b:
        out["stop"] = index
  return out


def sort_slices(slices, start, stop):
    """
    Tries to sort slices based on start and stop point

    :param slice:
    :param start:
    :param stop:
    :return:
    """

    if len(slices) > 1:
        s = get_startstop_slice(slices, start, stop)
        out = []

        sliceindexes = list(range(len(slices)))
        if "start" in s:
            startslice = s["start"]

            sliceindexes.remove(startslice)
        else:
            startslice = None

        if "stop" in s:
            stopslice = s["stop"]
            sliceindexes.remove(stopslice)
        else:
            stopslice = None


        if startslice is not None:
            out.append(slices[startslice])

        for i in sliceindexes:
            out.append(slices[i])

        if stopslice is not None:
            out.append(slices[stopslice])

        return out
    return slices

def sort_slice(slice):
    outslice = []
    current_index = 0

    # Add first element into output array
    outslice.append(slice.pop())

    while len(slice):
        # This function runs until slice is empty
        if current_index > len(slice):
            break

        if slice[current_index][0] in outslice[0] or slice[current_index][1] in outslice[0]:
            outslice = [slice[current_index]] + outslice
            del slice[current_index]
            current_index = 0

        elif slice[current_index][0] in outslice[-1] or slice[current_index][1] in outslice[-1]:
            outslice.append(slice[current_index])
            del slice[current_index]
            current_index = 0

        else:
            current_index += 1
    return outslice


# main function. uses the others to output a list containing dicts that django runs through template.
def get_sorted_cables_by_circuit(circuit):
    start_place, end_place, start_netbox, end_netbox = services.get_start_end_place_by_circuit(circuit)
    cables = services.get_routingcables_by_circuit(circuit)

    cabledata = {}
    cablelist = []
    for (index, cable) in enumerate(cables):
        cabledata[index] = cable
        cablelist.append([cable.cable.End_A, cable.cable.End_B, index])
    cableslices = get_slices(cablelist)

    sorted_slices = sort_slices(cableslices, start_place, end_place)

    previous = start_place
    out_list = []
    counter = 0
    for (index, slice2) in enumerate(sorted_slices):

        slice = sort_slice(slice2)

        # slices may need to be reversed
        if start_place not in slice[0] and index == 0:
            slice.reverse()
        if end_place not in slice[-1] and index == len(sorted_slices):
            slice.reverse()

        # finds the correct previous and next ends before running the main for loop
        for cable in slice:
            result_dict = {}
            ends = []
            if cable[0] == previous[1]:
                ends.append(cable[0])
                ends.append(cable[1])
            elif cable[1] == previous[1]:
                ends.append(cable[1])
                ends.append(cable[0])
            elif previous[0] == cable[0]:
                if len(out_list) > 0:
                    out_list[-1]['prev_end'] = previous[1]
                    out_list[-1]['next_end'] = previous[0]
                    ends.append(cable[0])
                    ends.append(cable[1])
            elif previous[0] == cable[1]:
                if len(out_list) > 0:
                    out_list[-1]['prev_end'] = previous[1]
                    out_list[-1]['next_end'] = previous[0]
                    ends.append(cable[1])
                    ends.append(cable[0])
            else:
                ends.append(cable[0])
                ends.append(cable[1])
            previous = cable
            result_dict.update({'prev_end': ends[0], 'next_end': ends[1]})
            out_list.append(result_dict)


        # main for loop
        for (cable_index, cable) in enumerate(slice):
            result_dict = out_list[counter]
            cable_id = cable[2]

            ports = services.get_ports_by_circuit(circuit, cabledata[cable_id].cable.Cable)
            spliced_prev = services.get_spliced(cabledata[cable_id], result_dict['prev_end'])
            spliced_next = services.get_spliced(cabledata[cable_id], result_dict['next_end'])
            kabter_prev = services.get_kabter_by_cable(cabledata[cable_id], ports[0].Core, result_dict['prev_end'])
            kabter_next = services.get_kabter_by_cable(cabledata[cable_id], ports[0].Core, result_dict['next_end'])
            position = len(out_list) + 2
            connector_next = None
            connector_prev = None

            if cable_index == 0:
                result_dict.update({'first_cable': True})
            else:
                result_dict.update({'first_cable': False})

            if index == 0:
                result_dict.update({'first_slice': True})
            else:
                result_dict.update({'first_slice': False})

            try:
                connector_next = abclist([(int(port.Core)- int(kabter_next.FromCore)) + 1 for port in ports], int(kabter_next.PinPrPos),
                                    int(kabter_next.Pos))
            except:
                pass
            try:
                connector_prev = abclist([(int(port.Core) - int(kabter_prev.FromCore)) + 1 for port in ports],
                                         int(kabter_prev.PinPrPos),
                                         int(kabter_prev.Pos))
            except:
                pass

            odf_index_start = None
            odf_index_end = None
            for p in ports:
                try:
                    if odf_index_start is None:
                        odf_index_start = services.get_kabter_by_cable(cabledata[cable_id], p.Core, result_dict['prev_end']).RowKey
                    if odf_index_start != services.get_kabter_by_cable(cabledata[cable_id], p.Core, result_dict['prev_end']).RowKey:
                        connector_prev = 'Error'
                except Exception as e:
                    connector_prev = 'N/A'

                try:
                    if odf_index_end is None:
                        odf_index_end = services.get_kabter_by_cable(cabledata[cable_id], p.Core,
                                                                       result_dict['next_end']).RowKey
                    if odf_index_end != services.get_kabter_by_cable(cabledata[cable_id], p.Core,
                                                                       result_dict['next_end']).RowKey:
                        connector_next = 'Error'

                except Exception as e:
                    connector_next = 'N/A'

            try:
                if kabter_next.Plinth is not None:
                    next_plinth = kabter_next.Plinth
                    next_postype = kabter_next.PosType
                else:
                    next_plinth = 'Tamp'
                    next_postype = ''
            except AttributeError:
                next_plinth = 'Tamp'
                next_postype = ''

            try:
                if kabter_prev.Plinth is not None:
                    prev_plinth = kabter_prev.Plinth
                    prev_postype = kabter_prev.PosType
                else:
                    prev_plinth = 'Tamp'
                    prev_postype = ''
            except AttributeError:
                prev_plinth = 'Tamp'
                prev_postype = ''

            result_dict.update(
                {'spliced_prev': spliced_prev, 'spliced_next': spliced_next,
                 'order': position, 'ports': ports, 'connector_next': connector_next,
                 'connector_prev': connector_prev,
                 'next_odf': next_plinth, 'next_odf_type': next_postype,
                 'prev_odf': prev_plinth, 'prev_odf_type': prev_postype,
                 'cable': cabledata[cable_id].cable})

            out_list[counter].update(result_dict)
            counter += 1

    return out_list





