from django.shortcuts import render
from navtelemator import services


def render_customer(request, customerid):
    customer = services.get_customer_by_id(customerid)
    return render(request,
                  'telemator/customer_info.html',
                  {
                      'customer': customer,
                  }
                  )
