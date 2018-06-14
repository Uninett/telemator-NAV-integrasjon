from django.shortcuts import render
from navtelemator import services
from django.http import JsonResponse, Http404


def render_customer_capacity(request, customerid):
    try:
        customer = services.get_customer_by_id(customerid)
        circuit_capacity = {}
        circuits = []
        for circuit in customer.circuits:
            circuits.append(circuit.circuit)
        for circuit in circuits:
            circuit_capacity[circuit.Circuit] = circuit.Speed
        return JsonResponse(circuit_capacity)
    except:
        raise Http404


