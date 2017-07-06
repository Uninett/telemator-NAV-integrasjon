#################################################
# Information for Telemator SQL Server (Import) #
#################################################

# Server to connect to
tm_host = ''
# Port number
tm_port = ''

# Username
tm_user = ''
# Password
tm_password = ''

# Name of database to use
tm_name = ''


############################################
# Information for Postgres Server (Export) #
############################################

# Server to connect to
pg_host = ''
# Port number
pg_port = ''

# Username
pg_user = ''
# Password
pg_password = ''

# Name of database to use
pg_name = ''


################################
# Information about extraction #
################################

# Dictionary with lists of which columns to get for each table
extract_dict = {
    'KabReg': ['RowKey', 'Cable', 'End_A', 'End_B'],
    'EndReg': ['RowKey', 'End'],
    'KabTer': ['RowKey', 'Cable', 'IsEnd_A', 'FromCore', 'End', 'IsDraft'],
    'LedRut': ['RowKey', 'Cable', 'Core', 'Circuit', 'Remark'],
    'SbReg': ['RowKey', 'Circuit', 'Type', 'Speed'],
    'UtsTilk': ['RowKey', 'Pin', 'Port', 'End', 'Circuit'],
    'UtsTlf': ['RowKey', 'Circuit', 'Parallel', 'End'],
    'UtsUtg': ['RowKey', 'End', 'Port', 'Label', 'Remark', 'Type']
               }

# Single-column primary key for each table
regular_primary_keys = {
    'KabReg': 'Cable',
    'EndReg': 'End',
    'SbReg': 'Circuit',
}

# Composite primary key for each table
composite_primary_keys = {
    'UtsUtg': ('Port', 'End')
}

# List of single-column foreign keys associated with each table
regular_foreign_keys = {
    'KabReg': ['End_A', 'End_B'],
    'KabTer': ['Cable', 'End'],
    'LedRut': ['Cable', 'Circuit'],
    'UtsTilk': ['Circuit'],
    'UtsTlf': ['Circuit', 'End'],
    'UtsUtg': ['End']
               }

# List of composite foreign keys associated with each table
composite_foreign_keys = {
    'UtsTilk': ['Port', 'End'],
}

# List of tables to be renamed with the new name
new_table_names = {
    'KabReg': 'cables',
    'EndReg': 'ends',
    'KabTer': 'terminations',
    'LedRut': 'routing_cables',
    'SbReg': 'circuits',
    'UtsTilk': 'connections',
    'UtsTlf': 'circuit_ends',
    'UtsUtg': 'ports'
}

# List of new column names
new_column_names = {
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
}