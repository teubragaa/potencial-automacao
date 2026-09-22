def avaliar_processo(dados):
    score = 0

    perguntas = [
        "frequente",
        "repetitivo",
        "regras_claras",
        "dados_digitais",
        "consome_tempo"
    ]

    for pergunta in perguntas:
        if dados.get(pergunta) == "sim":
            score += 20

    if score >= 80:
        potential = "Alto"
    elif score >= 40:
        potential = "Médio"
    else:
        potential = "Baixo"

    return {
        "score": score,
        "potential": potential
    }