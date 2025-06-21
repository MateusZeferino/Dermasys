document.addEventListener("DOMContentLoaded", function() {
    // Se tiver salvo, preenche
    if (localStorage.getItem('loginEmail')) {
        document.querySelector('input[name="email"]').value = localStorage.getItem('loginEmail');
        document.querySelector('input[name="senha"]').value = localStorage.getItem('loginSenha');
        document.querySelector('input[name="lembrar"]').checked = true;
    }

    document.getElementById('form-login').addEventListener('submit', function(e) {
        if(document.querySelector('input[name="lembrar"]').checked) {
            localStorage.setItem('loginEmail', document.querySelector('input[name="email"]').value);
            localStorage.setItem('loginSenha', document.querySelector('input[name="senha"]').value);
        } else {
            localStorage.removeItem('loginEmail');
            localStorage.removeItem('loginSenha');
        }
    });
});

