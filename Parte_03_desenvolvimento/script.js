const form = document.getElementById('form-inscricao');
const lista = document.getElementById('lista-inscritos');

form.addEventListener('submit', function(event) {
    event.preventDefault(); // evita recarregar a página

    const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();

    // Verifica se email é valido, contendo @
    if (!nome || !email.includes('@')) {
        alert('Por favor, insira um nome e um e-mail válido.');
        return;
    }

    // Adiciona o inscrito na lista
    const item = document.createElement('li');
    item.textContent = `${nome} - ${email}`;
    lista.appendChild(item);

    // Limpa os campos
    form.reset();
});