import streamlit as st
import pandas as pd
import os
from datetime import date

st.markdown("""
    <style>
            .stApp{background-color: #1a1f2e !important}
            .st-emotion-cache-1wivap2, .block-container {background-color: #1a1f2e !important}
            .st-emotion-cache-5rimss, p, h2, h3, {color: #000000  !important}
            .stButton > button {background-color: #2e7d32 !important;
            color: white !important}
    </style>
            """, unsafe_allow_html=True)
st.title("ADD NEW EXPENSE")

File="expense_tracker.csv"
CATEGORIES={1:"FOOD",2:"CLOTHES",3:"VEHICLES",4:"ELECTRONICS"}
if not os.path.exists(File): #to check file exist or not if not it will create a new one
    df=pd.DataFrame(columns=["Date","Category","Item","Amount","Payment Method"])
    df.to_csv(File,index=False)
    print("New expense file created")

current_date=date.today().strftime("%Y-%m-%d")

options = st.selectbox(
    "CATEGORIES:-" , ("FOOD", "CLOTHES", "ELECTRONICS", "VEHICLES"), index=None
)

item_name = st.text_input("ENTER THE ITEM YOU BOUGHT")

amount = st.number_input("ENTER THE AMOUNT")

payment = st.selectbox("PAYMENT MODE", ("ONLINE", "CASH"), index=None
)

if st.button("ADD"):
    if options ==None:
        st.error("Option can not be empty")
    elif payment ==None:
        st.error("payment can not be empty")
    elif not item_name.strip():
        st.error("item name can not be empty")
    else:
        new_expense=pd.DataFrame([[current_date,options,item_name, amount, payment]], columns=["Date","Category","Item","Amount","Payment Method"])
        new_expense.to_csv(File, mode='a', index=False, header=False)
        st.success("YOUR EXPENSE IS ADDED")

if st.button("HOME"):
    st.switch_page("app.py")
