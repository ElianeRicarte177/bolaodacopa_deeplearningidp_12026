# ⚽ Previsão da 1ª Rodada da Copa do Mundo 2026
### Deep Learning — Turma 1/2026 | Eliane Sa Ricarte | IDP Mestrado

Pipeline completo de Machine Learning para prever os placares dos 24 jogos da primeira rodada da fase de grupos da Copa do Mundo FIFA 2026, utilizando TensorFlow/Keras.

---

## 🎯 Hipótese central

A força histórica relativa entre duas seleções — capturada pelo rating ELO — combinada com a forma recente de cada equipe e a importância do torneio em que jogaram, contém informação suficiente para prever o placar esperado de um jogo internacional de futebol.

---

## 📂 Estrutura do repositório

```
├── bolao_copa.txt                          → Previsões finais (formato oficial)
├── Bolão da Copa do Mundo - Eliane Ricarte - 1 2026.ipynb  → Notebook principal
├── Mapeamento_Selecoes.py                  → Mapeamento nome ↔ sigla das 48 seleções
├── Resultados_Internacionais_1872_2026.csv → Base principal (49.287 partidas)
├── FIFA_World_Rankings_1992_2024.csv       → Rankings FIFA mensais por seleção
├── FIFA_Rankings_Partidas_Cruzados_1992_2022.csv → Rankings cruzados com resultados
├── Copa_America_Historico_desde_1916.csv   → Estatísticas históricas da Copa América
├── WC2026_ODS.csv                          → Odds 1X2 dos 24 jogos (coleta mai/2026)
└── Duelo das IAs/                          → Previsões de 5 LLMs para comparação
    ├── previsoes_Claude.json
    ├── previsoes_ChatGPT.json
    ├── previsoes_Gemini.json
    ├── previsoes_Copilot.json
    ├── previsoes_Grok.json
    └── previsoes_consolidado.json
```

---

## 🗄️ Dados

| Base | Fonte | Período | Conteúdo |
|---|---|---|---|
| Resultados Internacionais | Kaggle (martj42) | 1872–2026 | 49.287 partidas internacionais |
| FIFA World Rankings | Kaggle (cashncarry) | 1992–2024 | Rankings mensais por seleção |
| Rankings + Partidas Cruzados | Kaggle (gabipana7) | 1992–2022 | Rankings cruzados com resultados |
| Copa América Histórico | Kaggle | 1916–2024 | Estatísticas da Copa América |
| Transfermarkt Datasets | GitHub (dcaribou) | Atualizado | WC, Euro, Copa América, AFCON, Asian Cup |
| Odds WC2026 | Oddschecker (coleta manual) | Mai/2026 | Odds 1X2 dos 24 jogos da 1ª rodada |

Todas as 48 seleções participantes da Copa 2026 estão presentes na base de resultados.

---

## ⚙️ Pré-processamento

### Pesos por tipo de torneio

Nem todos os jogos têm o mesmo valor informativo. Foram atribuídos pesos diferentes a cada tipo de torneio:

| Peso | Torneios |
|---|---|
| 1.0 | FIFA World Cup |
| 0.9 | Copa América, AFCON, UEFA Euro, AFC Asian Cup |
| 0.8 | Eliminatórias (todas as confederações), Gold Cup |
| 0.7 | UEFA Nations League, CONCACAF Nations League |
| 0.3 | Amistosos e demais torneios |

### Rating ELO

Sistema de pontuação dinâmico que avalia a força histórica de cada seleção:
- Todas as seleções iniciam com **1500 pontos**
- Fator de atualização **K = 30**, ponderado pelo peso do torneio
- Calculado de forma incremental sobre todos os 49.287 jogos (1872–2026)
- O ELO no momento de cada jogo é usado como feature, sem vazamento de dados futuros

### Forma recente

Média das estatísticas dos últimos **10 jogos** de cada seleção antes da data de referência:
- Gols marcados por jogo
- Gols sofridos por jogo
- Pontos por jogo (3/1/0)

### Campo neutro

A Copa do Mundo é disputada em campo neutro (EUA, Canadá e México). O modelo v2 inclui a variável `neutral` como feature, e todos os 24 jogos da previsão foram setados com `neutral = 1`.

---

## 🧠 Modelo TensorFlow

### Abordagem: Regressão de Poisson Dupla

O modelo prevê independentemente a taxa esperada de gols (λ) de cada seleção. O placar final é obtido arredondando essas taxas para o inteiro mais próximo. Essa abordagem respeita a natureza discreta e assimétrica da distribuição de gols no futebol.

### Arquitetura (Modelo v2 — final)

```
Input (11 features)
    └── Dense(128, relu)
    └── Dropout(0.3)
    └── Dense(64, relu)
    └── Dropout(0.2)
    └── Dense(32, relu)
    ├── Dense(1, softplus) → gols_home
    └── Dense(1, softplus) → gols_away
```

### Features de entrada (11)

