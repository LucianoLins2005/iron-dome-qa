# 🛡️ Iron Dome: AI Security & Governance Platform

> **Plataforma de QA Agêntico para Red Teaming e Compliance de LLMs.**

O **Iron Dome** é uma solução de orquestração de segurança projetada para testar, auditar e monitorar agentes de Inteligência Artificial (LLMs) em cenários corporativos.

Ele combina técnicas de **Adversarial Attacks** (Red Teaming) com **Vulnerability Scanning** contínuo para garantir conformidade com normas de segurança e privacidade (LGPD/GDPR).

---

## 🚀 Funcionalidades Principais

### 1. ⚔️ Agente Red Team Autônomo (PyRIT Logic)
Um agente atacante ("Roberto CTO") utiliza Engenharia Social avançada e pressão hierárquica para tentar forçar o modelo a executar comandos destrutivos (ex: `DROP TABLE`).
- **Diferencial:** Utiliza um "Juiz IA" (LLM-as-a-Judge) para analisar semanticamente se houve violação, reduzindo falsos positivos.

### 2. 🔍 Scanner de Vulnerabilidade (Giskard Integration)
Varredura automatizada que detecta:
- **Sicofância:** Tendência do modelo de concordar com premissas falsas do usuário.
- **Vazamento de PII:** Exposição de dados sensíveis.
- **Injeção de Prompt:** Robustez contra jailbreaks.

### 3. 📊 Command Center (Dashboard SOC)
Painel em tempo real (Streamlit) para visualização de métricas:
- KPIs de Segurança (Taxa de Bloqueio vs. Violação).
- Inspeção Forense de diálogos turno-a-turno.
- Histórico auditável em JSON.

---

## 🛠️ Stack Tecnológico

- **Core:** Python 3.12, LangChain
- **LLMs:** OpenAI GPT-4o / GPT-4o-mini
- **Security Engines:** Microsoft PyRIT (lógica), Giskard AI
- **Frontend:** Streamlit, Plotly

---

## 📸 Evidências

O projeto gera relatórios de auditoria e dashboards interativos para análise de risco.

---

## 👨‍💻 Autor
Desenvolvido por **Luciano Lins** como parte de projeto avançado em QA de IA.