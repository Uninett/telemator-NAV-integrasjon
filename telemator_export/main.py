#!/usr/bin/env python3

from sqlalchemy import create_engine, inspect
from config import *
from db import *
import pandas as pd
from pandas.io import sql


def main():
    # Get parameters from the config, used for connecting to the server
    tm_params = 'mssql+pymssql://' + TM_USER + ':' + TM_PASSWORD + '@' + TM_HOST + ':' + TM_PORT + '/' + TM_DBNAME
    pg_params = 'postgresql://' + PG_USER + ':' + PG_PASSWORD + '@' + PG_HOST + ':' + PG_PORT + '/' + PG_DBNAME

    # Initiate engine, used for all queries
    tm_engine = create_engine(tm_params)
    pg_engine = create_engine(pg_params)

    table_dataframes = extract_dataframes(tm_engine, EXTRACT_DICT)
    print('Extract complete')
    lowercase_values(table_dataframes, COLUMN_TO_OBJECT, LOWERCASE_OBJECTS)
    print('Made values lowercase')
    regular_dict, composite_dict = create_dictionaries(table_dataframes, PREVIOUS_REGULAR_PRIMARY_KEYS, PREVIOUS_COMPOSITE_PRIMARY_KEYS)
    print('Created dictionaries')
    fix_foreign_keys(table_dataframes, REGULAR_FOREIGN_KEYS, COMPOSITE_FOREIGN_KEYS, regular_dict, composite_dict, COLUMN_TO_OBJECT)
    print('Fixed foreign keys')
    rename_columns(table_dataframes, NEW_COLUMN_NAMES)
    print('Renamed columns')
    rename_tables(table_dataframes, NEW_TABLE_NAMES)
    print('Renamed tables')
    table_dataframes['circuit_detail'] = generate_circuitdetails(table_dataframes)
    print('Generated circuitdetails')
    extract_cable_alias(table_dataframes)
    print('Extracted cable name')
    #delete_tables(table_dataframes, pg_engine)
    #print('Deleted old tables')
    print('Inserting dataframes')
    insert_dataframes(pg_engine, table_dataframes)


def delete_tables(datatables, engine):
    for key in datatables:
        sql.execute('DROP TABLE IF EXISTS "%s"'%key, engine)


def print_columns(engine, table_name):
    """
    Function for printing the columns of a table

    :param engine: Engine to be used for connecting
    :param table_name: String with the name of column
    """
    inspector = inspect(engine)
    for column in inspector.get_columns(table_name):
        print("Column: %s" % column['name'])


def extract_dataframes(engine, table_dict):
    """
    Extract dataframes from an SQLAlchemy engine

    :param engine: Engine used for extraction
    :param table_dict: Dictionary with table names as keys with list of columns as values
    :return: Dictionary with table names as keys and corresponding dataframe as value
    """
    result = {}
    for key in table_dict:
        result[key] = pd.read_sql_table(key, engine, columns=table_dict[key])
    return result


def insert_dataframes(engine, dataframes):
    """
    Inserts the given dataframes into a SQLAlchmey engine

    :param engine: The engine to be used
    :param dataframes: Dictionary of dataframes to be inserted
    """
    for key in dataframes:
        dataframes[key].to_sql(key, engine, index=False, if_exists='replace', schema='telemator')


def create_dictionaries(dataframes, regular_primaries, composite_primaries):
    """
    Return 2 dictionaries with the values used as primary key mapped to values which should be used as primary key.

    :param dataframes: Dictionary with the dataframes to be fixed
    :param regular_primaries: Dictionary containing the tables with regular primary key, with column names
    :param composite_primaries: Dictionary containing the tables with composite primary key, with column names
    :return: Tuple with the dictionary related to regular primary keys and dictionary related to composite primary key
    """
    def regular_dict(dataframes, primary_keys):
        result = {}
        for table in primary_keys:
            column = primary_keys[table]
            result[column] = {}
            for index, row in dataframes[table].iterrows():
                result[column][row[column]] = row['RowKey']
        return result

    def composite_dict(dataframes, primary_keys):
        result = {}
        for table in primary_keys:
            columns = primary_keys[table]
            result[columns] = {}
            for index, row in dataframes[table].iterrows():
                result[columns][str(row[columns[0]]) + ' ' + str(row[columns[1]])] = row['RowKey']
        return result

    return regular_dict(dataframes, regular_primaries), composite_dict(dataframes, composite_primaries)


def fix_foreign_keys(dataframes, regular_foreign_keys, composite_foreign_keys, regular_dict, composite_dict, column_mapping):
    """
    Updates the foreign key fields with the proper values (the unique id of the referenced object)
    :param dataframes: Dictionary of dataframes
    :param regular_foreign_keys: Dictionary of non-composite foreign keys, indexed by table name
    :param composite_foreign_keys: Dictionary of comosite foreign keys, indexed by table name
    :param regular_dict: Dictionary of non-composite objects, indexed by old id
    :param composite_dict: Dictionary of composite objects, indexed by old id
    :return:
    """
    def fix_regular_keys(dataframes, keys, dict, column_mapping):
        for key in keys:
            for i, row in dataframes[key].iterrows():
                for column in keys[key]:
                    if column_mapping[column] not in dict:
                        continue
                    elif (row[column] == None):
                        continue
                    dataframes[key].set_value(i, column, dict[column_mapping[column]][row[column]])

    def fix_composite_keys(dataframes, keys, dict):
        for key in keys:
            column1 = keys[key][0]
            column2 = keys[key][1]
            for i, row in dataframes[key].iterrows():
                result = dict[(column1, column2)][str(row[column1]) + ' ' + str(row[column2])]
                dataframes[key].set_value(i, column1, result)
            del dataframes[key][column2]

    fix_composite_keys(dataframes, composite_foreign_keys, composite_dict)
    fix_regular_keys(dataframes, regular_foreign_keys, regular_dict, column_mapping)


