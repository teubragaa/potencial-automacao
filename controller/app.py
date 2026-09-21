from flask import Flask, jsonify, render_template, request

from service.scoring import avaliar_processo


app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
