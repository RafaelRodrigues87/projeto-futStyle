function filterItems() {
    const query = document.getElementById('barra-pesquisa').value.toLowerCase();
    const items = document.querySelectorAll('.vitrine .item');

    items.forEach(item => {
        const nome = item.getAttribute('data-nome').toLowerCase();

        if (nome.includes(query)) {
            item.style.display = ''; // Mostra o item
            item.classList.add('filtrado'); // Adiciona a classe 'filtrado' para colocar no topo
        } else {
            item.style.display = 'none'; // Esconde o item
            item.classList.remove('filtrado'); // Remove a classe 'filtrado'
        }
    });
}








    // carrinho

    function adicionarAoCarrinho(produtoId) {
        fetch(`/carrinho/adicionar/${produtoId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => console.error('Erro:', error));
    }

    function openLogin() {
        document.getElementById('login-overlay').classList.add('active');
    }
    
    function closeLogin() {
        document.getElementById('login-overlay').classList.remove('active');
    }
    
    