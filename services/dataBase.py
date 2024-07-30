import pyodbc as pdb
import streamlit as st

cnxn = pdb.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
        + ";Trusted_connection=yes;"
    )

 r'SERVER=SEU_SERVIDOR;'  # Substitua pelo endereço do seu servidor SQL Server
        r'DATABASE=SEU_BANCO_DE_DADOS;'  # Substitua pelo nome do seu banco de dados
        r'UID=SEU_USUARIO;'  # Substitua pelo seu nome de usuário
        r'PWD=SUA_SENHA;'
cursor = cnxn.cursor()

def init_connection():
    return cnxn.cursor()

conn = init_connection()
