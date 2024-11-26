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

    function adicionarAoCarrinho(codproduto) {
        fetch(`/adicionar_ao_carrinho/${codproduto}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Para segurança contra CSRF
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Produto adicionado ao carrinho!');
            } else {
                alert(data.message);  // Exibe uma mensagem de erro
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Erro ao adicionar produto ao carrinho.');
        });
    }
    