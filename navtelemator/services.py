from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from navtelemator.models import Cable, Circuit, Connection, Customer, End, Owner, Port, RoutingCable
from django.conf import settings
import logging

TM_USER = getattr(settings, "TM_USER", None)
TM_PASSWORD = getattr(settings, "TM_PASSWORD", None)
TM_HOST = getattr(settings, "TM_HOST", None)
TM_PORT = getattr(settings, "TM_PORT", '1433')
TM_DBNAME = getattr(settings, "TM_DBNAME", None)

logger = logging.getLogger(__name__)

# Get parameters from the config, used for connecting to the server
db_params = 'mssql+pymssql://' + TM_USER + ':' + TM_PASSWORD + '@' + TM_HOST + ':' + TM_PORT + '/' + TM_DBNAME

# Initiate engine and session, used for all queries
engine = create_engine(db_params)
Session = sessionmaker(bind=engine)
session = Session()


def get_cable_by_id(cable):
    logger.info('get_cable_by_id called with %s', cable)
    result = session.query(Cable).filter(Cable.Cable == cable).one()
    logger.info('get_cable_by_id returned: %d', result.Cable)
    return result

def get_cables_by_end(end):
    logger.info('get_cables_by_end called with %s', end)
    result = session.query(Cable).filter(or_(Cable.End_A == end, Cable.End_B == end)).order_by(Cable.Cable).all()
    logger.info('get_cables_by_end gave length: %d', len(result))
    return result


def get_circuit_by_id(circuit):
    logger.info('get_circuit_by_id called with %s', circuit)
    result = session.query(Circuit).filter(Circuit.Circuit == circuit.upper()).one()
    logger.info('get_circuit_by_id returned: %d', result.Circuit)
    return result


def get_circuit_details():
    logger.info('get_circuit_details called')
    result = session.query(Connection, Port).filter(Connection.End == Port.End, Connection.Card == Port.Card,
                                                  Connection.Port == Port.Port).all()
    logger.info('get_circuit_details gave length: %d', len(result))
    return result


def get_circuit_details_by_netbox(end):
    logger.info('get_circuit_details_by_netbox called with %s', end)
    result = session.query(Connection, Port).filter(Connection.End == end, Connection.Wire == 'A')\
        .filter(Connection.End == Port.End, Connection.Card == Port.Card,Connection.Port == Port.Port).order_by(Connection.Circuit).all()
    logger.info('get_circuit_details_by_netbox gave length: %d', len(result))
    return result


def get_circuit_details_by_room(room):
    logger.info('get_circuit_details_by_room called with %s', room)
    result = session.query(RoutingCable, Cable).filter(or_(Cable.End_A == room, Cable.End_B == room))\
        .filter(RoutingCable.Cable == Cable.Cable, RoutingCable.Wire == 'A').order_by(RoutingCable.Circuit).all()
    logger.info('get_circuit_details_by_room gave length: %d', len(result))
    return result


def get_circuits():
    logger.info('get_circuits called')
    result = session.query(Circuit).order_by(Circuit.Circuit).all()
    logger.info('get_circuits gave length: %d', len(result))
    return result

def get_circuits_by_end(end):
    pass


def get_customer_by_id(custid):
    logger.info('get_customer_by_id called with %s', custid)
    result = session.query(Customer).filter(Customer.CustId == custid).one()
    logger.info('get_customer_by_id returned: %d', result.CustId)
    return result


# def get_customer_by_name(name):
#   return session.query(Customer).filter(Customer.CustId == name).all()

def get_connections_by_circuit(circuit):
    logger.info('get_connections_by_circuit called with %s', circuit)
    result = session.query(Connection, Port).filter(Connection.Circuit == circuit, Connection.Wire == 'A') \
        .filter(Connection.End == Port.End, Connection.Card == Port.Card, Connection.Port == Port.Port).order_by(Connection.End).all()
    logger.info('get_connections_by_circuit gave length: %d', len(result))
    return result


def get_end_by_id(end):
    logger.info('get_end_by_id called with %s', end)
    result = session.query(End).filter(End.End == end).one()
    logger.info('get_end_by_id returned: %d', result.End)
    return result


def get_owner_by_id(owner):
    logger.info('get_owner_by_id called with %s', owner)
    result = session.query(Owner).filter(Owner.Owner == owner).one()
    logger.info('get_owner_by_id returned: %d', result.Owner)
    return result


def get_routingcables_by_cable(cable):
    logger.info('get_routingcables_by_cable called with %s', cable)
    result = session.query(RoutingCable).filter(RoutingCable.Cable == cable, RoutingCable.Wire == 'A').order_by(RoutingCable.Core).all()
    logger.info('get_routingcables_by_cable gave length: %d', len(result))
    return result


def get_routingcables_by_circuit(circuit):
    logger.info('get_routingcables_by_circuit called with %s', circuit)
    result = session.query(RoutingCable).filter(RoutingCable.Circuit == circuit, RoutingCable.Wire == 'A').order_by(RoutingCable.Cable).all()
    logger.info('get_routingcables_by_circuit gave length: %d', len(result))
    return result
