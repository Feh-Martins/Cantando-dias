import streamlit as st
import datetime
import time
import base64

st.set_page_config(page_title="Contando os dias", page_icon="🌕")
# Função para converter a imagem local em base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Caminho da imagem no seu projeto (coloque a imagem na mesma pasta do código ou em uma subpasta)
image_path = "./WhatsApp Image 2025-03-11 at 20.32.28 (1).jpeg" # Alterar para o caminho correto

# Obtém o código base64 da imagem
base64_image = get_base64_of_image(image_path)

# Adicionando CSS para definir o fundo e deixar o texto branco
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("data:image/jpeg;base64,{base64_image}") no-repeat center center fixed;
        background-size: cover;
        color: white;  /* Deixa todo o texto branco */
    }}
    h1, h2, h3, h4, h5, h6, p, div, span {{
        color: white !important; /* Garante que todos os textos fiquem brancos */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Esperando a Boneca!!!")
st.write("Para a menina do olhar Hipnotizante ❤️")
st.write("Eu ja te enxerguei como essa princesa")
st.write("Tudo começou em - Mk, dia 04 de outubro de 2024 a mais ou menos 02:00h da madrugada!")
st.write("Eu te enxergava assim, como uma princesa!")
st.markdown("Deus e os santos daquela igreja são minhas testemunhas!")


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

    st.write("Você é como a Lua 🌕")
    st.write("Linda e muito longe de mim 💔!!!")
    
    time.sleep(1)
    st.rerun()
