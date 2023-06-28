import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalize = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalize

st.header("Fruityvice fruit advice:")
try:
    fruit_choice = st.text_input('What fruit would you like information about?')
    if not fruit_choice:
        st.error("Please select a fruit to get information.")
    else:
        function_return_value = get_fruitvice_data(fruit_choice)
        st.dataframe(function_return_value)
except URLError as e:
    st.error("An error occurred: " + str(e))

st.header("The fruit load list:")

def get_fruit_load_list(connection):
    with connection.cursor() as my_cur:
        my_cur.execute("SELECT * FROM fruit_load_list")
        return my_cur.fetchall()

if st.button("Get fruit load list"):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_data_rows = get_fruit_load_list(my_cnx)
    st.dataframe(my_data_rows)
def insert_row_snowflake(connection,new_friut):
    with connection.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values('from streamlit')")
        return "thanks fro adding "+new_fruit
add_my_fruit=st.text_input('Which fruit would you like to add?')
if st.button("Add new fruit"):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    back_from_fun=insert_row_snowflake(my_cnx,add_my_fruit)
    st.text(back_from_fun)
