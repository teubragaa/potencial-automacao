from flask import Flask, jsonify, render_template, request
from service.scoring import avaliar_processo
from service.ai_analyzer import analisar_texto_livre

app = Flask( __name__,
    template_folder="../templates",
    static_folder="../static"
)


@app.get("/")
def inicio():
    return render_template("index.html")


@app.post("/api/avaliar")
def avaliar():
    try:
        result = avaliar_processo(request.get_json(silent=True) or {})
        return jsonify(result)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.post("/api/analisar-texto")
def api_analisar_texto():
    try:
        data = request.get_json(silent=True) or {}
        texto = data.get("texto", "")
        
        if not texto.strip():
            return jsonify({"error": "O campo de texto está vazio."}), 400
            
        resultado_ia = analisar_texto_livre(texto)
        return jsonify({"analise": resultado_ia})
    except Exception as error:
        return jsonify({"error": str(error)}), 400



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