| Feature | Descrição |
|---|---|
| `elo_diff` | Diferença de ELO entre mandante e visitante |
| `elo_home` | ELO absoluto do time 1 |
| `elo_away` | ELO absoluto do time 2 |
| `forma_home_gm` | Gols marcados/jogo (time 1, últimos 10 jogos) |
| `forma_home_gs` | Gols sofridos/jogo (time 1, últimos 10 jogos) |
| `forma_home_pts` | Pontos/jogo (time 1, últimos 10 jogos) |
| `forma_away_gm` | Gols marcados/jogo (time 2, últimos 10 jogos) |
| `forma_away_gs` | Gols sofridos/jogo (time 2, últimos 10 jogos) |
| `forma_away_pts` | Pontos/jogo (time 2, últimos 10 jogos) |
| `peso` | Importância do torneio (1.0 = Copa do Mundo) |
| `neutral_int` | Campo neutro (0 ou 1) |

### Configuração de treino

- **Otimizador:** Adam
- **Função de perda:** Poisson (para cada saída)
- **Callbacks:** EarlyStopping (patience=10) + ReduceLROnPlateau (patience=5)
- **Batch size:** 64 | **Épocas máximas:** 100
- **Sementes fixadas:** `tf.random.set_seed(42)`, `np.random.seed(42)`

### Split temporal (sem vazamento de dados)

| Conjunto | Período | Uso |
|---|---|---|
| Treino | até 31/12/2021 | Ajuste dos pesos |
| Validação | 2022–2023 | EarlyStopping e ReduceLR |
| Teste | 2024–2026 | Avaliação final |

---

## 📊 Avaliação

### Comparação entre versões

| Modelo | Val Loss | Épocas | Diferencial |
|---|---|---|---|
| v1 — sem correção de campo neutro | 1.5398 | 16 | baseline |
| v2 — com correção de campo neutro | 1.5346 | 12 | ✅ melhor e mais rápido |

### Métricas no conjunto de teste (2.391 jogos, 2024–2026)

| Métrica | Resultado | Referência |
|---|---|---|
| Acurácia no resultado (W/D/L) | **55.5%** | Random baseline: 33% |
| Acurácia no placar exato | **9.6%** | Literatura: 8–12% |

### Estimativa de pontuação no bolão

| Cenário | Acertos resultado | Acertos placar | Pontos estimados |
|---|---|---|---|
| Base (55.5% / 9.6%) | ~13 jogos | ~2 jogos | **~36 / 120** |
| Otimista (confrontos assimétricos) | ~15 jogos | ~3 jogos | **~45 / 120** |

---

## 🎲 Previsões finais — 24 jogos

| Jogo | Grupo | Seleção 1 | Placar | Seleção 2 |
|---|---|---|---|---|
| 1 | A | MEX | 2 – 1 | RSA |
| 2 | A | KOR | 1 – 1 | CZE |
| 3 | B | CAN | 2 – 1 | BIH |
| 4 | D | USA | 1 – 1 | PAR |
| 5 | C | HAI | 1 – 1 | SCO |
| 6 | D | AUS | 1 – 1 | TUR |
| 7 | C | BRA | 1 – 1 | MAR |
| 8 | B | QAT | 1 – 2 | SUI |
| 9 | E | CIV | 1 – 1 | ECU |
| 10 | E | GER | 2 – 1 | CUW |
| 11 | F | NED | 1 – 1 | JPN |
| 12 | F | SWE | 1 – 1 | TUN |
| 13 | H | KSA | 1 – 1 | URU |
| 14 | H | ESP | 3 – 1 | CPV |
| 15 | G | IRN | 2 – 1 | NZL |
| 16 | G | BEL | 2 – 1 | EGY |
| 17 | I | FRA | 2 – 1 | SEN |
| 18 | I | IRQ | 1 – 1 | NOR |
| 19 | J | ARG | 2 – 1 | ALG |
| 20 | J | AUT | 2 – 1 | JOR |
| 21 | L | GHA | 1 – 1 | PAN |
| 22 | L | ENG | 2 – 1 | CRO |
| 23 | K | POR | 2 – 1 | COD |
| 24 | K | UZB | 1 – 1 | COL |

> O modelo apostou em empate em **13 dos 24 jogos** — reflexo direto do histórico real do futebol internacional, onde empates são mais comuns do que o senso comum sugere.

---

## ⚠️ Principais incertezas

- **Empates são imprevisíveis:** mesmo os melhores modelos da literatura atingem apenas ~30% de F1 para empates. A 1ª rodada historicamente tem ~26% de empates.
- **Lesões e escalações de última hora:** informações não disponíveis nos dados históricos.
- **Seleções estreantes ou com pouco histórico:** Curaçao, Cabo Verde e Uzbequistão têm bases de dados reduzidas.

---

## 🔧 Dependências

```
Python        3.11.15
TensorFlow    2.19.0
pandas
numpy
scikit-learn
duckdb
```

---

## 🚀 Como reproduzir

1. Clone o repositório
2. Instale as dependências: `pip install tensorflow pandas numpy scikit-learn duckdb`
3. Execute o notebook `Bolão da Copa do Mundo - Eliane Ricarte - 1 2026.ipynb` do início ao fim
4. O arquivo `bolao_copa.txt` será gerado automaticamente na última célula

> As sementes aleatórias estão fixadas (`seed=42`). Pequenas variações nos resultados são possíveis dependendo do hardware e da versão exata das bibliotecas.

---

*Projeto acadêmico — Mestrado | Disciplina de Deep Learning | Prof. Danny (IDP) | Turma 1/2026*
