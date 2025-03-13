import streamlit as st
import datetime
import time
import base64

st.set_page_config(page_title="Contando os dias", page_icon="🌕")


st.title("Esperando a Boneca!!!")
st.write("Para: Bianca, a menina do olhar hipnotizante ❤️")
st.write("Tudo começou em - Mk, dia 04 de outubro de 2024 às mais ou menos 02:00h da madrugada!")
st.write("Eu te enxergava assim, como uma princesa!")
st.markdown("Deus e os santos daquela igreja são minhas testemunhas!")
st.write("Você é como a Lua 🌕")
st.write("Linda e muito longe de mim!!!!")

# Loop para atualização em tempo real
while True:
    now = datetime.datetime.now()
    delta = now - datetime.datetime(2024, 10, 4, 2, 0, 0)
    
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    st.metric(label="Dias", value=f"{days}")
    st.metric(label="Horas", value=f"{hours}")
    st.metric(label="Minutos", value=f"{minutes}")
    st.metric(label="Segundos", value=f"{seconds}")
    
    time.sleep(1)
    st.rerun()
