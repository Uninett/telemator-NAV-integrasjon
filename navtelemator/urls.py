from django.conf.urls import patterns, url
from views import circuit, owner, cable, customer

urlpatterns = patterns('',
                       url(r'^cables/(?P<cableid>.+)', cable.render_cable, name='cable-info'),
                       url(r'^circuits/(?P<circuitid>.+)', circuit.render_circuit, name='circuit-info'),
                       url(r'^circuits/', circuit.render_circuits, name='circuit-list'),
                       url(r'^customers/(?P<customerid>.+)', customer.render_customer, name='customer-info'),
                       url(r'^ipdevinfo/(?P<netbox_sysname>.+)/circuits/', circuit.netbox_circuits,
                           name='netbox-info-circuits'),
                       url(r'^owners/(?P<ownerid>.+)', owner.render_owner, name='owner-info'),
                       url(r'^rooms/(?P<roomid>.+)/circuits/', circuit.room_circuits, name='room-info-circuits'),
                       url(r'^rooms/(?P<roomid>.+)/cables/', cable.room_cables, name='room-info-cables'),
                       )
