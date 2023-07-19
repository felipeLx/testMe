import pandas as pd
import requests
from utils import convert_attribute_column, handle_hyper_file

class MercadoLibreData:
    def __init__(self, product_name, num_items):
        self.product_name = product_name
        self.num_items = num_items
        self.df = pd.DataFrame()
    
    def retrieve_data(self):
        # Set the desired number of items to retrieve.
        num_items = self.num_items

        # Variables to function and data
        api_url = ''
        offset = 0
        limit = 50

        # Calculate the number of requests needed to retrieve the desired number of items.
        num_requests = num_items // limit

        # Make the requests to the API.
        for i in range(num_requests):
            # Calculate the current offset.
            offset = i * limit
            
            # Make a request to the API with the current offset and limit.
            editable_product_name = self.product_name.upper().replace(' ', '%20')
            api_url = f'https://api.mercadolibre.com/sites/MLA/search?q={editable_product_name}&limit={limit}&offset={offset}#json'
            data = requests.get(api_url)
            transformedData = data.json()
            
            # Convert the results to a DataFrame and append it to the existing DataFrame.
            new_df = pd.DataFrame(pd.json_normalize(transformedData['results']))
            # Find all columns that have the desired prefix.
            cols_to_drop = [col for col in new_df.columns if col.startswith('variations_data.')]

            # Drop the columns from the DataFrame.
            new_df = new_df.drop(cols_to_drop, axis=1)
            self.df = pd.concat([self.df, new_df], ignore_index=True)
            
            # Convert the attribute column.
            self.df = convert_attribute_column(self.df)
    
    def generate_hyper_file(self):
        # Generate the Hyper file.
        hyper_file = handle_hyper_file(self.df)

        # Read the contents of the Hyper file.
        with open(hyper_file, 'rb') as f:
            data = f.read()
        
        return data
