import requests
from django.shortcuts import render

def galeria(request):
    chave_api = 'S7znqqZSnQRW_CrtwCdJJFiTxbrgsKdMcTOyafXrI3c'  # Coloque aqui a sua chave da API Unsplash
    pesquisa = request.GET.get('query', 'tattoo')  # Pega o termo de pesquisa, com 'tattoo' como valor padrão

    # Requisição para a API do Unsplash com o termo de pesquisa
    url = f"https://api.unsplash.com/search/photos?query={pesquisa}&client_id={chave_api}&per_page=10"
    
    response = requests.get(url)
    data = response.json()
    
    # Extraindo URLs das imagens
    imagens = [image['urls']['regular'] for image in data['results']]  # Retorna as URLs das imagens

    return render(request, 'galeria.html', {'imagens': imagens, 'pesquisa': pesquisa})
