function abrirModalEditar() {
    document.getElementById('modal-editar').style.display = 'flex';
}

function fecharModalEditar() {
    document.getElementById('modal-editar').style.display = 'none';
}

// Fecha ao clicar fora do modal de editar
document.addEventListener('DOMContentLoaded', function() {
    var modalEditar = document.getElementById('modal-editar');
    if (modalEditar) {
        modalEditar.addEventListener('click', function(e) {
            if (e.target === this) {
                fecharModalEditar();
            }
        });
    }
});


function filtrarAgendamentosEditar() {
    const clienteId = document.getElementById('cliente-select-editar').value;
    const agendamentoSelect = document.getElementById('agendamento-editar-select');
    const opcoes = agendamentoSelect.querySelectorAll('option');

    opcoes.forEach(option => {
        if (option.value === "") {
            option.style.display = ""; // Deixar a opção "Selecione..."
        } else if (option.getAttribute('data-cliente') === clienteId) {
            option.style.display = "";
        } else {
            option.style.display = "none";
        }
    });

    agendamentoSelect.value = "";
}