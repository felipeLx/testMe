import streamlit as st
import pandas as pd
import requests
from utils import convert_attribute_column

#user input:
product_name = st.sidebar.text_input(label='Diga el producto que busca', placeholder='El Camino de Santiago')
editable_product_name = str(product_name.upper())
print(editable_product_name)
#variables to function and data
api_url = ''
df = ''

if(len(product_name) > 2):
    try:
        api_url = 'https://api.mercadolibre.com/sites/MLA/search?q='+editable_product_name+'&limit=50#json'
        data = requests.get(api_url)
        transformedData = data.json()
        df = pd.DataFrame(pd.json_normalize(transformedData['results']))
        #print(df.columns)
        df = convert_attribute_column(df)
    except NameError:
        st.warning('La busqueda no ha sido exitosa, intente otro producto.', icon="⚠️")

# print dataframe
if len(df) == 0:
    st.write('''
             # Por favor, indique el producto que está buscando en el lateral
              Y verás los datos del producto y podrá exportar el fichero con extensión hyper (Tableau) a la carpeta local.
             ''', unsafe_allow_html=False)

if len(df) != 0:
    st.write('''
             # Sigue los datos solicitados
             ''', unsafe_allow_html=False)
    st.write(df)