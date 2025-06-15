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
