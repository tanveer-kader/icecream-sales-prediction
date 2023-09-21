# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:05:51 2023

@author: TanveerKader
"""

import numpy as np
import pickle
import streamlit as st


lr_model = pickle.load(open("C:/Users/TanveerKader/Desktop/New folder/icecream_sale_webapp/icecream_sale_lr_model.sav", 'rb')) 
xgb_model = pickle.load(open("C:/Users/TanveerKader/Desktop/New folder/icecream_sale_webapp/icecream_sale_xgb_model.sav", 'rb')) 

def icecream_sale_prediction(input_data):

    # change input data to nympy array
    input_data_arr = np.asarray(input_data)

    # reshape the numpy array
    input_data_reshaped = input_data_arr.reshape(1, -1)

    prediction_lr = lr_model.predict(input_data_reshaped)
    prediction_xgb = xgb_model.predict(input_data_reshaped)
    
    
    return prediction_lr[0], prediction_xgb[0]

def main():
    #title
    st.title("Ice Cream Sales Prediction")
    
    
    temperature = st.text_input("Enter the temperature today (C)")
    
    result_lr = ''
    result_xgb = ''
    
    #button
    if st.button("Predict"):
        result_lr, result_xgb = icecream_sale_prediction([float(temperature)])
        
    st.subheader("Todays Sale Prediction (Litres)")
    st.caption("Linear Regression Model")
    st.success(result_lr)
    st.caption("XGBoost Regressor Model")
    st.success(result_xgb)
    
    
    
if __name__ == "__main__":
    main()
    
    
# streamlit run "C:\Users\TanveerKader\Desktop\New folder\icecream_sale_webapp\icecream_sales_webapp.py"