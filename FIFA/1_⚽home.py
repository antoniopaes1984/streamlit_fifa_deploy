import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in  st.session_state:
    df_data = pd.read_csv("FIFA/datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"]>=datetime.today().year]
    df_data = df_data[df_data["Value(£)"]>0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown("#FIFA23 OFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por Antônio Paes")

btn = st.link_button("Acesse os dados no Kaggle","https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")




st.markdown(
    """
Esse site fornece o conjunto de dados do jogo FIFA 2025, para jogadores que gostem de aumentar sua
performance, atravé sde números e dados.
""")