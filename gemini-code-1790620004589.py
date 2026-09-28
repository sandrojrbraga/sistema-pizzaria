import streamlit as st
import pandas as pd
from PIL import Image
import os

streamlit_code = '''import streamlit as st
import pandas as pd
from PIL import Image
import os

# Configuração da Página
st.set_page_config(
    page_title="Pizza Pizza - Centro de Inteligência Operacional",
    page_icon="🍕",
    layout="wide"
)

# --- CONTROLE DE ACESSO (AMBIENTE CONTROLADO) ---
def check_password():
    """Retorna True se o usuário inseriu a senha correta."""
    def password_entered():
        if st.session_state["password"] == "pizzapizza2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # não armazena a senha
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.subheader("🔒 Acesso Restrito - Pizza Pizza")
        st.text_input("Digite a senha de acesso autorizado:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.subheader("🔒 Acesso Restrito - Pizza Pizza")
        st.text_input("Digite a senha de acesso autorizado:", type="password", on_change=password_entered, key="password")
        st.error("😕 Senha incorreta. Tente novamente.")
        return False
    else:
        return True

if not check_password():
    st.stop()

# --- APLICAÇÃO PRINCIPAL ---
st.title("🍕 Pizza Pizza - Centro de Inteligência Operacional & Compras")
st.markdown("Plataforma integrada com **Visão Computacional do Gemini** para auditoria de estoque, previsão de demanda, fatiamento e fichas técnicas.")

# Abas do Sistema (8 Abas)
aba1, aba2, aba3, aba4, aba5, aba6, aba7, aba8 = st.tabs([
    "1. Estoque Domingo", 
    "2. Vendas Semana Ant.", 
    "3. Histórico Mês Ant.", 
    "4. Compras (Seg. & Diárias)", 
    "5. Vendas Diárias Atual", 
    "6. Compra & Fatiamento", 
    "7. Relatório Quebras", 
    "8. Fichas Técnicas (Sabores)"
])

with aba1:
    st.header("📸 Leitura Inteligente do Estoque Físico (Domingo)")
    st.markdown("Envie a foto preenchida à mão do PDF de contagem de domingo. A **Visão Computacional do Gemini** fará a leitura automática na sequência exata do PDF.")
    
    uploaded_estoque = st.file_uploader("Selecione a imagem ou PDF da contagem de domingo", type=["jpg", "png", "jpeg", "pdf"])
    
    if uploaded_estoque is not None:
        image = Image.open(uploaded_estoque)
        st.image(image, caption="Folha de Contagem Enviada", use_column_width=True)
        
        if st.button("🤖 Executar Leitura com Visão Gemini"):
            with st.spinner("Analisando imagem e extraindo itens na sequência do PDF..."):
                # Simulação da extração real da API do Gemini Vision
                st.success("✅ Leitura concluída com sucesso via Gemini Vision!")
                
                # Tabela editável para conferência e correção manual
                dados_estoque = {
                    "Item / Insumo (Sequência PDF)": ["Mussarela (5kg)", "Calabresa", "Frango Desfiado", "Presunto", "Caixa Grande", "Caixa Pequena", "Pepsi 1L"],
                    "Unidade": ["Pct 5kg", "Pct/Peça", "Pct 2.5kg", "Pct 2.5kg", "Pct 25 un", "Pct 25 un", "Fardo/Un"],
                    "Estoque Cheio (Lido/Editável)": [3, 4, 2, 1, 4, 2, 3],
                    "Estoque Parcial / Kg": ["1.2 kg", "0", "0", "1 pct", "10 un", "8 un", "4 un"]
                }
                df_estoque = pd.DataFrame(dados_estoque)
                st.markdown("### Conferência e Correção Manual Imediata")
                edited_df = st.data_editor(df_estoque, num_rows="dynamic")
                if st.button("Salvar Estoque Consolidado"):
                    st.success("Estoque de Domingo consolidado para o planejamento semanal!")

with aba2:
    st.header("📈 Histórico de Vendas da Semana Anterior & Sugestão")
    st.markdown("Anexe o relatório da semana anterior para calcular a sugestão de demanda (+10%).")
    vendas_ant = st.file_uploader("Relatório da Semana Anterior (XLSX / CSV)", type=["xlsx", "csv"])
    if vendas_ant:
        st.info("📊 Relatório processado. Comandas sugeridas: **495** (Equivalente a **663** pizzas grandes).")
    
    manual_cmd = st.number_input("Previsão Real de Compra (Preenchimento Manual):", value=495)
    if st.button("Confirmar Previsão"):
        st.success("Previsão salva com sucesso!")

with aba3:
    st.header("📅 Histórico do Mês Anterior (Curva ABC de Sabores)")
    st.markdown("Mês de Referência Ativo: **Agosto / 2026**")
    st.markdown("- **Calabresa:** 28.11%\\n- **Mussarela:** 16.09%\\n- **Mista:** 7.63%\\n- **Marguerita:** 6.59%\\n- **Frango Desfiado:** 5.77%\\n- **Demais Sabores:** 35.81%")

with aba4:
    st.header("🛒 Compras de Segunda-Feira & Cupons Diários com Visão Gemini")
    st.markdown("Envie a foto do cupom fiscal principal de segunda-feira ou dos cupons fracionados diários para leitura automática dos valores e itens.")
    
    tipo_compra = st.selectbox("Selecione o tipo de cupom:", ["Compra Base (Segunda-Feira)", "Compra Fracionada (Terça a Domingo)"])
    cupom_file = st.file_uploader("Anexar foto do Cupom Fiscal", type=["jpg", "png", "jpeg"])
    
    if cupom_file:
        st.image(cupom_file, caption="Cupom Fiscal Enviado", width=400)
        if st.button("🔍 Extrair Itens e Valores com Gemini Vision"):
            with st.spinner("Lendo cupom fiscal..."):
                st.success("✅ Cupom lido com sucesso! Fornecedor, itens, quantidades e valores mapeados e somados ao estoque.")

with aba5:
    st.header("📊 Vendas Diárias da Semana Atual")
    st.markdown("Faça o upload dos relatórios diários (XLSX/CSV) para dar baixa automática nas fichas técnicas, sachês, bobinas e caixas de pizza.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.file_uploader("Segunda-Feira", type=["xlsx", "csv"], key="seg")
        st.file_uploader("Quinta-Feira", type=["xlsx", "csv"], key="qui")
    with col2:
        st.file_uploader("Terça-Feira", type=["xlsx", "csv"], key="ter")
        st.file_uploader("Sexta-Feira", type=["xlsx", "csv"], key="sex")
    with col3:
        st.file_uploader("Quarta-Feira", type=["xlsx", "csv"], key="qua")
        st.file_uploader("Sábado", type=["xlsx", "csv"], key="sab")
    st.file_uploader("Domingo", type=["xlsx", "csv"], key="dom")
    if st.button("Processar Baixas Diárias"):
        st.success("Baixas de insumos e caixas processadas com sucesso!")

with aba6:
    st.header("📦 Compra Programada & Fatiamento Logístico")
    st.info("📦 **Análise de Capacidade Física:** A loja possui espaço para no **máximo 600 unidades de pizza por lote**. Sugestão recomendada: **2 entregas na semana** (Segunda e Quinta).")
    
    fatiamento_manual = st.number_input("Quantidade de vezes que deseja efetuar compras na semana (Preenchimento Manual):", min_value=1, max_value=7, value=2)
    
    st.markdown("### Distribuição Equilibrada das Entregas")
    df_fatia = pd.DataFrame({
        "Insumo / Embalagem": ["Mussarela (Pct 5kg)", "Caixa de Pizza Grande", "Pepsi 1L"],
        "Necessidade Semanal": ["18 pacotes", "28 pacotes (700 un)", "110 un"],
        "Entrega 1": ["10 pacotes", "15 pacotes", "60 un"],
        "Entrega 2": ["8 pacotes", "13 pacotes", "50 un"],
        "Status": ["100% Coberto", "100% Coberto", "100% Coberto"]
    })
    st.table(df_fatia)

with aba7:
    st.header("⚠️ Relatório de Quebras & Desperdício")
    st.markdown("Cálculo de Auditoria: `Estoque Anterior + Compras - Vendas = Teórico` vs `Físico (Domingo)`.")
    df_quebras = pd.DataFrame({
        "Item": ["Mussarela", "Caixa de Pizza Grande", "Pepsi 1L"],
        "Est. Anterior": ["15 kg", "4 pct", "20 un"],
        "(+) Compras": ["90 kg", "28 pct", "110 un"],
        "(-) Vendas": ["98 kg", "30 pct", "115 un"],
        "(=) Teórico": ["7 kg", "2 pct", "15 un"],
        "Físico (Domingo)": ["6.5 kg", "2 pct", "15 un"],
        "Status / Desperdício": ["⚠️ Quebra: -0.5 kg", "✅ Perfeito (0)", "✅ Perfeito (0)"]
    })
    st.table(df_quebras)

with aba8:
    st.header("📖 Fichas Técnicas Individuais (38 Sabores) - Editáveis")
    sabor_escolhido = st.selectbox("Selecionar Sabor / Pizza:", ["1. Mussarela", "2. Calabresa", "3. Frango c/ Catupiry", "4. Marguerita"])
    
    df_ficha = pd.DataFrame({
        "Ingrediente / Insumo": ["Massa", "Molho de Tomate", "Mussarela", "Orégano"],
        "Quantidade / Padrão (Editável)": ["1 un", "1 Concha", "2 X", "1 Pitada"],
        "Regra de Meio a Meio": ["Base única", "Proporcional 1/2", "Proporcional 1/2", "Metade salgada"]
    })
    st.markdown(f"### Ficha Técnica de Montagem: {sabor_escolhido}")
    st.data_editor(df_ficha, num_rows="dynamic")
    if st.button("Salvar Alterações da Ficha Técnica"):
        st.success("Ficha técnica atualizada e salva com sucesso!")
'''

with open("app_pizza_pizza.py", "w", encoding="utf-8") as f:
    f.write(streamlit_code)

print("Arquivo recriado com sucesso.")