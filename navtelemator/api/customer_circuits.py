from django.shortcuts import render
from navtelemator import services
from django.http import JsonResponse, Http404


def render_customer_circuits(request, customerid):
    try:
        customer = services.get_customer_by_id(customerid)
        customer_circuits = {}
        circuits = []
        for circuit in customer.circuits:
            circuits.append(circuit.circuit)
        for circuit in circuits:
            customer_circuits[circuit.Circuit] = circuit.Speed
        return JsonResponse(customer_circuits)
    except:
        raise Http404


