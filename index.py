import streamlit as st
import pandas as pd
import requests
import tableauhyperapi as th
from utils import convert_attribute_column

#user input:
_input = st.sidebar.text_input(label='Qual Produto você está buscando?')

#variables to function and data
api_url = ''
df = ''

try:
    api_url = 'https://api.mercadolibre.com/sites/MLA/search?q='+_input+'&limit=50#json'
    data = requests.get(api_url)
    transformedData = data.json()
    # print(transformedData['results'])
    df = pd.DataFrame(pd.json_normalize(transformedData['results']))
    convert_attribute_column(df.copy())
except:
    st.warning('La busqueda no ha sido exitosa, intente otro producto.', icon="⚠️")

# print dataframe
print(len(df))

# Main body view
if len(df) == 0:
    st.write('''
             # Por favor, indique el producto que está buscando en el lateral
              Y verás los datos del producto y podrá exportar el fichero con extensión hyper (Tableau) a la carpeta local.
             ''', unsafe_allow_html=False)

if len(df) != 0:
    st.write(df) 

