from django.conf.urls import patterns, url
from views import index, circuit, owner, cable, customer, netbox
from navtelemator.api import api_index, customer_circuits

urlpatterns = patterns('',
                       url(r'^$', index.render_index, name='index-list'),
                       url(r'^cables/(?P<cableid>.+)', cable.render_cable, name='cable-info'),
                       url(r'^circuits/(?P<circuitid>.+)', circuit.render_circuit, name='circuit-info'),
                       url(r'^circuits/', circuit.render_circuits, name='circuit-list'),
                       url(r'^customers/(?P<customerid>.+)', customer.render_customer, name='customer-info'),
                       url(r'^customers/$', customer.render_customer_list, name='customer-list'),
                       url(r'^api/$', api_index.render_api_index, name='api-index'),
                       url(r'^api/1.0/customer_circuits/(?P<customerid>.+)', customer_circuits.render_customer_circuits,
                           name='customer-capacity'),
                       url(r'^ipdevinfo/(?P<netbox_sysname>.+)/circuits/', circuit.netbox_circuits,
                           name='netbox-info-circuits'),
                       url(r'^ipdevinfo/(?P<netbox_sysname>.+)', netbox.render_netbox,
                           name='telemator-netbox-info'),
                       url(r'^owners/(?P<ownerid>.+)', owner.render_owner, name='owner-info'),
                       url(r'^rooms/(?P<roomid>.+)/circuits/', circuit.room_circuits, name='room-info-circuits'),
                       url(r'^rooms/(?P<roomid>.+)/cables/', cable.room_cables, name='room-info-cables'),
                       )
