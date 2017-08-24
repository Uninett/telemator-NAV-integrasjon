##################################################
# Information for Telemator SQL Server (Extract) #
##################################################

# Server to connect to
TM_HOST = ''
# Port number
TM_PORT = '1433'

# Username
TM_USER = ''
# Password
TM_PASSWORD = ''

# Name of database to use
TM_DBNAME = ''


############################################
# Information for Postgres Server (Inserrt) #
############################################

# Server to connect to
PG_HOST = ''
# Port number
PG_PORT = '5432'

# Username
PG_USER = ''
# Password
PG_PASSWORD = ''

# Name of database to use
PG_DBNAME = ''

try:
    LOCAL_DB_SETTINGS
except NameError:
    try:
        from local_db_settings import *
    except ImportError:
        pass
