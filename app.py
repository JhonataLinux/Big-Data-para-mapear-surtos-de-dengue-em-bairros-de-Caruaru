import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from numpy.random import default_rng as rng

# Configuração da página
st.set_page_config(page_title="Monitoramento Aedes - Caruaru", layout="wide")

# Carrega os dados
df = pd.read_csv("bairros_caruaru.csv", delimiter='\t')

# Dados de exemplo para os bairros com focos
bairros_com_focos = ['Petropolis', 'Vassoural', 'Cedro', 'Rendeiras', 'Salgado']
df['focos_confirmados'] = 0

# Atribui valores de exemplo
for bairro in bairros_com_focos:
    df.loc[df['name'] == bairro, 'focos_confirmados'] = [15, 8, 12, 20, 6][bairros_com_focos.index(bairro)]

# CORREÇÃO: Usar códigos hexadecimais para cores
def get_color(focos):
    if focos > 15: return '#FF0000'  # Vermelho
    elif focos > 8: return '#FFA500'  # Laranja
    elif focos > 0: return '#FFFF00'  # Amarelo
    else: return '#00FF00'  # Verde

df['color'] = df['focos_confirmados'].apply(get_color)

# Título principal
st.title("🦟 Monitoramento de Focos do Aedes em Caruaru")

# Usar abas para organizar
tab1, tab2 = st.tabs(["🗺️ Mapa Interativo", "📊 Dados Detalhados"])

with tab1:
    st.subheader("🌍 Mapa de Focos do Aedes em Caruaru")
    
    # Legenda
    st.markdown("""
    **Legenda:**
    - 🔴 Alto Risco (15+ focos)
    - 🟠 Médio Risco (8-14 focos) 
    - 🟡 Baixo Risco (1-7 focos)
    - 🟢 Sem focos registrados
    """)
    
    # Apenas UM mapa com todas as informações
    st.map(df,
           latitude='latitude',
           longitude='longitude',
           size=100,
           color='color')

with tab2:
    st.subheader("📍 Bairros com Focos do Aedes")
    
    # Filtra bairros com focos
    df_com_focos = df[df['focos_confirmados'] > 0].copy()
    
    if not df_com_focos.empty:
        # Mostra tabela em vez de segundo mapa
        st.write("**Bairros com focos confirmados:**")
        
        # Ordena por quantidade de focos
        df_com_focos = df_com_focos.sort_values('focos_confirmados', ascending=False)
        
        # Mostra dados em formato de tabela
        for _, row in df_com_focos.iterrows():
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{row['name']}**")
            with col2:
                st.write(f"**{int(row['focos_confirmados'])}** focos")
            with col3:
                risco = "Alto" if row['focos_confirmados'] > 15 else "Médio" if row['focos_confirmados'] > 8 else "Baixo"
                st.write(f"`{risco} risco`")
            st.divider()
        
        # Estatísticas
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total de Bairros com Focos", len(df_com_focos))
        with col2:
            st.metric("Total de Focos", int(df_com_focos['focos_confirmados'].sum()))
        with col3:
            st.metric("Média de Focos por Bairro", f"{df_com_focos['focos_confirmados'].mean():.1f}")
        with col4:
            max_focos = df_com_focos ['focos_confirmados'].max()
            bairro_max = df_com_focos.loc[df_com_focos['focos_confirmados'].idxmax(), 'name']
            st.metric("Maior Foco", f"{int(max_focos)}({bairro_max})")
        st.subheader("📍 Bairros com Focos do Aedes")
        if not df_com_focos.empty:
            st.map(df_com_focos,
                latitude='latitude',
                longitude='longitude',
                color='#FF0000')
        else:
             st.success("🎉 Nenhum foco registrado!")

# Informações adicionais na sidebar
with st.sidebar:
    st.header("ℹ️ Informações")
    st.write("""
    Este dashboard monitora os focos do mosquito Aedes aegypti 
    nos bairros de Caruaru.
    
    **Fonte:** Dados simulados para demonstração
    """)
    
    # Filtro rápido
    st.subheader("🔍 Filtro Rápido")
    risco_selecionado = st.selectbox(
        "Nível de risco:",
        ["Todos", "Alto Risco", "Médio Risco", "Baixo Risco"]
    )
    
    if risco_selecionado != "Todos":
        if risco_selecionado == "Alto Risco":
            filtrado = df[df['focos_confirmados'] > 15]
        elif risco_selecionado == "Médio Risco":
            filtrado = df[(df['focos_confirmados'] > 8) & (df['focos_confirmados'] <= 15)]
        else:
            filtrado = df[(df['focos_confirmados'] > 0) & (df['focos_confirmados'] <= 8)]
        
        st.write(f"**{len(filtrado)}** bairros com {risco_selecionado.lower()}")