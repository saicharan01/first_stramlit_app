import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
def get_fruitvice_data(this_fruit_choise):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choise ) 
  fruityvice_normalize=pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalize

streamlit.header("Frutiyvice fruit advice:")
try:
  fruit_choice = streamlit .text_input('What fruit would you like information about?')
  if not  fruit_choice :
    st.error("please select a fruit to get information.")
  else:
    function_retun_value=get_fruitvice_data(fruit_choice)
    st.dataframe(function_retun_value)
except URLError as e:
  st.error()

st.header("The fruit load list:")

def get_fruit_load_list():
        my_cur = my_cnx.cursor()
        my_cur.execute("SELECT * FROM fruit_load_list")
        return my_cur.fetchall()


my_cux = None
if st.button("Get fruit load list"):
    my_cux = snowflake.connector.connect(**st.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    st.dataframe(my_data_rows)

  
