import requests
from bs4 import BeautifulSoup

def popula_brasil_2025():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive'
    }
    url = "https://www.gov.br/secom/pt-br/assuntos/noticias/2025/08/populacao-do-brasil-alcanca-marca-de-213-4-milhoes-de-habitantes-divulga-ibge"
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Buscar parágrafo que contenha o número da população
        textos = soup.find_all('p')
        populacao = None
        
        for p in textos:
            text = p.get_text()
            if '213,4 milhões de habitantes' in text or '213.4 milhões' in text or '213,4 milhões' in text:
                populacao = text.strip()
                break
        
        if populacao:
            print(f"🌎 População do Brasil em 2025: {populacao}")
        else:
            print("🔍 Informação da população não encontrada.")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

popula_brasil_2025()