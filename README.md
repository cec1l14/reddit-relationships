# Relationships on Reddit
Projeto de análise exploratória de dados da disciplina **Introdução à Ciência de Dados** (Ciência de Dados e Inteligência Artificial, UFPB).

#### 1. Coleta de dados
#### 2. Explicação do conjunto de dados
Os dados por nós obtidos foram retirados de 2830 posts e 222533 comentários, os quais pertencem a cinco subrredits distintos: r/relationships, r/relationship_advice ('all time' e 'past year'), r/interracialdating, r/gayrelationships e r/actuallesbians. Além disso, é válido pontuar que adicionamos as extrações em csv's, os quais estão organizados em 206 colunas: 'AutorPost', 'Título', 'Estado/Flair', 'Link', 'Conteúdo', 'AutorCom1',..., 'Autorcom100', 'Comentário 1',..., 'Comentário 100'. Quanto à distribuição de cada dataset individualmente, nota-se:
| Subreddit | Período | Posts | Comentários |
|---|---|---|---|
| r/relationships | Todos os tempos | [491] | [46947] |
| r/relationship_advice | Todos os tempos | [487] | [48347] |
| r/relationship_advice | Último ano | [462] | [45372] |
| r/interracialdating | Último ano | [464] | [45509] |
| r/gayrelationships | Último ano | [472] | [7414] |
| r/actuallesbians | Último ano | [454] | [28944] |
#### 3. Explicação do processo de coleta de dados
Em suma, a coleta foi realizada a partir do web scraping aplicado ao 'old.reddit.com'. A justificava para tal escolha se dá devido à simplicidade com que o site foi construído, haja vista que, por não depender de JavaScript, a extração de dados tradicional se torna possível ([Bernard, 2026](https://roundproxies.com/blog/reddit/)). Assim, para tal, fizemos uso de um script ('raspagem.py'), o qual percorre a listagem "top" do período escolhido, página por página, até o limite de 40 páginas (uma vez que o Reddit restringe a listagem a aproximadamente 1000 publicações). Além disso, urge pontuar que a navegação entre as páginas é realizada a partir do botão de próxima página, configurado na interface do site. 

No tocante à funcionalidade do script, vê-se que esse extrai o autor, título, flair e o endereço, para, em seguida, acessar a página do post para obter o texto e os comentários. Além disso, foram descartados os comentários do usuário 'AutoModerator' e aqueles marcados como '[deleted]' ou '[removed]'. Quanto às quebras de linhas, estas foram substituídas por '|', enquanto os valores ausentes foram preenchidos com 'Desconhecido', 'Sem Estado/Flair' e 'Post sem texto (Link ou Imagem)'. 

#### 4. Descrição de cada coluna
| Coluna | Descrição | Exemplo |
|---|---|---|
| `AutorPost` | Usuário que publicou o post | `usuario_exemplo` |
| `Título` | Título do post | `Peguei meu marido no flagra...` |
| `Estado/Flair` | Etiqueta do post | `Sem Estado/Flair` |
| `Link` | URL do post | `https://old.reddit.com/r/.../comments/...` |
| `Conteúdo` | Texto do post | `Meus pais se divorciaram quando eu estava na pré-escola...` |
| `AutorCom N` | Autor do N-ésimo comentário (N de 1 a 100) | `outro_usuario` |
| `Comentário N` | Texto do N-ésimo comentário (N de 1 a 100) | `Pergunte à sua mãe se ela pode mudar sua genética...` |
#### 5. Link do Google Drive
 [Dados do projeto](https://drive.google.com/drive/u/4/folders/1jatpj7-MGdezqWZKNTkjlBcMaB7bKh6o?hl=pt-br)
###  Integrantes

| | Nome | GitHub |
|---|---|---|
| <img src="https://github.com/cec1l14.png" width="40"> | Cecília Candeia | [@cec1l14](https://github.com/cec1l14) |
| <img src="https://github.com/italoosilva.png" width="40"> | Ítalo Silva | [@italoosilva](https://github.com/italoosilva) |
| <img src="https://github.com/vicktoriasilva.png" width="40"> | Joana Victória | [@vicktoriasilva](https://github.com/vicktoriasilva) |
| <img src="https://github.com/techteus.png" width="40"> | Matheus Fernandes | [@techteus](https://github.com/techteus) |