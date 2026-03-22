import streamlit as st
import pandas as pd
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

File="expense_tracker.csv"
st.title("SEARCH EXPENSE")
today=date.today()

options = st.selectbox(
    "SEARCH BY:-" , ("DATE", "CATEGORY","ALL EXPENSES"), index=None
)

if options=="DATE":
    date_input=st.date_input("SELECT DATE", format="YYYY-MM-DD" , value=today)
    df=pd.read_csv(File)
    df["Date"]=df["Date"].astype(str).str.strip()
    date_str=date_input.strftime("%Y-%m-%d")
    filter=df[df["Date"]==date_str]
    if st.button("SEARCH"):
        if not filter.empty:
            st.success(f"Found {len(filter)} record(s) for {date_str}")
            filter.index+=1
            st.dataframe(filter)
        else:
            st.warning("NO RECORD FOUND")

elif options=="CATEGORY":
    option = st.selectbox(
    "CATEGORIES:-" , ("FOOD", "CLOTHES", "ELECTRONICS", "VEHICLES"), index=None)
    df=pd.read_csv(File)
    filter1=df[df["Category"]==option]
    if st.button("SEARCH"):
        if not filter1.empty:
            st.success(f"Found {len(filter1)} record(s) for {option}")
            filter1.index+=1
            st.dataframe(filter1)
        else:
            st.warning("NO RECORD FOUND")
    
elif options=="ALL EXPENSES":
    df=pd.read_csv(File)
    df.index+=1
    st.dataframe(df)

if st.button("HOME"):
    st.switch_page("app.py")

        
            
            
     
