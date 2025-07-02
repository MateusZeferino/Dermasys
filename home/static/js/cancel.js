function abrirModalCancelar() {
  document.getElementById('modal-cancelar').style.display = 'flex';
}
function fecharModal() {
  document.getElementById('modal-cancelar').style.display = 'none';
}

// Fecha ao clicar fora da janela modal
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('modal-cancelar').addEventListener('click', function(e) {
        if (e.target === this) {
            fecharModal();
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const clienteSelect = document.getElementById('cliente-cancelar-select');
    const agendamentoSelect = document.getElementById('agendamento-select');

    if (clienteSelect && agendamentoSelect) {
        clienteSelect.addEventListener('change', function () {
            const clienteId = this.value;

            // Limpa opções
            agendamentoSelect.innerHTML = "";

            if (!clienteId) {
                // Nenhum cliente escolhido
                agendamentoSelect.innerHTML = "<option value=''>Selecione um cliente</option>";
                agendamentoSelect.disabled = true;
                return;
            }

            // Filtra agendamentos do cliente escolhido
            const agsDoCliente = agendamentos.filter(ag => ag.cliente_id === clienteId);

            if (agsDoCliente.length === 0) {
                agendamentoSelect.innerHTML = "<option value=''>Nenhum agendamento encontrado</option>";
                agendamentoSelect.disabled = true;
            } else {
                agendamentoSelect.disabled = false;
                agendamentoSelect.innerHTML = "<option value=''>Selecione...</option>";
                agsDoCliente.forEach(ag => {
                    const opt = document.createElement('option');
                    opt.value = ag.id;
                    opt.textContent = `${ag.cliente_nome} — ${ag.dia} ${ag.horario}`;
                    agendamentoSelect.appendChild(opt);
                });
            }
        });

        // Ao tentar abrir o modal, resetar agendamentos dropdown
        if (typeof abrirModalCancelar !== "undefined") {
            const originalAbrir = abrirModalCancelar;
            window.abrirModalCancelar = function() {
                clienteSelect.selectedIndex = 0;
                agendamentoSelect.innerHTML = "<option value=''>Selecione um cliente</option>";
                agendamentoSelect.disabled = true;
                originalAbrir();
            }
        } else {
            // Ao carregar a página já deixa dropdown de agendamento desabilitado
            agendamentoSelect.innerHTML = "<option value=''>Selecione um cliente</option>";
            agendamentoSelect.disabled = true;
        }
    }
});
