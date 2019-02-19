from django.shortcuts import render
from navtelemator import services
from django.http import JsonResponse, Http404


def render_customer_circuits(request, customerid):
    try:
        customer = services.get_customer_by_id(customerid)
        return_list = []
        circuits = []
        for circuit in customer.circuits:
            circuits.append(circuit.circuit)
        for circuit in circuits:
            customer_circuits = {}
            customer_circuits["Circuit"] = circuit.Circuit
            customer_circuits["Speed"] = circuit.Speed
            customer_circuits["Reference"] = circuit.Reference
            customer_circuits["DtOrdered"] = circuit.DtOrdered
            customer_circuits["DtRdyToUse"] = circuit.DtRdyToUse
            customer_circuits["DtTakeDown"] = circuit.DtTakeDown
            customer_circuits["DtShutDown"] = circuit.DtShutDown
            return_list.append(customer_circuits)
        response = JsonResponse(return_list, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response
    except:
        raise Http404


