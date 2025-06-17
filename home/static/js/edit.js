function abrirModalEditar() {
  document.getElementById('modal-editar').style.display = 'flex';
}
function fecharModalEditar() {
  document.getElementById('modal-editar').style.display = 'none';
}
document.addEventListener('DOMContentLoaded', function() {
    // Fecha ao clicar fora do modal editar
    document.getElementById('modal-editar').addEventListener('click', function(e) {
        if (e.target === this) {
            fecharModalEditar();
        }
    });
});
