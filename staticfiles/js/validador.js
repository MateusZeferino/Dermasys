document.addEventListener("DOMContentLoaded", function() {
    const senhaInput = document.getElementById("senha");

    // Pegando cada li
    const minLength = document.getElementById("min-len");
    const temLetra = document.getElementById("letra");
    const temNumero = document.getElementById("numero");
    const especial = document.getElementById("car-especial");
    const minusc = document.getElementById("minus");
    const maiusc = document.getElementById("maius");

    // Função de validação
    senhaInput.addEventListener("input", function() {
        const senha = senhaInput.value;

        // 1. Mínimo de 8 letras
        minLength.style.color = senha.length >= 8 ? "green" : "red";

        // 2. Pelo menos uma letra
        /[a-zA-Z]/.test(senha) ? temLetra.style.color = "green" : temLetra.style.color = "red";

        // 3. Pelo menos um número
        /\d/.test(senha) ? temNumero.style.color = "green" : temNumero.style.color = "red";

        // 4. Pelo menos um caracter especial
        /[!@#$%^&*()\-_=+\[\]{}|;:'",.<>?/`~]/.test(senha) ? especial.style.color = "green" : especial.style.color = "red";

        // 5. Pelo menos uma letra minúscula
        /[a-z]/.test(senha) ? minusc.style.color = "green" : minusc.style.color = "red";

        // 6. Pelo menos uma letra maiúscula
        /[A-Z]/.test(senha) ? maiusc.style.color = "green" : maiusc.style.color = "red";
    });

    // Deixa tudo vermelho quando carrega
    minLength.style.color = "red";
    temLetra.style.color = "red";
    temNumero.style.color = "red";
    especial.style.color = "red";
    minusc.style.color = "red";
    maiusc.style.color = "red";
});
