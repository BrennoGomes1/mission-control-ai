# MISSION CONTROL AI
# Sistema Inteligente de Monitoramento de Missão Espacial

nome_missao = "Prometheus Alpha"
nome_equipe  = "Equipe Nebula"


# Matriz principal: [temperatura, comunicacao, bateria, oxigenio, estabilidade]
# Ciclo 1 – Lançamento e estabilização inicial
# Ciclo 2 – Operação nominal
# Ciclo 3 – Aquecimento moderado detectado
# Ciclo 4 – Queda de comunicação e energia
# Ciclo 5 – Risco operacional elevado
# Ciclo 6 – Crise máxima dos sistemas
# Ciclo 7 – Tentativa de recuperação parcial
# Ciclo 8 – Estabilização progressiva

dados_missao = [
    [22, 95, 91, 97, 93],   # Ciclo 1
    [26, 87, 80, 95, 88],   # Ciclo 2
    [32, 70, 65, 92, 74],   # Ciclo 3
    [37, 45, 40, 88, 58],   # Ciclo 4
    [40, 25, 18, 76, 32],   # Ciclo 5
    [42, 18, 10, 72, 25],   # Ciclo 6
    [36, 48, 28, 80, 44],   # Ciclo 7
    [30, 62, 45, 85, 60],   # Ciclo 8
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]


# FUNÇÕES DE ANÁLISE POR SENSOR


def analisar_temperatura(valor):
    """Classifica a temperatura e retorna (status, pontos, descricao)."""
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    """Classifica a qualidade da comunicação."""
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    """Classifica o nível de bateria."""
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    """Classifica o nível de oxigênio."""
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    """Classifica a estabilidade operacional."""
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"



# FUNÇÕES DE CLASSIFICAÇÃO E ANÁLISE

def classificar_ciclo(pontuacao):
    """Retorna a classificação textual do ciclo com base na pontuação."""
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(resultados):
    """
    Gera recomendação automática com base nas classificações do ciclo.
    resultados: lista de tuplas (status, pontos, descricao) na ordem dos sensores.
    """
    criticos = []
    atencoes = []
    nomes_sensores = [
        "Temperatura",
        "Comunicação",
        "Bateria",
        "Oxigênio",
        "Estabilidade",
    ]
    recomendacoes_critico = {
        "Temperatura":   "Verificar controle térmico da missão.",
        "Comunicação":   "Tentar restabelecer contato com a base.",
        "Bateria":       "Ativar modo de economia de energia.",
        "Oxigênio":      "Acionar protocolo de suporte à vida.",
        "Estabilidade":  "Reduzir operações não essenciais.",
    }

    for i, (status, _, _) in enumerate(resultados):
        if status == "CRÍTICO":
            criticos.append(nomes_sensores[i])
        elif status == "ATENÇÃO":
            atencoes.append(nomes_sensores[i])

    if len(criticos) >= 3:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."
    elif criticos:
        return " | ".join(recomendacoes_critico[s] for s in criticos)
    elif atencoes:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Manter operação normal e continuar monitoramento."


def analisar_tendencia(riscos):
    """Compara risco do primeiro e último ciclo e retorna string de tendência."""
    if riscos[-1] > riscos[0]:
        return "A missão apresentou tendência de PIORA."
    elif riscos[-1] < riscos[0]:
        return "A missão apresentou tendência de MELHORA."
    else:
        return "A missão permaneceu ESTÁVEL em relação ao início."


def identificar_area_mais_afetada(pontuacao_acumulada):
    """Retorna o nome da área com maior pontuação acumulada."""
    maior_idx = 0
    for i in range(1, len(pontuacao_acumulada)):
        if pontuacao_acumulada[i] > pontuacao_acumulada[maior_idx]:
            maior_idx = i
    return areas_monitoradas[maior_idx]


def calcular_medias():
    """Calcula a média de cada sensor ao longo de todos os ciclos."""
    n = len(dados_missao)
    somas = [0, 0, 0, 0, 0]
    for ciclo in dados_missao:
        for i in range(5):
            somas[i] += ciclo[i]
    return [round(somas[i] / n, 2) for i in range(5)]



# PROCESSAMENTO DOS CICLOS


