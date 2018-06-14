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


def render_customer_list(request):
    customers = services.get_customers()
    return render(request,
                  'telemator/customer_list.html',
                  {
                      'customers': customers,
                  }
                  )
