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

    const btnIa = document.getElementById("btn-analisar-ia");

    if (btnIa) {
        btnIa.addEventListener("click", async function() {
            const textoLivre = document.getElementById("descricao_livre").value;
            const blocoIa = document.getElementById("bloco-ia");
            const parecerIaEl = document.getElementById("parecer-ia");

            if (!textoLivre.trim()) {
                alert("Por favor, descreva o processo primeiro.");
                return;
            }

            parecerIaEl.textContent = "Analisando com IA... Aguarde...";
            blocoIa.hidden = false;

            const respostaIa = await fetch("/api/analisar-texto", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ texto: textoLivre })
            });

            const resultadoIa = await respostaIa.json();
            parecerIaEl.textContent = resultadoIa.analise || resultadoIa.error;
        });
    }