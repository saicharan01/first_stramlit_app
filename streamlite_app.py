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
fruit_list=pandas.read_cvs("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(fruit_list)
