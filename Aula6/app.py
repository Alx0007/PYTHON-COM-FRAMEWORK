import streamlit as st
from abc import ABC, abstractmethod
import datetime


st.set_page_config(page_title='POO e Streamlit')
st.title('Laboratório de testes')


class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo =  titulo
        self.autor = autor
        self.ano = ano
        self.lista  = []
    
    def cadastro_livro(self):
        self.lista.extend([self.titulo, self.autor, self.ano])
        return self.lista
    def __str__(self):
        st.write(self.lista)
        print(self.lista)







nome  = st.text_input('Digite o nome do livro')
autor = st.text_input('Digite o nome do autor')
ano = st.date_input('Digite o ano')
l = Livro(nome, autor, ano)
l.cadastro_livro()





if st.button('Salvar na lista'):


    st.success('Dado cadastrado') 
l.__str__()


    




        