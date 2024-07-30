import streamlit as st
import services.dataBase as db
import pandas as pd



def cadastrarAtleta(atleta):
    count = db.cursor.execute("""
    INSERT INTO BD_ATLETAS ([Data_de_Cadastro],[Atleta],[vb_imagem])
    VALUES (?,?,?)""",
    atleta.dataCadastro, atleta.nome, atleta.file).rowcount
    db.cnxn.commit()

def exibirAtleta(nome):
    def init_connection():
            return db.cnxn

    conn = init_connection()


    query = f"""SELECT [vb_imagem] FROM BD_ATLETAS2 WHERE [Atleta] = '{nome}'"""
    df = pd.read_sql(query, conn)
                        
    return df