def rename_tables(dataframes, name_dict):
    """
    Changes the name of the dataframes in the given dictionary
    :param dataframes: Dictionary with dataframes to be renamed
    :param name_dict: Dictionary with old name as key and new name as value
    """
    for key in dataframes:
        if key in name_dict:
            dataframes[name_dict[key]] = dataframes.pop(key)


def lowercase_values(dataframes, column_mapping, lowercase_list):
    """
    Converts the values in a table to lowercase
    :param dataframes: Dictionary of dataframes to iterate over
    :param column_mapping: Mapping from column to object type
    :param lowercase_list: Dict with columns to be converted, indexed by table name
    :return:
    """
    for key in dataframes:
        for i, row in dataframes[key].iterrows():
            for column_name in row.index:
                if column_name not in column_mapping or row.loc[column_name] == None:
                    continue
                if column_name in lowercase_list or column_mapping[column_name] in lowercase_list:
                    dataframes[key].set_value(i, column_name, row.loc[column_name].lower())


def rename_columns(dataframes, column_dict):
    """
    Rename the columns of the given dataframes
    :param dataframes: Dictionary of dataframes
    :param column_dict: Dictionary with names, the old one being key and the new being the value
    """
    for key in dataframes:
        dataframes[key].rename(columns=column_dict, inplace=True)


def generate_circuitdetails(dataframes):
    """
    Function for generating details for circuits, as hown in the telemator application
    :param dataframes: Dictionary of the dataframes used in the script
    :return: Dataframe of the circuit_details generated
    """
    def get_objects_and_ids(dataframes, circuit_id):
        start = None
        stop = None
        cables = []
        routing_cables = []
        routing_cableids = []
        for j, routingrow in dataframes['routing_cable'].iterrows():
            if (routingrow['circuit'] == circuit_id):
                routing_cables.append(routingrow)
                routing_cableids.append(routingrow['cable'])
        for j, cablerow in dataframes['cable'].iterrows():
            if cablerow['cable'] in routing_cableids:
                cables.append(cablerow)
        for j, circuitendrow in dataframes['circuit_end'].iterrows():
            if circuitendrow['circuit'] == circuit_id:
                if circuitendrow['parallel'] == 1:
                    start = circuitendrow['end']
                elif circuitendrow['parallel'] == 2:
                    stop = circuitendrow['end']
        return cables, routing_cables, routing_cableids, start, stop

    def get_current_row(current):
        current_row = None
        found_row = False
        for j, endrow in dataframes['end'].iterrows():
            if endrow['end'] == current:
                current_row = endrow
                found_row = True
                break
        return current_row, found_row

    def get_next_element(current, current_row, cables, stop):
        if current_row['is_equipment'] == 0:
            if len(cables) == 0:
                current = stop
            else:
                for cableindex, cablerow in enumerate(cables):
                    if cablerow['end_a'] == current:
                        current = cablerow['end_b']
                    elif cablerow['end_b'] == current:
                        current = cablerow['end_a']
                    else:
                        continue
                    del cables[cableindex]
                    break
        elif current_row['is_equipment'] == 1:
            current = current_row['room']
        return current, cables

    def generate():
        circuit_details = pd.DataFrame(columns=['id', 'circuit', 'index', 'end'])
        counter = 1
        maxloops = 10
        for i,row in dataframes['circuit'].iterrows():
            circuit_id = row['circuit']
            if circuit_id.startswith('TEMPLATE'):
                dataframes['circuit'].drop(i, inplace=True)
                continue
            print(circuit_id)
            cables, routing_cables, routing_cableids, start, stop = get_objects_and_ids(dataframes, circuit_id)
            if start == None and stop == None:
                continue
            current = start
            details = [current]
            loopcounter = 0
            while current != stop:
                # If there is no stop, just add the start
                if stop == None:
                    break
                loopcounter += 1
                if loopcounter == 11:
                    break
                current_row, found_row = get_current_row(current)
                if found_row == False:
                    break
                current, cables = get_next_element(current, current_row, cables, stop)
                details.append(current)
            if loopcounter == 11:
                continue
            for index, detail in enumerate(details):
                circuit_details.loc[counter] = pd.Series({'id': counter, 'circuit': circuit_id, 'index': index + 1, 'end': detail})
                counter += 1
        return circuit_details

    return generate()


def extract_cable_alias(dataframes):
    result = {}
    for i, row in dataframes['cable'].iterrows():
        if row['comment']:
            try:
                result[i] = row['comment'].split('\nSambandsnavn:')[1]
            except IndexError:
                result[i] = None
        else:
            result[i] = None
    dataframes['cable']['alias'] = pd.Series(result)


if __name__ == '__main__':
    main()
