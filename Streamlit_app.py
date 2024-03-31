import streamlit as st
import snowflake.connector
import pandas as pd

st.title("Zena's Amazing Athleisure Catalog")

# Connect to Snowflake
cnx = st.connection('snowflake')
session = cnx.session()

# Run a Snowflake query

my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")

st.dataframe(data=my_dataframe, use_container_width=True)
