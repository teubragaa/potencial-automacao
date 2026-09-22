const form = document.getElementById("form-avaliacao");

form.addEventListener("submit", async function(event) {
    event.preventDefault();

    const dados = Object.fromEntries(new FormData(form));

    const resposta = await fetch("/api/avaliar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    });

    const resultado = await resposta.json();

    document.getElementById("score").textContent = resultado.score;
    document.getElementById("potencial").textContent = resultado.potential;

    document.getElementById("resultado").hidden = false;
});