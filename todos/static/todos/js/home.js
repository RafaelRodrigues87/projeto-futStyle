
    function filterItems() {
        const query = document.getElementById('barra-pesquisa').value.toLowerCase();
        const items = document.querySelectorAll('.vitrine .item');

        items.forEach(item => {
            const nome = item.getAttribute('data-nome').toLowerCase();
            if (nome.includes(query)) {
                item.style.display = ''; // Mostra o item
            } else {
                item.style.display = 'none'; // Esconde o item
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
    