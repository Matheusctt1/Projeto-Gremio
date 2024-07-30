import pyodbc as pdb
import streamlit as st

server= 'GFBPA-AS222472'
database= 'BD_Gremio'
username= 'cdd.base'
password= '@tricolor1903'

cnxn = pdb.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";Trusted_connection=yes;"
    )
cursor = cnxn.cursor()

def init_connection():
    return cnxn.cursor()

conn = init_connection()