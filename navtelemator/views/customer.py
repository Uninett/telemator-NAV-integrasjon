from django.shortcuts import render
from navtelemator import services
from django.conf import settings


def render_customer(request, customerid):
    customer = services.get_customer_by_id(customerid)
    return render(request,
                  'telemator/customer_info.html',
                  {
                      'customer': customer,
                      'cmdb_orgbyid_url': getattr(settings, 'TM_CMDB_ORGBYID_URL', None),
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