def processar_ciclos():
    """
    Percorre todos os ciclos, exibe análise detalhada e retorna
    os dados consolidados para o relatório final.
    """
    riscos           = []
    pontuacao_acum   = [0, 0, 0, 0, 0]   # acumulado por área
    ciclo_mais_crit  = 1
    maior_risco      = 0
    qtd_criticos     = 0

    analisadores = [
        analisar_temperatura,
        analisar_comunicacao,
        analisar_bateria,
        analisar_oxigenio,
        analisar_estabilidade,
    ]
    rotulos = ["Temperatura", "Comunicação", "Bateria", "Oxigênio", "Estabilidade"]
    unidades = ["°C", "%", "%", "%", "%"]

    for idx, ciclo in enumerate(dados_missao):
        num_ciclo = idx + 1
        print(f"\nCICLO {num_ciclo}")
        print("-" * 60)

        resultados = []
        pontuacao_ciclo = 0

        for i in range(5):
            status, pts, descricao = analisadores[i](ciclo[i])
            resultados.append((status, pts, descricao))
            pontuacao_ciclo      += pts
            pontuacao_acum[i]    += pts
            print(f"{rotulos[i]}: {ciclo[i]} {unidades[i]} | {status} | {descricao}")

        riscos.append(pontuacao_ciclo)
        classificacao = classificar_ciclo(pontuacao_ciclo)
        recomendacao  = gerar_recomendacao(resultados)

        print(f"\nPontuação de risco do ciclo: {pontuacao_ciclo}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")

        if pontuacao_ciclo > maior_risco:
            maior_risco     = pontuacao_ciclo
            ciclo_mais_crit = num_ciclo
        if classificacao == "MISSÃO CRÍTICA":
            qtd_criticos += 1

    return riscos, pontuacao_acum, ciclo_mais_crit, maior_risco, qtd_criticos


# RELATÓRIO FINAL

def gerar_relatorio_final(riscos, pontuacao_acum, ciclo_mais_crit, maior_risco, qtd_criticos):
    """Exibe o relatório consolidado da missão."""
    medias      = calcular_medias()
    tendencia   = analisar_tendencia(riscos)
    area_afet   = identificar_area_mais_afetada(pontuacao_acum)
    risco_medio = round(sum(riscos) / len(riscos), 2)
    class_final = classificar_ciclo(round(risco_medio))

    print("\n")
    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão : {nome_missao}")
    print(f"Equipe : {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")

    print(f"\nMédia de temperatura  : {medias[0]} °C")
    print(f"Média de comunicação  : {medias[1]}%")
    print(f"Média de bateria      : {medias[2]}%")
    print(f"Média de oxigênio     : {medias[3]}%")
    print(f"Média de estabilidade : {medias[4]}%")

    print(f"\nCiclo mais crítico      : Ciclo {ciclo_mais_crit}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão   : {risco_medio}")
    print(f"Quantidade de ciclos críticos: {qtd_criticos}")

    print(f"\nTendência da missão:")
    print(f"  {tendencia}")

    print(f"\nPontuação acumulada por área:")
    for i, area in enumerate(areas_monitoradas):
        print(f"  {area}: {pontuacao_acum[i]} pontos")

    print(f"\nÁrea mais afetada:")
    print(f"  {area_afet}")

    print(f"\nClassificação final da missão:")
    print(f"  {class_final}")

    print(f"\nConclusão:")
    if class_final == "MISSÃO CRÍTICA":
        print("  A missão enfrentou condições extremamente adversas.")
        print("  É necessária intervenção imediata e revisão completa dos sistemas.")
    elif class_final == "MISSÃO EM ATENÇÃO":
        print("  A missão apresentou instabilidade relevante durante a operação.")
        print("  A equipe deve manter o plano de contingência ativo e monitorar de perto.")
    else:
        print("  A missão transcorreu de forma satisfatória.")
        print("  Manter monitoramento contínuo para garantir a segurança da operação.")

    print("=" * 60)



# EXECUÇÃO PRINCIPAL


def main():
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão : {nome_missao}")
    print(f"Equipe : {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    riscos, pontuacao_acum, ciclo_mais_crit, maior_risco, qtd_criticos = processar_ciclos()

    gerar_relatorio_final(riscos, pontuacao_acum, ciclo_mais_crit, maior_risco, qtd_criticos)


if __name__ == "__main__":
    main()
