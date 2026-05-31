# ⚽ Batalha de IAs — Bolão da Copa do Mundo 2026

Previsões de placar da **1ª Rodada da Copa do Mundo FIFA 2026** geradas por uma rede neural treinada com TensorFlow e por 5 modelos de linguagem (LLMs), para fins de comparação e competição em bolão acadêmico.

---

## 🤖 Participantes

| Participante | Tipo | Detalhes |
|---|---|---|
| **Rede Neural** | MLP (TensorFlow/Keras) | Treinada sobre 49.000+ partidas internacionais (1872–2026) |
| Claude | LLM | Anthropic — Sonnet 4 |
| ChatGPT | LLM | OpenAI — GPT-4o |
| Gemini | LLM | Google |
| Copilot | LLM | Microsoft |
| Grok | LLM | xAI |

---

## 📂 Arquivos

```
bolao_copa.txt              → Previsões da rede neural (formato oficial do professor)
previsoes_Claude.json       → Previsões do Claude
previsoes_ChatGPT.json      → Previsões do ChatGPT
previsoes_Gemini.json       → Previsões do Gemini
previsoes_Copilot.json      → Previsões do Copilot
previsoes_Grok.json         → Previsões do Grok
previsoes_consolidado.json  → Todas as previsões lado a lado por jogo
```

> **Atenção:** todos os arquivos seguem a **ordem oficial dos 24 jogos** definida pelo professor Danny (Prof. Danny IDP), conforme a tabela abaixo.

---

## 🗓️ Ordem oficial dos jogos (1ª Rodada)

| Jogo | Grupo | Data | Seleção 1 | Seleção 2 |
|------|-------|------|-----------|-----------|
| 1 | A | 11/06 | MEX — México | RSA — África do Sul |
| 2 | A | 11/06 | KOR — Coreia do Sul | CZE — Tchéquia |
| 3 | B | 12/06 | CAN — Canadá | BIH — Bósnia e Herzegovina |
| 4 | D | 12/06 | USA — Estados Unidos | PAR — Paraguai |
| 5 | C | 13/06 | HAI — Haiti | SCO — Escócia |
| 6 | D | 13/06 | AUS — Austrália | TUR — Turquia |
| 7 | C | 13/06 | BRA — Brasil | MAR — Marrocos |
| 8 | B | 13/06 | QAT — Catar | SUI — Suíça |
| 9 | E | 14/06 | CIV — Costa do Marfim | ECU — Equador |
| 10 | E | 14/06 | GER — Alemanha | CUW — Curaçao |
| 11 | F | 14/06 | NED — Países Baixos | JPN — Japão |
| 12 | F | 14/06 | SWE — Suécia | TUN — Tunísia |
| 13 | H | 15/06 | KSA — Arábia Saudita | URU — Uruguai |
| 14 | H | 15/06 | ESP — Espanha | CPV — Cabo Verde |
| 15 | G | 15/06 | IRN — Irã | NZL — Nova Zelândia |
| 16 | G | 15/06 | BEL — Bélgica | EGY — Egito |
| 17 | I | 16/06 | FRA — França | SEN — Senegal |
| 18 | I | 16/06 | IRQ — Iraque | NOR — Noruega |
| 19 | J | 16/06 | ARG — Argentina | ALG — Argélia |
| 20 | J | 16/06 | AUT — Áustria | JOR — Jordânia |
| 21 | L | 17/06 | GHA — Gana | PAN — Panamá |
| 22 | L | 17/06 | ENG — Inglaterra | CRO — Croácia |
| 23 | K | 17/06 | POR — Portugal | COD — RD Congo |
| 24 | K | 17/06 | UZB — Uzbequistão | COL — Colômbia |

---

## 📊 Análise comparativa (resultado previsto)

Comparação entre a rede neural e as 5 IAs quanto ao resultado esperado (V1 = vitória do time 1, V2 = vitória do time 2, E = empate).

