# Calculadora de Tempo de Experiência

Ferramenta desenvolvida para apurar o tempo total de experiência profissional de forma ágil e precisa, especialmente voltada para a análise de pontuação e requisitos em **concursos públicos e editais de seleção**.

Muitas vezes, candidatos possuem vínculos de trabalho simultâneos (períodos concomitantes), e a soma simples pode gerar contagem duplicada. Esta calculadora resolve esse problema fundindo automaticamente os períodos sobrepostos em blocos únicos contínuos.

## Links de Acesso

- **Aplicação Online (Streamlit):** https://calculadoraexperiencia.streamlit.app/
- **Repositório no GitHub:** https://github.com/AlexJordane/calculadora_experiencia/

---

## Como funciona a lógica de cálculo

- **União de períodos concomitantes:** Se dois ou mais períodos possuem interseção de datas, eles são mesclados em um único intervalo contínuo para que nenhum dia seja contabilizado em duplicidade.
- **Contagem inclusiva:** Tanto a data de início quanto a data de fim são incluídas na soma de dias (`fim - início + 1`).
- **Padrão de tempo e arredondamento:**
  - **Em anos:** Considera-se o ano padrão de **365 dias**. Quando a sobra após os anos inteiros atinge **180 dias ou mais**, acrescenta-se 1 ano ao total arredondado.
  - **Em meses (versão HTML):** Considera-se o mês comercial de **30 dias**. Quando a sobra após os meses inteiros atinge **15 dias ou mais**, acrescenta-se 1 mês ao total arredondado.

---

## Versões disponíveis no repositório

O projeto conta com duas implementações equivalentes:

### 1. Versão Python / Streamlit (`calculadora_experiencia.py`)
Aplicação interativa construída em Python com **Streamlit**.
- Permite inserir múltiplos períodos dinâmicos.
- Calcula o total de dias sem sobreposição e o tempo em anos (com arredondamento).
- Exibe a lista detalhada dos períodos resultantes após a união das interseções.

**Como executar localmente:**
```bash
pip install streamlit
streamlit run calculadora_experiencia.py
```

### 2. Versão Web Standalone (`Calculadora.html`)
Aplicação em arquivo único (**HTML + CSS/Tailwind + JavaScript**), que roda diretamente no navegador sem necessidade de servidor ou instalação de pacotes.
- Interface responsiva com painel lateral explicativo retrátil.
- Apresenta o resultado em **anos arredondados** e **meses arredondados**, além do resumo de **total de dias**, **anos inteiros** e **dias restantes**.

**Como executar:**
Basta abrir o arquivo `Calculadora.html` em qualquer navegador web.

---

## Como usar

1. Insira a data de **Início** e **Fim** de cada período profissional (pares em branco são ignorados).
2. Caso precise de mais de 5 períodos, clique em **"Adicionar novo período"**.
3. Clique em **"Calcular Tempo de Experiência"** para visualizar os resultados.
4. Para limpar todos os campos e recomeçar, clique em **"Novo Cálculo"**.

---

## Autoria

Elaborado por **Alex Jordane**, em colaboração com Inteligência Artificial (Gemini 3.1 Pro e Canva).

