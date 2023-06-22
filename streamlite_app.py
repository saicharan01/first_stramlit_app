
import snowflake.connector
conn = snowflake.connector.connect(
    user='SAICHARAN11',
    password='Saicharan@11',
    account='bc34544.central-india.azure',
    warehouse='DEMO_WH',
    database='MY_DB',
    schema='MY_SCH'
)



cursor = conn.cursor()
cursor.execute("SELECT * FROM SALES")
results = cursor.fetchall()



import streamlit as st
st.write(results)



!pip install streamlit
!pip install pyngrok



%%writefile app.py



!streamlit run app.py
