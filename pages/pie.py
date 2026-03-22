import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
st.markdown("""
    <style>
            .stApp{background-color: #1a1f2e !important}
            .st-emotion-cache-1wivap2, .block-container {background-color: #1a1f2e !important}
            .st-emotion-cache-5rimss, p, h1, h2, h3 {color: #e0f7e0 !important}
            .stButton > button {background-color: #2e7d32 !important;
            color: white !important}
    </style>
            """, unsafe_allow_html=True)

st.title("EXPENSE CHART")
File="expense_tracker.csv"
rd=pd.read_csv(File)
total_amount=rd.groupby('Category')['Amount'].sum()
plt.figure(figsize=(10,8))
plt.pie(total_amount.values, labels=total_amount.index, autopct='%1.2f%%', startangle=90)
plt.title("SPENDING BY CATEGORY")
plt.axis('equal')
plt.legend(title="CATEGORIES")
st.pyplot(plt.gcf())



if st.button("HOME"):
    st.switch_page("app.py")

