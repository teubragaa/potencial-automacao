def calcular_pontuacao(data):
    score = 0

    if data.get("frequente"):
        score += 20

    if data.get("repetitivo"):
        score += 20

    if data.get("regras_claras"):
        score += 20

    if data.get("dados_digitais"):
        score += 20

    if data.get("consome_tempo"):
        score += 20

    return score


def classificar_potencial(score):
    if score >= 80:
        return "Alto"

    elif score >= 60:
        return "Médio"

    else:
        return "Baixo"


def avaliar_processo(data):
    score = calcular_pontuacao(data)

    potencial = classificar_potencial(score)

    return {
        "score": score,
        "potential": potencial
    }