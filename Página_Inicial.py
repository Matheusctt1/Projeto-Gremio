# Pagina de rosto do App

import streamlit as st
st.set_page_config(
    page_title = ${{ vars.PAGETITLE }},
    page_icon = ${{ vars.PAGEICON }},
    layout="wide",
    initial_sidebar_state='auto'
)
import page.pageCadastroIndividual as cadastroBancoIndividual
import page.paginaInicial as paginaInicial
import page.visuIndividual as PageVisuIndiv
import page.visuGoleiros as PageVisuGoleiros
import page.visuColetivo as PageVisuColetivo
import page.visuAdversario as PageVisuAdversario
import page.pageAtletas as PageAtletas



st.sidebar.header('Menu')

Page_cliente = st.sidebar.selectbox(
    'Ferramentas', ['Pagina Inicial', 'Cadastro Banco de Dados', 'Cadastro Atletas', 'Visualizar BD. Individual', 'Visualizar BD. Goleiros', 'Visualizar BD. Coletivo', 
                    'Visualizar BD. Adversario'], 0)

if Page_cliente == 'Pagina Inicial':
  paginaInicial.exibirPagina()

if Page_cliente == 'Cadastro Banco de Dados':
  cadastroBancoIndividual.cadastrar()

if Page_cliente  == 'Cadastro Atletas':
  PageAtletas.cadastrar()

if Page_cliente == 'Visualizar BD. Individual':
  PageVisuIndiv.pageVisuIndividual()

if Page_cliente == 'Visualizar BD. Goleiros':
  PageVisuGoleiros.pageVisuGoleiros()

if Page_cliente == 'Visualizar BD. Coletivo':
  PageVisuColetivo.pageVisuColetivo()

if Page_cliente == 'Visualizar BD. Adversario':
  PageVisuAdversario.pageVisuAdversario()

with st.sidebar.container(border=None):
        st.sidebar.image(image = ${{ vars.SIDEBARIMAGE }}, width=220)



