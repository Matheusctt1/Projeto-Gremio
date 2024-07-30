import streamlit as st
import controles.controleJogo as controle


def pageVisuIndividual():
    df = controle.mostrarBanco()


    st.sidebar.header('Funções:', divider='gray')
    funcoes = ['Excluir', 'Filtrar por Adversario']
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
    
    if (option == 'Filtrar por Adversario'):
        filtrarADV = st.sidebar.multiselect(
            'Selecione o Adversario:',
            df['Adversario+data'].unique()
        )
        if filtrarADV:
            ADV = st.sidebar.button('Filtrar')
            if ADV:
                controle.filtrar(filtrarADV)
                

                 