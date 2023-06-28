import streamlit 
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
    streamlit.error("please select a fruit to get information.")
  else:
    function_retun_value=get_fruitvice_data(fruit_choice)
    streamlit.dataframe(function_retun_value)
except URLError as e:
  streamlit.error()
