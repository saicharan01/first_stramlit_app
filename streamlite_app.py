import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)
fruit_choice = streamlit .text_input('What fruit would you like information about?','')
streamlit .write('The user entered ', fruit_choice)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
streamlit.dataframe(my_data_row)
