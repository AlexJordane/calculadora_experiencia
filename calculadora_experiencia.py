import streamlit as st
from datetime import datetime, date

def mesclar_periodos(periodos):
    # Filtra períodos válidos (onde início e fim foram preenchidos corretamente)
    periodos_validos = [p for p in periodos if p[0] and p[1] and p[0] <= p[1]]
    if not periodos_validos:
        return []

    # Ordena os períodos de forma crescente pela data de início
    periodos_ordenados = sorted(periodos_validos, key=lambda x: x[0])
    periodos_mesclados = [periodos_ordenados[0]]

    # Investiga e resolve as sobreposições de tempo
    for inicio_atual, fim_atual in periodos_ordenados[1:]:
        inicio_anterior, fim_anterior = periodos_mesclados[-1]

        if inicio_atual <= fim_anterior:
            # Há interseção: alargamos a janela de tempo fundindo as datas
            periodos_mesclados[-1] = (inicio_anterior, max(fim_anterior, fim_atual))
        else:
            # Não há interseção: a janela anterior fecha e iniciamos uma nova
            periodos_mesclados.append((inicio_atual, fim_atual))

    return periodos_mesclados

def calcular_tempo(periodos_mesclados):
    total_dias = 0
    for inicio, fim in periodos_mesclados:
        # Adicionamos 1 dia para que o período seja inclusivo
        total_dias += (fim - inicio).days + 1 

    # Conversão padrão para apresentar os resultados
    anos = total_dias // 365
    resto_dias = total_dias % 365
    meses = resto_dias // 30
    dias = resto_dias % 30

    # Arredondamento conforme solicitado
    anos_arredondados = anos + 1 if meses >= 6 else anos

    return total_dias, anos, meses, dias, anos_arredondados

def limpar_dados():
    # Restabelece o número de períodos e avança o contador de recomeço
    st.session_state.num_periodos = 5
    st.session_state.contador_recomeco += 1

# --- Configuração da Barra Lateral ---
with st.sidebar:
    st.header("Sobre a Calculadora")
    st.write("""
    Esta ferramenta foi criada para oferecer agilidade no cálculo do tempo de experiência de trabalho. 
    Especialmente para situações que envolvem o cálculo de tempo em concursos públicos e editais de seleção.  
    Muitas vezes, os períodos de experiência são concomitantes e a contagem tradicional pode levar a erros de cálculo, resultando em uma contagem duplicada do tempo.
    A calculadora foi projetada para lidar com essas situações, unindo os períodos de experiência concomitantes, garantindo uma contagem precisa do tempo total de experiência.
    
    **Como funciona a lógica:**
    - **União de períodos:** Se dois períodos de trabalho possuem datas concomitantes, a calculadora os une em um único bloco contínuo.
    - **Padrão de tempo:** Para os cálculos, consideramos o ano com 365 dias e o mês com 30 dias.
    - **Arredondamento:** Quando o tempo restante após o cálculo dos anos inteiros atinge 6 meses ou mais, ele é contado como um novo ano completo.
    """)
    
    st.write("---")
    
    st.header("Como usar")
    st.markdown("""
    1. Insira a data de início e fim de cada período.
    2. Caso sejam necessários mais de 5 períodos, clique em **"Adicionar novo período"**.
    3. Depois de inserir todas as datas, clique em **"Calcular Tempo de Experiência"**.
    4. Para um novo cálculo, clique em **"Novo Cálculo"**.
    """)

    st.write("---")
    st.caption("Elaborada por Alex Jordane, em colaboração com Inteligência Artificial, Gemini 3.1 Pro.")

# --- Interface Principal ---
st.title("Calculadora de Tempo de Experiência")
st.write("Elaborado por Alex Jordane, em colaboração com Inteligência Artificial, Gemini 3.1 Pro.")
st.write("Por favor, insira as datas de início e fim para cada período profissional.")

# Gerenciamento do número de períodos e do contador de limpeza
if 'num_periodos' not in st.session_state:
    st.session_state.num_periodos = 5
if 'contador_recomeco' not in st.session_state:
    st.session_state.contador_recomeco = 0

periodos_inseridos = []

# Criação colaborativa dos campos de data com chaves dinâmicas
for i in range(st.session_state.num_periodos):
    col1, col2 = st.columns(2)
    with col1:
        data_inicio = st.date_input(
            f"Início do Período {i+1}", 
            # A chave agora carrega o contador, renovando-se ao limpar
            key=f"inicio_{i}_{st.session_state.contador_recomeco}", 
            format="DD/MM/YYYY", 
            value=None,
            min_value=date(1950, 1, 1),
            max_value=date(2050, 12, 31)
        )
    with col2:
        data_fim = st.date_input(
            f"Fim do Período {i+1}", 
            # A chave agora carrega o contador, renovando-se ao limpar
            key=f"fim_{i}_{st.session_state.contador_recomeco}", 
            format="DD/MM/YYYY", 
            value=None,
            min_value=date(1950, 1, 1),
            max_value=date(2050, 12, 31)
        )
    periodos_inseridos.append((data_inicio, data_fim))

st.write("---")

# Distribuição dos botões em três colunas para manter a harmonia visual
col_btn1, col_btn2, col_btn3 = st.columns(3)

with col_btn1:
    if st.button("Adicionar novo período"):
        st.session_state.num_periodos += 1
        st.rerun()

with col_btn2:
    calcular = st.button("Calcular Tempo de Experiência", type="primary")

with col_btn3:
    if st.button("Novo Cálculo"):
        limpar_dados()
        st.rerun()

# Apresentação dos resultados
if calcular:
    periodos_mesclados = mesclar_periodos(periodos_inseridos)

    if not periodos_mesclados:
        st.warning("Gentilmente, verifique se todas as datas foram preenchidas e se a ordem cronológica está correta.")
    else:
        total_dias, anos, meses, dias, anos_arredondados = calcular_tempo(periodos_mesclados)

        st.subheader("Resultados:")
        st.write(f"**(1) Total em dias:** {total_dias} dias")
        st.write(f"**(2) Anos, meses e dias:** {anos} anos, {meses} meses e {dias} dias")
        st.write(f"**(3) Anos (arredondado):** {anos_arredondados} anos")

        st.write("---")
        st.write("**Detalhes dos períodos considerados (após unir interseções):**")
        for inicio, fim in periodos_mesclados:
            st.write(f"- De {inicio.strftime('%d/%m/%Y')} a {fim.strftime('%d/%m/%Y')}")
