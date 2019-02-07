#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Some lookup functions, can be used for testing the Telemator DB connection
Usage: 
   python tmlookup.py <method> <search-arg> <attribute>
Examples:
   python tmlookup.py get_customer_by_id 3 Name
   python tmlookup.py get_cables_by_end teknobyen
   python tmlookup.py get_customer_by_id 140 OrgNum
   python tmlookup.py get_cables_by_end teknobyen
"""

import os, sys
import argparse
sys.path.append("/etc/nav/python")
from local_settings import *
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from navtelemator.models import Cable, Circuit, Connection, Customer, Owner, Port, RoutingCable

db_params = 'mssql+pymssql://' + TM_USER + ':' + TM_PASSWORD + '@' + TM_HOST + ':' + TM_PORT + '/' + TM_DBNAME

# Initiate engine and session, used for all queries
engine = create_engine(db_params)
Session = sessionmaker(bind=engine)
session = Session()

def realmain ():
    print TM_DBNAME
    c = get_customer_by_id(140);
    print c.Name
    
def get_ports_all(a):
    return session.query(Port).all()

def get_cable_by_id(cable):
    return session.query(Cable).filter(Cable.Cable == cable).one()

def get_cables_by_end(end):
    return session.query(Cable).filter(or_(Cable.End_A == end, Cable.End_B == end)).all()


def get_circuit_by_id(circuit):
    return session.query(Circuit).filter(Circuit.Circuit == circuit.upper()).one()


def get_circuit_details():
    return session.query(Connection, Port).filter(Connection.End == Port.End, Connection.Card == Port.Card,
                                                  Connection.Port == Port.Port)


def get_circuit_details_by_netbox(end):
    return session.query(Connection, Port).filter(Connection.End == end, Connection.Wire == 'A')\
        .filter(Connection.End == Port.End, Connection.Card == Port.Card,Connection.Port == Port.Port).all()


def get_circuit_details_by_room(room):
    return session.query(RoutingCable, Cable).filter(or_(Cable.End_A == room, Cable.End_B == room))\
        .filter(RoutingCable.Cable == Cable.Cable, RoutingCable.Wire == 'A').all()


def get_circuits():
    return session.query(Circuit).all()

def get_circuits_by_end(end):
    pass


def get_customer_by_id(custid):
    return session.query(Customer).filter(Customer.CustId == custid).one()


# def get_customer_by_name(name):
#   return session.query(Customer).filter(Customer.CustId == name).all()


def get_owner_by_id(owner):
    return session.query(Owner).filter(Owner.Owner == owner).one()


def get_routingcables_by_cable(cable):
    return session.query(RoutingCable).filter(RoutingCable.Cable == cable, RoutingCable.Wire == 'A').all()


def get_routingcables_by_circuit(circuit):
    return session.query(RoutingCable).filter(RoutingCable.Circuit == circuit, RoutingCable.Wire == 'A').all()

if __name__ == '__main__':
    try:
        method = getattr(sys.modules[__name__], sys.argv[1])
        args = sys.argv[2]
        try: 
            objmethod = sys.argv[3]
        except:
            objmethod = None
    except:
        method = getattr(sys.modules[__name__], 'get_customer_by_id')
        args = ['140']
        objmethod = 'Name'
    result = method (args)
    if (type(result) is list):
        if objmethod:
            print [getattr(x, objmethod) for x in result]
        else:
            print [x for x in result]
    else:
        if objmethod:
            print getattr(result, objmethod)
        else:
            print result
        
    
