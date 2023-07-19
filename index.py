import streamlit as st
from mercado_libre_data import MercadoLibreData

# Initialize the session state variables.
if 'download_clicked' not in st.session_state:
    st.session_state.download_clicked = False
if 'product_name' not in st.session_state:
    st.session_state.product_name = ''
if 'user_items_limit' not in st.session_state:
    st.session_state.user_items_limit = 150
data = ''

# User input
st.sidebar.text_input(label='Diga el producto que busca', placeholder='El Camino de Santiago', key='product_name')
st.sidebar.slider(label='Informar la cantidad de items', min_value=150, max_value=1000, key='user_items_limit')
st.image('./logo.png', caption='Mercado Libre')

# Create an instance of the MercadoLibreData class.
ml_data = MercadoLibreData(st.session_state.product_name, st.session_state.user_items_limit)

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

    # Add a download button.
    if st.sidebar.download_button('Guardar Hyper', data, file_name=st.session_state.product_name+'.hyper'):
        # Set the session state variable to True and rerun the script.
        st.session_state.download_clicked = True
        st.experimental_rerun()