| Jogo | Confronto | Rede | Claude | ChatGPT | Gemini | Copilot | Grok | Consenso |
|------|-----------|------|--------|---------|--------|---------|------|----------|
| 1 | MEX x RSA | V1 | V1 | V1 | V1 | V1 | V1 | ✅ total |
| 2 | KOR x CZE | E | V1 | E | V1 | E | E | ⚠️ parcial |
| 3 | CAN x BIH | V1 | E | V1 | E | V1 | V1 | ⚠️ parcial |
| 4 | USA x PAR | E | V1 | V1 | V1 | V1 | V1 | ❌ rede isolada |
| 5 | HAI x SCO | E | V2 | V2 | V2 | V2 | V2 | ❌ rede isolada |
| 6 | AUS x TUR | E | V2 | V2 | V2 | V2 | E | ❌ diverge |
| 7 | BRA x MAR | E | V1 | E | V1 | V1 | V1 | ❌ diverge |
| 8 | QAT x SUI | V2 | V2 | V2 | V2 | V2 | E | ⚠️ parcial |
| 9 | CIV x ECU | E | V2 | E | V2 | E | E | ⚠️ parcial |
| 10 | GER x CUW | V1 | V1 | V1 | V1 | V1 | V1 | ✅ total |
| 11 | NED x JPN | E | V1 | V1 | V1 | V1 | V1 | ❌ rede isolada |
| 12 | SWE x TUN | E | V1 | V1 | V1 | V1 | V1 | ❌ rede isolada |
| 13 | KSA x URU | E | V2 | V2 | V2 | V2 | V2 | ❌ rede isolada |
| 14 | ESP x CPV | V1 | V1 | V1 | V1 | V1 | V1 | ✅ total |
| 15 | IRN x NZL | V1 | V2 | V1 | V2 | V1 | V1 | ⚠️ parcial |
| 16 | BEL x EGY | V1 | V1 | V1 | V1 | V1 | V1 | ✅ total |
| 17 | FRA x SEN | V1 | V1 | V1 | V1 | V1 | V1 | ✅ total |
| 18 | IRQ x NOR | E | V2 | V2 | V2 | V2 | V2 | ❌ rede isolada |
| 19 | ARG x ALG | V1 | V1 | V1 | V1 | V1 | V1 | ✅ total |
| 20 | AUT x JOR | V1 | E | V1 | E | V1 | E | ⚠️ parcial |
| 21 | GHA x PAN | E | V2 | V1 | V2 | V1 | E | ❌ diverge |
| 22 | ENG x CRO | V1 | V1 | E | V1 | E | V1 | ⚠️ parcial |
| 23 | POR x COD | V1 | V1 | V1 | V1 | V1 | V1 | ✅ total |
| 24 | UZB x COL | E | V2 | V2 | V2 | V2 | V2 | ❌ rede isolada |

**Resumo:**
- ✅ Consenso total (todos iguais): **7 jogos**
- ⚠️ Consenso parcial (4+ concordam): **6 jogos**
- ❌ Divergência (rede isolada ou divisão): **11 jogos**
- 🔁 Claude e Gemini produziram previsões **idênticas** nos 24 jogos
- 📐 A rede apostou em **empate em 13 dos 24 jogos** — bem acima das IAs, que tendem a cravar um vencedor

---

## 🏆 Sistema de pontuação (bolão)

- Acertar o **placar exato**: **5 pontos**
- Acertar o **resultado** (vencedor ou empate), mas não o placar: **2 pontos**
- Errar o resultado: **0 pontos**

Pontuação máxima: **120 pontos** (24 jogos × 5 pts)

Bônus acadêmico: pontuação total ÷ 100 como ponto extra na disciplina.

---

## 🧠 Metodologia da rede neural

- **Modelo:** MLP (Multi-Layer Perceptron) com TensorFlow/Keras
- **Dados:** 49.000+ resultados de partidas internacionais (1872–2026)
- **Features principais:** ELO rating das seleções, forma recente (últimos 5 jogos em pontos), vantagem de mando de campo
- **Base de dados:** [International football results – Kaggle](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017)
- **Saída:** placar previsto (gols do time 1 e gols do time 2) via regressão

---

*Projeto acadêmico — Mestrado | Disciplina de Deep Learning | Prof. Danny (IDP) | Turma 1/2026*
