from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import circuit

urlpatterns = patterns('',
    url(r'^telemator/circuits/', circuit.render_circuits, name='circuit-list'),
    url(r'^telemator/circuits/(?P<circuitid>.+)', circuit.render_circuit, name='circuit-info'),
    url(r'^(?P<roomid>.+)/circuits/', circuit.room_circuits, name='room-info-circuits'),
)
