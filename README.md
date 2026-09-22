# Potencial de Automação

Aplicação web simples para identificar se um processo possui potencial para automação.

O usuário responde algumas perguntas sobre o processo e a aplicação calcula uma pontuação, retornando o nível de potencial de automação.

## Preview

### Formulário

![Formulário da aplicação](images/formulario.png)

### Resultado

![Resultado da avaliação](images/resultado.png)

## Tecnologias

- Python
- Flask
- JavaScript
- HTML
- CSS
- Docker
- Gunicorn

## Como executar

### Clone o projeto

git clone 

### Suba a aplicação com Docker:
docker compose up --build

### Acesse: 
http://localhost:5000

### Funcionamento

O formulário envia as respostas para a API:

POST /api/avaliar

O backend calcula a pontuação e retorna o resultado em JSON.
