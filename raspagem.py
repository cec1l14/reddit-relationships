# altere o codigo conforme sua necessidade, como os subreddits, entradas e saidas de arquivos.
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import time
import csv

load_dotenv() 

cookie = os.environ.get("REDDIT_COOKIE", "")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 MeuScraperReddit/1.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
}
if cookie:
    headers["Cookie"] = cookie # em caso de erro, altere o cookie.


# Subrredits usados:

# URL 1 (Top Histórico de Sempre): "https://old.reddit.com/r/relationships/top/?sort=top&t=all"
# URL 2 (Advices): "https://old.reddit.com/r/relationship_advice/top/?sort=top&t=all"
# URL 3 (Advices - past year): "https://old.reddit.com/r/relationship_advice/top/?sort=top&t=year"
# URL 4 (Interracial relantionships): "https://old.reddit.com/r/interracialdating/top/?sort=top&t=year"
# URL 5 (Gay relationships): "https://old.reddit.com/r/gayrelationships/top/?sort=top&t=year"
# URL 6 (Actual Lesbians - past year): "https://old.reddit.com/r/actuallesbians/top/?sort=top&t=year" 

url_atual = "https://old.reddit.com/r/gayrelationships/top/?sort=top&t=year"

# Nome do arquivo customizado para diferenciar da raspagem anterior
NOME_ARQUIVO_SAIDA = "gayrelationship_pastyear.csv"

paginas_para_raspar = 40 # aqui tem o maximo de 40, visto que o reddit só deixar fazer o scraping de 1000 posts por vez.
QTD_COMENTARIOS = 100

total_posts_processados = 0
total_comentarios_validos = 0

cabecalho_csv = ['AutorPost', 'Título', 'Estado/Flair', 'Link', 'Conteúdo']
for i in range(1, QTD_COMENTARIOS + 1):
    cabecalho_csv.append(f'AutorCom {i}')
    cabecalho_csv.append(f'Comentário {i}')

with open(NOME_ARQUIVO_SAIDA, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(cabecalho_csv) 

    for pagina in range(paginas_para_raspar):
        print(f"\n--- Acessando página {pagina + 1} ---")
        resposta = requests.get(url_atual, headers=headers)
        
        if resposta.status_code == 200:
            sopa = BeautifulSoup(resposta.text, 'html.parser')
            posts = sopa.find_all('div', class_='thing')
            
            for post in posts:
                try:
                    titulo_elemento = post.find('a', class_='title')
                    if not titulo_elemento: 
                        continue
                        
                    titulo = titulo_elemento.text
                    
                    link_comentarios = post.get('data-permalink')
                    if not link_comentarios:
                        continue
                    link = "https://old.reddit.com" + link_comentarios
                        
                    autor_post = post.find('a', class_='author').text if post.find('a', class_='author') else "Desconhecido"
                    
                    flair_elemento = post.find('span', class_='flair')
                    estado_flair = flair_elemento.text.strip() if flair_elemento else "Sem Estado/Flair"
                    
                    print(f"Salvando post: {titulo[:30]}...")
                    
                    resp_post = requests.get(link, headers=headers)
                    conteudo = "Post sem texto (Link ou Imagem)"
                    
                    autores_comentarios = [""] * QTD_COMENTARIOS
                    textos_comentarios = [""] * QTD_COMENTARIOS 
                    
                    if resp_post.status_code == 200:
                        sopa_post = BeautifulSoup(resp_post.text, 'html.parser')
                        
                        corpo_post = sopa_post.find('div', class_='expando')
                        if corpo_post and corpo_post.find('div', class_='md'):
                            conteudo_bruto = corpo_post.find('div', class_='md').text.strip()
                            conteudo = conteudo_bruto.replace('\n', ' | ')
                        
                        area_comentarios = sopa_post.find('div', class_='commentarea')
                        
                        if area_comentarios:
                            lista_comentarios = area_comentarios.find_all('div', class_='comment') 
                            
                            idx_salvo = 0
                            for com_bloco in lista_comentarios:
                                if idx_salvo >= QTD_COMENTARIOS:
                                    break
                                    
                                autor_com = com_bloco.find('a', class_='author')
                                nome_autor_com = autor_com.text if autor_com else "Desconhecido"
                                
                                if nome_autor_com == 'AutoModerator':
                                    continue
                                    
                                texto_com = com_bloco.find('div', class_='md')
                                
                                if texto_com and texto_com.text.strip():
                                    texto_limpo = texto_com.text.strip().replace('\n', ' | ')
                                    
                                    if texto_limpo not in ["[deleted]", "[removed]"]:
                                        autores_comentarios[idx_salvo] = nome_autor_com
                                        textos_comentarios[idx_salvo] = texto_limpo
                                        idx_salvo += 1
                                        total_comentarios_validos += 1
                    
                    pares_comentarios = []
                    for a, c in zip(autores_comentarios, textos_comentarios):
                        pares_comentarios.extend([a, c])
                    
                    linha_dados = [autor_post, titulo, estado_flair, link, conteudo] + pares_comentarios
                    escritor.writerow(linha_dados)
                    
                    total_posts_processados += 1
                    time.sleep(5) 
                    
                except Exception as e:
                    continue
                    
            botao_proxima = sopa.find('span', class_='next-button')
            
            if botao_proxima and botao_proxima.find('a'):
                url_atual = botao_proxima.find('a')['href']
                time.sleep(10) 
            else:
                break
                
        else:
            print(f"Erro no status code: {resposta.status_code}")
            break

print("\n" + "="*40)
print(" RELATÓRIO FINAL DE EXTRAÇÃO ")
print("="*40)
print(f" Total de posts processados: {total_posts_processados}")
print(f" Total de comentários válidos salvos: {total_comentarios_validos}")
print("="*40)