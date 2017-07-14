from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import circuit, telemator

urlpatterns = patterns('',
    url(r'^$', telemator.index, name="telemator-index"),
    url(r'^circuits/(?P<circuitid>.+)', circuit.render_circuit, name='circuit-info'),
    url(r'^circuits/', circuit.render_circuits, name='circuit-list'),
    url(r'^rooms/(?P<roomid>.+)/circuits/', circuit.room_circuits, name='room-info-circuits'),
)
