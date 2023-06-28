import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
def get_fruitvice_data(this_fruit_choise):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choise ) 
  st.text(fruityvice_response.json())
  fruityvice_normalize=pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalize

st.header("Frutiyvice fruit advice:")
try:
  fruit_choice = st .text_input('What fruit would you like information about?')
  if not  fruit_choice :
    st.error("please select a fruit to get information.")
  else:
    function_retun_value=get_fruitvice_data(fruit_choice)
    st.dataframe(function_retun_value)
except URLError as e:
  st.error()
