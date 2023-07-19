import requests
import tableauhyperapi as th

API_LINK = 'https://api.mercadolibre.com/sites/MLA/search?q=chromecast#json'

# defined the variable to be appended
data = ''
data = requests.get(API_LINK)
transformedData = data.content


# convert column with array of Dictionary to multiple columns with prefix
def convert_df_to_hyper(df):
    csv_file = df.to_csv('sellout.csv', sep=';', encoding='utf-8', header=True, decimal=',')
    return csv_file
  
# convert dataframe to hyper file
def convert_attribute_column(df):
    """
    Convert the attribute column in the df DataFrame into multiple columns with the prefix `attribute-`.

    Args:
        df (DataFrame): The DataFrame to be converted.

    Returns:
        DataFrame: The converted DataFrame.
    """
    # Define a function to extract attribute values from a list of dictionaries.
    def extract_attributes(row):
        attributes = row['attributes']
        for attribute_dict in attributes:
            for key, value in attribute_dict.items():
                row['att-' + str(key)] = value
                #att_values = row['att-values']
                #for key, value in att_values:
                    #row['att-vl-' + str(key)] = value
        return row

    # Apply the function to each row of the DataFrame.
    df = df.apply(extract_attributes, axis=1)

    # Drop the original attribute column.
    df.drop('attributes', axis=1, inplace=True)

    return df
