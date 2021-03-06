from sqlalchemy import create_engine, or_, func
from sqlalchemy.orm import sessionmaker
from navtelemator.models import Cable, Circuit, CircuitEnd, Connection, Customer, End, Owner, Port, RoutingCable, Setting, KabTer
from django.conf import settings
import logging
import collections

TM_USER = getattr(settings, "TM_USER", None)
TM_PASSWORD = getattr(settings, "TM_PASSWORD", None)
TM_HOST = getattr(settings, "TM_HOST", None)
TM_PORT = getattr(settings, "TM_PORT", '1433')
TM_DBNAME = getattr(settings, "TM_DBNAME", None)

# writes to spam.log in NAV directory
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


# Get parameters from the config, used for connecting to the server
db_params = 'mssql+pymssql://' + TM_USER + ':' + TM_PASSWORD + '@' + TM_HOST + ':' + TM_PORT + '/' + TM_DBNAME

# Initiate engine and session, used for all queries
engine = create_engine(db_params)
Session = sessionmaker(bind=engine)
session = Session()


# Hardcoded database version from what is expected.
def correct_database_version():
    version = session.query(Setting).filter(Setting.VALUENAME == 'Version::DBFversion').one()
    if str(version.VALUEDATA) != '285212672':
        return version.VALUEDATA


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
    temp = session.query(RoutingCable, Cable).filter(or_(Cable.End_A == room, Cable.End_B == room))\
        .filter(RoutingCable.Cable == Cable.Cable, RoutingCable.Wire == 'A').order_by(RoutingCable.Circuit).all()
    result = []
    taken_list = []
    for entry in temp:
        if entry.RoutingCable.Circuit not in taken_list:
            taken_list.append(entry.RoutingCable.Circuit)
            result.append(entry)
    logger.info('get_circuit_details_by_room gave length: %d', len(result))
    return result


def get_circuits():
    logger.info('get_circuits called')
    result = session.query(Circuit).order_by(Circuit.Circuit).all()
    logger.info('get_circuits gave length: %d', len(result))
    return result

def get_circuits_by_end(end):
    pass


def get_circuit_amount():
    logger.info('get_circuit_amount called')
    result = session.query(func.count(Circuit.RowKey)).scalar()
    logger.info('get_circuit_amount gave: %d', result)
    return result


def get_customers():
    logger.info('get_customers called')
    result = session.query(Customer).order_by(Customer.Name).all()
    logger.info('get_customers gave length: %d', len(result))
    return result


def get_customer_by_id(custid):
    logger.info('get_customer_by_id called with %s', custid)
    result = session.query(Customer).filter(Customer.CustId == custid).one()
    logger.info('get_customer_by_id returned: %d', result.CustId)
    return result


def get_customer_amount():
    logger.info('get_customer_amount called')
    result = session.query(Customer).count()
    logger.info('get_customer_amount gave: %d', result)
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


def get_start_end_place_by_circuit(circuit):
    logger.info('get_start_end_place_by_circuit called with %s', circuit)
    start_point = None
    end_point = None
    start_netbox = None
    end_netbox = None
    try:
        circuit_start = session.query(CircuitEnd).filter(CircuitEnd.Circuit == circuit,
                                                         CircuitEnd.Parallel == 1).first()
        start_netbox = circuit_start
        point_info_start = session.query(End).filter(End.End == circuit_start.End).first()
        if point_info_start.IsEquipm == 1:
            start_point = point_info_start.EqLinkToPt
        else:
            start_point = point_info_start.End

    except Exception as e:
        logger.info(e)
    try:
        circuit_end = session.query(CircuitEnd).filter(CircuitEnd.Circuit == circuit,
                                                       CircuitEnd.Parallel == 2).first()
        end_netbox = circuit_end
        point_info_end = session.query(End).filter(End.End == circuit_end.End).first()
        if point_info_end.IsEquipm == 1:
            end_point = point_info_end.EqLinkToPt
        else:
            end_point = point_info_end.End
    except:
        pass

    return start_point, end_point, start_netbox, end_netbox


# returns a list of ports (fiber) in a cable
def get_ports_by_circuit(circuit, cable):
    result = session.query(RoutingCable).filter(RoutingCable.Circuit == circuit, RoutingCable.Cable == cable).all()
    return result


# returns odf for cable towards an end
def get_kabter_by_cable(cable, port, place):
    logger.info('get_kabter_by_cable called with %s %s %s', cable.Cable, port, place)
    entries = session.query(KabTer).filter(KabTer.Cable == cable.Cable, KabTer.End == place).all()
    result = None
    for entry in entries:
        if entry.FromCore <= port > result and (entry.FromCore + entry.NumCores > port):
            result = entry
    return result


# returns true if spliced (sjott) towards an end
def get_spliced(cable, end):
    logger.info('get_spliced called with %s', end)
    try:
        result = session.query(KabTer).filter(KabTer.Cable == cable.Cable, KabTer.End == end).first()
        if result.TrmTxt == 6:
            return True
    except:
        pass
    return False


