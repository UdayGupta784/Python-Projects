import requests
import streamlit as st

API_KEY = "fe14c09f3591624f4d050628"
@st.cache_data

def get_rate():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    return requests.get(url).json()
    




st.title("🔄 Currency Converter")

data = get_rate()
rate = data["conversion_rates"]
currencies = sorted(rate.keys())

col1, col2 = st.columns(2)
with col1:
    from_curr = st.selectbox("FROM Currency", currencies)
with col2:
    to_curr = st.selectbox("TO Currency", currencies)

amount = st.number_input("Amount", min_value=0.0, value=1.0)
if st.button("Convert"):
    if from_curr == to_curr:
         st.error("Currencies Must Be Different!")
    else:
        result = amount/rate[from_curr]*rate[to_curr]
        st.success(f"{amount} {from_curr} = {result:.2f} {to_curr}")
    


