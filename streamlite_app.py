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
# Let's put a pick list here so they can pick the fruit they want to include 
st.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
st.dataframe(my_fruit_list)


import snowflake.connector
conn = snowflake.connector.connect(
    user='SAICHARAN11',
    password='Saicharan@11',
    account='bc34544.central-india.azure',
    warehouse='DEMO_WH',
    database='MY_DB',
    schema='MY_SCH'
)
st.dataframe(sales)
