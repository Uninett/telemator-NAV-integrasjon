################################
# Information about extraction #
################################

# Dictionary with lists of which columns to get for each table
EXTRACT_DICT = {
    'KabReg': ['RowKey', 'Cable', 'End_A', 'End_B', 'Owner'],
    'EndReg': ['RowKey', 'End', 'EqLinkToPt', 'IsEquipm'],
    'KabTer': ['RowKey', 'Cable', 'IsEnd_A', 'FromCore', 'End', 'IsDraft'],
    'LedRut': ['RowKey', 'Cable', 'Core', 'Circuit', 'Remark'],
    'SbReg': ['RowKey', 'Circuit', 'Type', 'Speed', 'Reference', 'Owner'],
    'UtsTilk': ['RowKey', 'Pin', 'Port', 'End', 'Circuit'],
    'UtsTlf': ['RowKey', 'Circuit', 'Parallel', 'End'],
    'UtsUtg': ['RowKey', 'End', 'Port', 'Label', 'Remark', 'Type'],
    'ElmOwner': ['RowKey', 'Owner', 'Name', 'Email', 'Type']
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
    'KabReg': ['End_A', 'End_B'],
    'KabTer': ['Cable', 'End'],
    'LedRut': ['Cable', 'Circuit'],
    'UtsTilk': ['Circuit'],
    'UtsTlf': ['Circuit', 'End'],
    'UtsUtg': ['End'],
    'EndReg': ['EqLinkToPt']
               }

# Mapping from column name to which model to use as foreign key
COLUMN_TO_OBJECT = {
    'End': 'End',
    'End_A': 'End',
    'End_B': 'End',
    'Cable': 'Cable',
    'Circuit': 'Circuit',
    'EqLinkToPt': 'End',
}

# List of composite foreign keys associated with each table
COMPOSITE_FOREIGN_KEYS = {
    'UtsTilk': ['Port', 'End'],
}

# List of tables to be renamed with the new name
NEW_TABLE_NAMES = {
    'KabReg': 'cable',
    'EndReg': 'end',
    'KabTer': 'termination',
    'LedRut': 'routing_cable',
    'SbReg': 'circuit',
    'UtsTilk': 'connection',
    'UtsTlf': 'circuit_end',
    'UtsUtg': 'port',
    'ElmOwner': 'owner'
}

# Dict of new column names
NEW_COLUMN_NAMES = {
    'Cable': 'cable',
    'RowKey': 'id',
    'Circuit': 'circuit',
    'End_A': 'end_a',
    'End_B': 'end_b',
    'IsEnd_A': 'is_end_a',
    'FromCore': 'from_core',
    'End': 'end',
    'IsDraft': 'is_draft',
    'Type': 'type',
    'Core': 'core',
    'Remark': 'remark',
    'Speed': 'speed',
    'Pin': 'pin',
    'Port': 'port',
    'Parallel': 'parallel',
    'Label': 'label',
    'EqLinkToPt': 'room',
    'IsEquipm': 'is_equipment',
    'Reference': 'alias',
    'Owner': 'owner',
    'Email': 'email',
    'Name': 'name',
}

# List of columns to be lowercased
LOWERCASE_OBJECTS = ['End', 'Reference']
