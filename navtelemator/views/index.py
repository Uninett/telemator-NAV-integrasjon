from django.shortcuts import render
from navtelemator import services


def render_index(request):
    total_circuits = services.get_circuit_amount()
    total_customers = services.get_customer_amount()
    return render(request,
                  'telemator/index_info.html',
                  {
                      'total_circuits': total_circuits,
                      'total_customers': total_customers
                  }
                  )

