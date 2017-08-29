################################
# Information about extraction #
################################

# Dictionary with lists of which columns to get for each table
EXTRACT_DICT = {
    'AboReg': ['RowKey', 'CustId', 'Name', 'Department', 'Addr2'],
    'ElmOwner': ['RowKey', 'Owner', 'Name', 'Email', 'Type'],
    'EndReg': ['RowKey', 'End', 'EqLinkToPt', 'IsEquipm'],
    'KabReg': ['RowKey', 'Cable', 'End_A', 'End_B', 'Owner', 'RemarkM'],
    'KabTer': ['RowKey', 'Cable', 'IsEnd_A', 'FromCore', 'End', 'IsDraft'],
    'KuSbLink': ['RowKey', 'CustId', 'Circuit'],
    'LedRut': ['RowKey', 'Cable', 'Core', 'Circuit', 'Wire', 'Remark'],
    'SbReg': ['RowKey', 'Circuit', 'Type', 'Speed', 'Reference', 'Owner'],
    'UtsTilk': ['RowKey', 'Pin', 'Port', 'End', 'Circuit'],
    'UtsTlf': ['RowKey', 'Circuit', 'Parallel', 'End'],
    'UtsUtg': ['RowKey', 'End', 'Port', 'Label', 'Remark', 'Type'],
               }

# Single-column primary key for each table
PREVIOUS_REGULAR_PRIMARY_KEYS = {
}

# Composite primary key for each table
PREVIOUS_COMPOSITE_PRIMARY_KEYS = {
    'UtsUtg': ('Port', 'End')
}

# List of single-column foreign keys associated with each table
REGULAR_FOREIGN_KEYS = {
    'EndReg': ['EqLinkToPt'],
    'KabReg': ['End_A', 'End_B'],
    'KabTer': ['Cable', 'End'],
    'LedRut': ['Cable', 'Circuit'],
    'UtsTilk': ['Circuit'],
    'UtsTlf': ['Circuit', 'End'],
    'UtsUtg': ['End'],
               }

# Mapping from column name to which model to use as foreign key
COLUMN_TO_OBJECT = {
    'Cable': 'Cable',
    'Circuit': 'Circuit',
    'End': 'End',
    'End_A': 'End',
    'End_B': 'End',
    'EqLinkToPt': 'End',
}

# List of composite foreign keys associated with each table
COMPOSITE_FOREIGN_KEYS = {
    'UtsTilk': ['Port', 'End'],
}

# List of tables to be renamed with the new name
NEW_TABLE_NAMES = {
    'AboReg': 'customer',
    'ElmOwner': 'owner',
    'EndReg': 'end',
    'KabReg': 'cable',
    'KabTer': 'termination',
    'KuSbLink': 'customer_circuit',
    'LedRut': 'routing_cable',
    'SbReg': 'circuit',
    'UtsTilk': 'connection',
    'UtsTlf': 'circuit_end',
    'UtsUtg': 'port',
}

# Dict of new column names
NEW_COLUMN_NAMES = {
    'Addr2': 'address',
    'Cable': 'cable',
    'Circuit': 'circuit',
    'Core': 'core',
    'CustId': 'customer',
    'Department': 'department',
    'Email': 'email',
    'End': 'end',
    'End_A': 'end_a',
    'End_B': 'end_b',
    'EqLinkToPt': 'room',
    'FromCore': 'from_core',
    'IsDraft': 'is_draft',
    'IsEnd_A': 'is_end_a',
    'IsEquipm': 'is_equipment',
    'Label': 'label',
    'Name': 'name',
    'Owner': 'owner',
    'Pin': 'pin',
    'Port': 'port',
    'Parallel': 'parallel',
    'Reference': 'alias',
    'Remark': 'remark',
    'RemarkM': 'comment',
    'RowKey': 'id',
    'Speed': 'speed',
    'Type': 'type',
    'Wire': 'wire',
}

# List of columns to be lowercased
LOWERCASE_OBJECTS = ['End', 'Reference']

SCHEMA = 'telemator'
