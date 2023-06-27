import streamlit 
streamlit .title("i am using snowflake")
streamlit .header(' snowflake')
streamlit .title('data warehouse')
streamlit .header('Breakfast Menu')
streamlit .text('🥣Omega 3 & Blueberry Oatmeal')
streamlit .text(' 🥗Kale, Spinach & Rocket Smoothie')
streamlit .text('🐔Hard-Boiled Free-Range Egg')
streamlit .text('🥑🍞 toast')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit .dataframe(my_fruit_list)
streamlit .multiselect("Pick some fruits:", list(my_fruit_list.index))
fruit_selected=streamlit .multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Banana'])
fruits_show=my_fruit_list.loc[fruit_selected]
streamlit .dataframe(fruits_show)

fruit_choice = streamlit .text_input('What fruit would you like information about?','Kiwi')
streamlit .write('The user entered ', fruit_choice)
import requests as rs
streamlit .header("Fruityvice Fruit Advice!")
fruityvice_response = rs.get("https://fruityvice.com/api/fruit/watermelon")
streamlit .text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit .dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
