from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import circuit, index, owner, cable, customer

urlpatterns = patterns('',
                       url(r'^$', index.index, name="telemator-search"),
                       url(r'^circuits/(?P<circuitid>.+)', circuit.render_circuit, name='circuit-info'),
                       url(r'^circuits/', circuit.render_circuits, name='circuit-list'),
                       url(r'^rooms/(?P<roomid>.+)/circuits/', circuit.room_circuits, name='room-info-circuits'),
                       url(r'^rooms/(?P<roomid>.+)/cables/', cable.room_cables, name='room-info-cables'),
                       url(r'^ipdevinfo/(?P<netbox_sysname>.+)/circuits/', circuit.netbox_circuits, name='netbox-info-circuits'),
                       url(r'^owners/(?P<ownerid>.+)', owner.render_owner, name='owner-info'),
                       url(r'^cables/(?P<cableid>.+)', cable.render_cable, name='cable-info'),
                       url(r'^customers/(?P<customerid>.+)', customer.render_customer, name='customer-info')
                       )
