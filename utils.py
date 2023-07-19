import requests
from tableauhyperapi import HyperProcess, Telemetry, Connection, CreateMode, TableName, SqlType, TableDefinition, Inserter
import pandas as pd
  
# convert dataframe to hyper file
def convert_attribute_column(df):
    # Define a function to extract attribute values from a list of dictionaries.
    def extract_attributes(row):
        attributes = row['attributes']
        for attribute_dict in attributes:
            for key, value in attribute_dict.items():
                row['att-' + str(key)] = value
            att_values = row['att-values']
            if isinstance(att_values, dict):
                for key, value in att_values.items():
                    row['att-vl-' + str(key)] = value

        return row

    # Apply the function to each row of the DataFrame.
    df = df.apply(extract_attributes, axis=1)
    # Delete the 'attributes' and 'att-values' columns from the DataFrame.
    #df = df.drop(['attributes', 'att-values'], axis=1)
    
    return df

def handle_hyper_file(df):
    # Define the name of the Hyper file.
    hyper_file = 'data.hyper'
    
    # Define the table schema.
    table_name = TableName('public', 'Extract')
    table_def = TableDefinition(table_name)
    for col in df.columns:
        table_def.add_column(col, SqlType.text())
    
    # Create a copy of the DataFrame with all columns converted to strings.
    df = df.astype(str)
    
    # Create the Hyper file.
    with HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:
        with Connection(hyper.endpoint, hyper_file, CreateMode.CREATE_AND_REPLACE) as connection:
            connection.catalog.create_table(table_def)
            
            # Insert the data into the Hyper file.
            with Inserter(connection, table_def) as inserter:
                for row in df.itertuples(index=False):
                    inserter.add_row(row)
                inserter.execute()
    # Return the path to the Hyper file.
    return hyper_file