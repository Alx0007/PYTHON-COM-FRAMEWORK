import streamlit as st

st.set_page_config(page_title='Portfólio Streamlit:')
st.title('Portfólio streamlit')

st.image("images.jpg")

st.title("Alexandre Lacerda")
st.subheader("Estudante SENAI")
st.write("Acesse meu perfil no GitHub: https://github.com/Alx0007")

st.divider()

st.subheader("Contato e Localização")
st.write("E-mail: alexandre.senai@senai.com")
st.write("WhatsApp: +55 (11) 98948-5788")
st.write("Endereço: Rua Galapagos, nº 07, Bairro Vila Velha - Guarulhos/SP")

st.divider()

st.subheader("Música")
st.audio("Metallica_ One.mp3")