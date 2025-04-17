import streamlit as st
import requests
import plotly.express as px
import pandas as pd

API_URL = "http://backend:5000"

st.set_page_config(page_title="Monitoramento de Rede", layout="wide")
st.title("📡 Monitoramento de Tráfego de Rede")

# Indicadores rápidos
col1, col2, col3 = st.columns(3)

# Formulário de novo dispositivo
st.subheader("➕ Registrar novo dispositivo")
with st.form("register_form"):
    ip = st.text_input("Endereço IP")
    name = st.text_input("Nome do dispositivo")
    traffic = st.number_input("Taxa de tráfego (Mbps)", min_value=0.0)
    submitted = st.form_submit_button("Registrar")
    if submitted:
        response = requests.post(f"{API_URL}/devices", json={
            "ip": ip,
            "name": name,
            "traffic": traffic
        })
        if response.status_code == 201:
            st.success("✅ Dispositivo registrado com sucesso!")
            st.rerun()
        else:
            st.error("❌ Erro ao registrar dispositivo.")

# Dados dos dispositivos
st.subheader("📋 Dispositivos registrados")
response = requests.get(f"{API_URL}/devices")
if response.status_code == 200:
    devices = response.json()
    if devices:
        df = pd.DataFrame(devices)

        # Indicadores rápidos
        col1.metric("Total de dispositivos", len(df))
        col2.metric("Tráfego médio (Mbps)", f"{df['traffic'].mean():.2f}")
        col3.metric("Alto Tráfego", df[df["traffic"] > 50].shape[0])

        # Gráfico de barras
        st.markdown("### 📊 Tráfego por Dispositivo")
        fig = px.bar(df, x="name", y="traffic", color=df["traffic"] > 50,
                     labels={"traffic": "Taxa de Tráfego (Mbps)", "name": "Dispositivo"},
                     color_discrete_map={True: "red", False: "green"},
                     title="Dispositivos e suas taxas de tráfego")
        st.plotly_chart(fig, use_container_width=True)

        # Lista com botões de remoção
        st.markdown("### 🧾 Lista de Dispositivos")
        for device in devices:
            status = "🔴 Alto" if device['traffic'] > 50 else "🟢 Normal"
            st.write(f"**{device['name']}** ({device['ip']}) → {device['traffic']} Mbps - {status}")
            if st.button(f"Remover {device['name']}", key=device['id']):
                del_res = requests.delete(f"{API_URL}/devices/{device['id']}")
                if del_res.status_code == 200:
                    st.success("Dispositivo removido.")
                    st.rerun()
    else:
        st.info("Nenhum dispositivo cadastrado.")
else:
    st.error("Erro ao carregar dados.")