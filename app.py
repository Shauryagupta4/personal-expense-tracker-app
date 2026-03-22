import streamlit as st
st.set_page_config(
    menu_items={
        
    },
)

st.markdown("""
    <style>
            .stButton > button {background-color: #2e7d32 !important;
            color: white !important}
    </style>
            """, unsafe_allow_html=True)

st.title("PERSONAL EXPENSE TRACKER")

if st.button("ADD EXPENSES"):
    st.switch_page("pages/add.py")

if st.button("EXPENSE PIE CHART"):
    st.switch_page("pages/pie.py")

if st.button("SEARCH EXPENSE"):
    st.switch_page("pages/searching.py")
