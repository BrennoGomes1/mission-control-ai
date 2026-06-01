# 🚀 Mission Control AI

**Sistema Inteligente de Monitoramento de Missão Espacial**  

---

## 📋 Descrição

O **Mission Control AI** simula um sistema de controle de missão espacial.  
Ele analisa ciclos de monitoramento com dados de temperatura, comunicação, bateria, oxigênio e estabilidade, gerando alertas automáticos, calculando o risco de cada ciclo e produzindo um relatório final completo no terminal.

---

## 🛸 Missão simulada

| Campo       | Valor             |
|-------------|-------------------|
| Nome        | Prometheus Alpha  |
| Equipe      | Equipe Nebula     |
| Ciclos      | 8                 |

### Narrativa dos ciclos

| Ciclo | Descrição                          |
|-------|------------------------------------|
| 1     | Lançamento e estabilização inicial |
| 2     | Operação nominal                   |
| 3     | Aquecimento moderado detectado     |
| 4     | Queda de comunicação e energia     |
| 5     | Risco operacional elevado          |
| 6     | Crise máxima dos sistemas          |
| 7     | Tentativa de recuperação parcial   |
| 8     | Estabilização progressiva          |

---

## 📊 Áreas monitoradas

| Coluna | Área                     | Unidade |
|--------|--------------------------|---------|
| 0      | Temperatura interna      | °C      |
| 1      | Comunicação com a base   | %       |
| 2      | Sistema de energia       | %       |
| 3      | Suporte de oxigênio      | %       |
| 4      | Estabilidade operacional | %       |

---

## ⚠️ Regras de alerta

### Temperatura (°C)
| Condição          | Classificação |
|-------------------|---------------|
| < 18              | ATENÇÃO       |
| 18 a 30           | NORMAL        |
| > 30 até 35       | ATENÇÃO       |
| > 35              | CRÍTICO       |

### Comunicação (%)
| Condição  | Classificação |
|-----------|---------------|
| < 30      | CRÍTICO       |
| 30 a 59   | ATENÇÃO       |
| ≥ 60      | NORMAL        |

### Bateria (%)
| Condição  | Classificação |
|-----------|---------------|
| < 20      | CRÍTICO       |
| 20 a 49   | ATENÇÃO       |
| ≥ 50      | NORMAL        |

### Oxigênio (%)
| Condição  | Classificação |
|-----------|---------------|
| < 80      | CRÍTICO       |
| 80 a 89   | ATENÇÃO       |
| ≥ 90      | NORMAL        |

### Estabilidade (%)
| Condição  | Classificação |
|-----------|---------------|
| < 40      | CRÍTICO       |
| 40 a 69   | ATENÇÃO       |
| ≥ 70      | NORMAL        |

---

## 🎯 Pontuação e classificação de ciclo

| Classificação | Pontos |
|---------------|--------|
| NORMAL        | 0      |
| ATENÇÃO       | 1      |
| CRÍTICO       | 2      |

| Pontuação total | Classificação do ciclo |
|-----------------|------------------------|
| 0 a 2           | MISSÃO ESTÁVEL         |
| 3 a 5           | MISSÃO EM ATENÇÃO      |
| 6 a 10          | MISSÃO CRÍTICA         |

---

## 🔧 Funções implementadas

| Função                          | Descrição                                              |
|---------------------------------|--------------------------------------------------------|
| `analisar_temperatura()`        | Classifica a temperatura do módulo                     |
| `analisar_comunicacao()`        | Classifica a qualidade do sinal                        |
| `analisar_bateria()`            | Classifica o nível de energia                          |
| `analisar_oxigenio()`           | Classifica o suporte de oxigênio                       |
| `analisar_estabilidade()`       | Classifica a estabilidade operacional                  |
| `classificar_ciclo()`           | Determina o status geral do ciclo pela pontuação       |
| `gerar_recomendacao()`          | Gera recomendação automática baseada nos alertas       |
| `analisar_tendencia()`          | Compara risco do 1º e do último ciclo                  |
| `identificar_area_mais_afetada()` | Aponta a área com maior pontuação acumulada          |
| `calcular_medias()`             | Calcula médias por sensor ao longo dos ciclos          |
| `processar_ciclos()`            | Loop principal de análise e exibição de cada ciclo     |
| `gerar_relatorio_final()`       | Exibe o relatório consolidado da missão                |

---

## ▶️ Como executar

Pré-requisito: Python 3.x instalado (sem bibliotecas externas necessárias).

```bash
python mission_control.py
```

---

## 📁 Estrutura do repositório

```
mission-control-ai/
├── README.md
└── mission_control.py
```

---

## 👨‍🚀 Integrantes

| Nome                              | RM     |
|-----------------------------------|--------|
| Brenno Ferreira Gomes dos Santos  | 570525 |
| Eduardo Moreira Silva             | 569923 |


