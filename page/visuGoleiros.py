import streamlit as st
import controles.controleGoleiro as controle



def pageVisuGoleiros():
    df = controle.mostrarBanco()


    st.sidebar.header('Funções:', divider='gray')
    funcoes = ['Excluir']
    option= st.sidebar.selectbox(
            'Selecione uma função:',
            options= funcoes, 
            placeholder='Selecione uma Opção',
            index=None
    )

    if (option == 'Excluir'):
        excluiLinha = st.sidebar.multiselect(
            'Selecione o ID da linha:',
            df['ID']
        )
        if excluiLinha:
            excluirID = st.sidebar.button('Excluir')
            if excluirID:
                controle.excluir(excluiLinha)
                