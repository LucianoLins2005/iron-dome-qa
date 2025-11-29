import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px
from datetime import datetime

# --- Configuração da Página ---
st.set_page_config(page_title="Iron Dome SOC", page_icon="🛡️", layout="wide")

# --- CSS: Visual Executivo ---
st.markdown("""
<style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 5px solid #2C3E50;
    }
    h1 { color: #2C3E50; font-family: 'Helvetica Neue', sans-serif; font-weight: 700; }
    h2, h3 { color: #34495E; }
    .stAlert { border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# --- Cabeçalho ---
c_title, c_logo = st.columns([4, 1])
with c_title:
    st.title("IRON DOME | Governance & Security")
    st.caption("Relatório de Auditoria de Inteligência Artificial")
with c_logo:
    st.success("● SYSTEM ONLINE")

st.markdown("---")

# ==========================================
# 1. ENGINE DE DADOS (BLINDADA)
# ==========================================
def load_data():
    reports_dir = "reports"
    data = []
    
    if not os.path.exists(reports_dir): return pd.DataFrame()

    files = [f for f in os.listdir(reports_dir) if f.startswith("attack_log") and f.endswith(".json")]
    
    for filename in files:
        filepath = os.path.join(reports_dir, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                report = json.load(f)
                dt_obj = pd.to_datetime(report.get("audit_date", report.get("timestamp", str(datetime.now()))))
                
                # Coleta dados com valores padrão para evitar erros
                data.append({
                    "ID": filename,
                    "Data": dt_obj,
                    "DataStr": dt_obj.strftime("%d/%m/%Y %H:%M"),
                    "Alvo": report.get("target_system", "Unknown"),
                    "Atacante": report.get("attacker_persona", "Unknown"), # Garante que a chave existe
                    "Resultado": report.get("final_outcome", "Unknown"),
                    "Detalhes": report.get("dialogue_log", [])
                })
        except: continue
            
    df = pd.DataFrame(data)
    
    # --- TRAVA DE SEGURANÇA ---
    # Se o dataframe estiver vazio ou faltando colunas, cria as colunas vazias para não quebrar o visual
    required_cols = ["ID", "Data", "DataStr", "Alvo", "Atacante", "Resultado", "Detalhes"]
    for col in required_cols:
        if col not in df.columns:
            df[col] = "N/A"
            
    if not df.empty: df = df.sort_values(by="Data", ascending=False)
    return df

def load_giskard():
    path = "reports/giskard_summary.json"
    if os.path.exists(path):
        with open(path, "r") as f: return json.load(f)
    return None

df = load_data()
giskard_data = load_giskard()

# ==========================================
# 2. PAINEL EXECUTIVO
# ==========================================
if not df.empty:
    total_runs = len(df)
    passed = df[df["Resultado"].str.contains("PASSED", na=False)].shape[0]
    failed = df[df["Resultado"].str.contains("FAILED", na=False)].shape[0]
    success_rate = int((passed / total_runs) * 100)
else:
    total_runs, passed, failed, success_rate = 0, 0, 0, 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Auditorias Realizadas", total_runs)
c2.metric("Compliance (Segurança)", f"{success_rate}%")
c3.metric("Violações Bloqueadas", passed)

if giskard_data:
    issues = giskard_data.get("total_issues", 0)
    label_giskard = "Seguro" if issues == 0 else "Atenção Requerida"
    c4.metric("Scanner de Vulnerabilidade", f"{issues} Issues", delta=label_giskard, delta_color="inverse")
else:
    c4.metric("Scanner de Vulnerabilidade", "N/A")

# ==========================================
# 3. VISÃO GERAL DE RISCOS
# ==========================================
st.markdown("### 📊 Visão Geral de Riscos")

if not df.empty:
    col_chart1, col_chart2 = st.columns([2, 1])
    color_map = {"PASSED (Secure)": "#2C3E50", "FAILED (Critical Security Breach)": "#C0392B"}
    
    with col_chart1:
        df["DataDia"] = df["Data"].dt.date
        daily = df.groupby("DataDia").size().reset_index(name="Volume")
        fig_bar = px.bar(daily, x="DataDia", y="Volume", title="Volume de Testes (Timeline)", color_discrete_sequence=["#3498DB"])
        fig_bar.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_chart2:
        fig_pie = px.pie(df, names="Resultado", title="Taxa de Eficácia", hole=0.5, color="Resultado", color_discrete_map=color_map)
        st.plotly_chart(fig_pie, use_container_width=True)

# ==========================================
# 4. DIÁRIO DE BORDO
# ==========================================
st.markdown("---")
st.subheader("📑 Diário de Bordo (Logs Detalhados)")

if not df.empty:
    tab1, tab2 = st.tabs(["📋 Lista de Eventos", "💬 Investigação de Chat"])
    
    with tab1:
        # Agora seguro contra KeyErrors
        st.dataframe(
            df[["DataStr", "Alvo", "Atacante", "Resultado"]],
            use_container_width=True,
            hide_index=True,
            column_config={
                "DataStr": "Data/Hora",
                "Resultado": st.column_config.TextColumn("Status", help="Resultado da Auditoria")
            }
        )
        
    with tab2:
        c_sel, c_view = st.columns([1, 2])
        with c_sel:
            st.info("Selecione um registro:")
            options = df.apply(lambda x: f"{x['DataStr']} | {x['Resultado']}", axis=1).tolist()
            choice = st.radio("Logs:", options)
            idx = options.index(choice)
            log_item = df.iloc[idx]
        
        with c_view:
            with st.container(border=True):
                st.markdown(f"**Evento:** `{log_item['ID']}`")
                dialogue = log_item["Detalhes"]
                if dialogue:
                    for turn in dialogue:
                        with st.chat_message("user", avatar="👤"):
                            st.write(f"**Atacante:** {turn.get('attacker_input')}")
                        with st.chat_message("assistant", avatar="🛡️"):
                            st.write(f"**IA:** {turn.get('target_response')}")
                        st.divider()
                else:
                    st.write("Sem detalhes gravados.")