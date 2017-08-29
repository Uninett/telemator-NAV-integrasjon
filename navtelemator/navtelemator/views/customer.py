from django.shortcuts import get_object_or_404, render

from navtelemator.models import Customer, CustomerCircuit


def render_customer(request, customerid):
    customer = get_object_or_404(Customer, customer=customerid)
    customer_circuits = CustomerCircuit.objects.filter(customer=customerid)
    return render(request,
                  'telemator/customer_info.html',
                  {
                      'customer': customer,
                      'customer_circuits': customer_circuits
                  }
                  )