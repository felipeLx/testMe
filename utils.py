import requests

API_LINK = 'https://api.mercadolibre.com/sites/MLA/search?q=chromecast&limit=50#json'

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

    # Get the attribute column from the DataFrame.
    attribute_column = df['attribute']

    # Iterate over the attribute column and create new columns for each attribute.
    for attribute in attribute_column:
        new_column_name = 'attribute-' + attribute
        df[new_column_name] = attribute

    # Drop the original attribute column.
    df.drop('attribute', axis=1, inplace=True)

    return df
