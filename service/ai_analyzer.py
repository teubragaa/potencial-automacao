import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

def analisar_texto_livre(texto_usuario):
    """
    Recebe a descrição em texto livre de um processo e utiliza o Gemini
    para extrair insights, gargalos e viabilidade de automação.
    """
    prompt = f"""
    Atue como um analista de automação de processos. O usuário descreveu seu fluxo de trabalho de forma livre abaixo:
    
    "{texto_usuario}"

    Com base apenas nessa descrição, forneça uma análise curta e objetiva contendo:
    1. Principais gargalos manuais identificados.
    2. Viabilidade e nível de facilidade para automatizar (Baixa, Média, Alta).
    3. Uma sugestão prática de qual tecnologia/ferramenta (ex: Python com Pandas, Selenium, scripts de API) resolveria o problema.
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Não foi possível processar a análise com IA no momento: {str(e)}"