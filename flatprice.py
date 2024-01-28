import base64
import pickle
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# Setting Page configuration and Background
st.set_page_config(page_title = 'Singapore Flats Price Prediction',layout='wide') 

st.markdown('<h1 style="text-align: center;color:#4b6331;">Singapore Flat Price Prediction</h1>', unsafe_allow_html=True)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    

set_background('img1.png')



data = pd.read_csv('raw_data.csv')
data1 = data.copy()

# Inverse transform of the columns for Streamlit Application
le = LabelEncoder()
       
def transform(column):
       data1[column] = le.fit_transform(data[column])
       original_column = list(le.inverse_transform(data1[column].unique()))
       return original_column

def dics(column):
       data1[column] = le.fit_transform(data[column])
       encoded_column = list(data1[column].unique())
       original_column = list(le.inverse_transform(data1[column].unique()))
       key_value = {}
       for key in original_column:
              for value in encoded_column:
                     key_value[key] = value
                     encoded_column.remove(value)
                     break
       return key_value


c1,c2 = st.columns(2)
with c1:
            Town = st.selectbox('Town',options= list(transform('town')))
            town1 = dics('town')
            t1 = town1[Town]
            flat_type = st.selectbox('Flat Type',options= list(transform('flat_type')))
            flat1 = dics('flat_type')
            f1 = flat1[flat_type]
            block = st.selectbox('Block',options= list(transform('block')))
            block1 = dics('block')
            b1 = block1[block]
            street_name = st.selectbox('Street Name',options=list(transform('street_name')))
            street1 = dics('street_name')
            s1 = street1[street_name]
            storey_range = st.selectbox('Storey Range',options=list(transform('storey_range')))
            storey1 = dics('storey_range')
            st1 =storey1[storey_range]
with c2:
            floor_area = st.number_input('Floor Area in sqm(30.0-300.0)',min_value=30.0,max_value=300.0)
            flat_model = st.selectbox('Falt model',options= list(transform('flat_model')))
            flatm = dics('flat_model')
            fm = flatm[flat_model]
            lease_commence_date = st.number_input('Lease Commence year(1966-2022)',min_value=1966,max_value=2022)
            year_sold = st.number_input('Year Sold(2015-2024)',min_value=2015,max_value=2024)
            cal = ((lease_commence_date + 99) - 2024) * 12
            remaining_lease_months = st.number_input('Remaining Lease in Months',cal)
         
button = st.button('Predict Flat Price')
if button:
       # Reading the prediction model
       with open('model.pkl','rb') as file:
               rf_model = pickle.load(file)
       ip =[[t1,f1,b1,s1,st1,floor_area,fm,lease_commence_date,year_sold,cal]]
       price = rf_model.predict(np.array(ip))[0]
       st.markdown(f'<h3 style="text-align: center;color:#4b6331;">Predicted Resale Price : {price} SGD</h3>', unsafe_allow_html=True)