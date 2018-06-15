from django.shortcuts import render
from navtelemator import services
from django.http import HttpResponse
from sqlalchemy import exc



def render_index(request):
    try:
        total_circuits = services.get_circuit_amount()
        total_customers = services.get_customer_amount()
        return render(request,
                      'telemator/index_info.html',
                      {
                          'total_circuits': total_circuits,
                          'total_customers': total_customers
                      }
                      )
    except exc.OperationalError as e:
        return HttpResponse("Oops! Seems like something went wrong on the database connection. Try checking"
                            " your settings configuration. <br><br><br> Full message:<br>" +
                            e.message)
