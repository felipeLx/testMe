import streamlit as st
from mercado_libre_data import MercadoLibreData

# User input
product_name = st.sidebar.text_input(label='Diga el producto que busca', placeholder='El Camino de Santiago')
user_items_limit = st.sidebar.number_input(label='Informar la cantidad de items', min_value=150)
st.image('./logo.png', caption='Mercado Libre')    
# Create an instance of the MercadoLibreData class.
ml_data = MercadoLibreData(product_name, user_items_limit)

# Retrieve data from the API.
ml_data.retrieve_data()

# Print DataFrame
if len(ml_data.df) == 0:
    st.write('''
             # Por favor, indique el producto que está buscando en el lateral
              Y verás los datos del producto y podrá exportar el fichero con extensión hyper (Tableau) a la carpeta local.
             ''', unsafe_allow_html=False)

if len(ml_data.df) != 0:
    # Generate the Hyper file.
    data = ml_data.generate_hyper_file()

    # Body
    
    st.write('''
            # Sigue los datos solicitados
            ''', unsafe_allow_html=False)
    st.write(ml_data.df)

    
    st.sidebar.download_button('Guardar Hyper', data, file_name=product_name+'.hyper')
