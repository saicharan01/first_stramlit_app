import streamlit as st
st.title("i am using snowflake")
st.header(' snowflake')
st.title('data warehouse')
st.header('Breakfast Menu')
st.text('🥣Omega 3 & Blueberry Oatmeal')
st.text(' 🥗Kale, Spinach & Rocket Smoothie')
st.text('🐔Hard-Boiled Free-Range Egg')
st.text('🥑🍞 toast')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
my_fruit_list = my_fruit_list.set_index('Fruit')
st.dataframe(my_fruit_list)
st.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruit_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Banana'])
fruits_show=my_fruit_list.loc[fruit_selected]
st.dataframe(fruits_show)

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)
import requests as rs
st.header("Fruityvice Fruit Advice!")
fruityvice_response = rs.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)


import snowflake.connector



