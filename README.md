# Relationships on Reddit
Projeto de análise exploratória de dados da disciplina **Introdução à Ciência de Dados** (Ciência de Dados e Inteligência Artificial, UFPB).

#### Explicação do conjunto de dados
Os dados por nós obtidos foram retirados de 2830 posts e 222533 comentários, os quais pertencem a cinco subrredits distintos: r/relationships, r/relationship_advice ('all time' e 'past year'), r/interracialdating, r/gayrelationships e r/actuallesbians. Além disso, é válido pontuar que adicionamos as extrações em csv's, os quais estão organizados em 205 colunas ('AutorPost', 'Título', 'Estado/Flair', 'Link', 'Conteúdo', 'AutorCom 1',..., 'AutorCom 100', 'Comentário 1',..., 'Comentário 100'). O notebook acrescenta a coluna 'fonte' (arquivo de origem do post), por isso aparecem 206 colunas ao carregar os dados. Quanto à distribuição de cada dataset individualmente, nota-se:
| Subreddit | Período | Posts | Comentários |
|---|---|---|---|
| r/relationships | Todos os tempos | [491] | [46947] |
| r/relationship_advice | Todos os tempos | [487] | [48347] |
| r/relationship_advice | Último ano | [462] | [45372] |
| r/interracialdating | Último ano | [464] | [45509] |
| r/gayrelationships | Último ano | [472] | [7414] |
| r/actuallesbians | Último ano | [454] | [28944] |
#### Explicação do processo de coleta de dados
Em suma, a coleta foi realizada a partir do web scraping aplicado ao 'old.reddit.com'. A justificava para tal escolha se dá devido à simplicidade com que o site foi construído, haja vista que, por não depender de JavaScript, a extração de dados tradicional se torna possível ([Bernard, 2026](https://roundproxies.com/blog/reddit/)). Assim, para tal, fizemos uso de um script ('raspagem.py'), o qual percorre a listagem "top" do período escolhido, página por página, até o limite de 40 páginas (uma vez que o Reddit restringe a listagem a aproximadamente 1000 publicações). Além disso, urge pontuar que a navegação entre as páginas é realizada a partir do botão de próxima página, configurado na interface do site. 

No tocante à funcionalidade do script, vê-se que esse extrai o autor, título, flair e o endereço, para, em seguida, acessar a página do post para obter o texto e os comentários. Além disso, foram descartados os comentários do usuário 'AutoModerator' e aqueles marcados como '[deleted]' ou '[removed]'. Quanto às quebras de linhas, estas foram substituídas por '|', enquanto os valores ausentes foram preenchidos com 'Desconhecido', 'Sem Estado/Flair' e 'Post sem texto (Link ou Imagem)'. 

#### Descrição de cada coluna
| Coluna | Descrição | Exemplo |
|---|---|---|
| `AutorPost` | Usuário que publicou o post | `usuario_exemplo` |
| `Título` | Título do post | `Peguei meu marido no flagra...` |
| `Estado/Flair` | Etiqueta do post | `Sem Estado/Flair` |
| `Link` | URL do post | `https://old.reddit.com/r/.../comments/...` |
| `Conteúdo` | Texto do post | `Meus pais se divorciaram quando eu estava na pré-escola...` |
| `AutorCom N` | Autor do N-ésimo comentário (N de 1 a 100) | `outro_usuario` |
| `Comentário N` | Texto do N-ésimo comentário (N de 1 a 100) | `Pergunte à sua mãe se ela pode mudar sua genética...` |
#### Limitações dos dados
- A coleta usa a listagem "top" de cada período, que favorece posts de sucesso. Os dados não representam a comunidade inteira;
- Cada post guarda no máximo 100 comentários, os primeiros que aparecem na página. Posts com menos de 100 comentários válidos deixam as últimas colunas vazias;
- O script não coleta data de publicação nem pontuação (score) dos posts e comentários.

#### Estrutura do repositório
```
reddit-relationships/
├── data/                                      
│   ├── relationships_top_alltime.csv
│   ├── relationship_advice.csv
│   ├── relationship_advice_pastyear.csv
│   ├── interracial_relationships_pastyear.csv
│   ├── gayrelationship_pastyear.csv
│   └── actuallesbians_pastyear.csv
├── notebooks/
│   ├── relationships.ipynb                    
│   ├── limpeza.ipynb                          
│   └── analise.ipynb                          
├── .env                                       
├── .gitignore
├── LICENSE
├── raspagem.py                               
├── requirements.txt                           
└── README.md
```

| Item | Descrição |
|---|---|
| `raspagem.py` | Script de coleta (web scraping do old.reddit.com) |
| `notebooks/relationships.ipynb` | Carregamento e verificação da qualidade dos dados |
| `notebooks/limpeza.ipynb` | Limpeza dos dados (em construção) |
| `notebooks/analise.ipynb` | Análise dos dados (em construção) |
| `data/` | CSVs coletados (não versionados; ver link do Google Drive) |
| `requirements.txt` | Bibliotecas necessárias |
| `.env` | Cookie de acesso (não versionado; cada pessoa cria o seu) |

#### Como reproduzir
1. Crie e ative um ambiente virtual e instale as [bibliotecas](requirements.txt):
```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```
2. Crie um arquivo `.env` na raiz com o cookie da sua sessão do Reddit:
```
REDDIT_COOKIE=cole_aqui_o_cookie
```
Se as requisições derem erro, troque o cookie por um novo. Depois, edite no `raspagem.py` a URL do subrredit (`url_atual`) e o nome do arquivo de saída (`NOME_ARQUIVO_SAIDA`) e rode `python raspagem.py`. A coleta de cada subrredit leva dezenas de minutos por causa das pausas entre as requisições.


#### Link do Google Drive
 [Dados do projeto](https://drive.google.com/drive/u/4/folders/1jatpj7-MGdezqWZKNTkjlBcMaB7bKh6o?hl=pt-br)

### Aspectos éticos e legais

Os dados foram coletados de posts e comentários públicos do Reddit, apenas para fins acadêmicos. Eles incluem nomes de usuário e podem tratar de temas sensíveis, como orientação sexual e origem étnico-racial ([Lei Geral de Proteção de Dados, Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)). Por isso, os resultados são apresentados de forma agregada, sem expor usuários, e os CSVs não são redistribuídos fora do contexto da disciplina. A coleta foi feita com pausas entre as requisições, e o uso dos dados respeita diretamente os Termos de Uso do Reddit.


###  Integrantes

| | Nome | GitHub |
|---|---|---|
| <img src="https://github.com/cec1l14.png" width="40"> | Cecília Candeia | [@cec1l14](https://github.com/cec1l14) |
| <img src="https://github.com/italoosilva.png" width="40"> | Ítalo Silva | [@italoosilva](https://github.com/italoosilva) |
| <img src="https://github.com/vicktoriasilva.png" width="40"> | Joana Victória | [@vicktoriasilva](https://github.com/vicktoriasilva) |
| <img src="https://github.com/techteus.png" width="40"> | Matheus Fernandes | [@techteus](https://github.com/techteus) |