
# Objetivo

O projeto tem o objetivo de demonstrar o estudo feito pelo autor como parte complementar do TCC de Engenharia de Computação do Centro Universitário Uniftec com o tema:
- **ANÁLISE PREDITIVA DE DADOS METEOROLÓGICOS USANDO MACHINE LEARNING**
Seu desenvolvimento e resultados serão publicados no decorrer do segundo semestre de 2025 como parte da disciplina.
## 🛠 Instalação

Para que seja possível executar o projeto deverão ser atendidos os requisitos abaixo.

- Instalação do **Python na versão 3.8** ou superior - https://www.python.org/
- Criação de cadastro do **MongoDB** - https://www.mongodb.com/
  - Gerar chave de acesso para o uso do pacote Python [**PyMongo**](https://www.mongodb.com/pt-br/docs/languages/python/pymongo-driver/current/get-started/)
- (*Opcional*) Criação de cadastro da **HG Brasil** para controle de requisições - https://hgbrasil.com/
  - Gerar chave de acesso para uso da API [**HG Weather**](https://hgbrasil.com/status/weather)

Com essas etapas feitas, executar os comandos abaixo no terminal para a preparação do ambiente com a instalação das dependências necessárias incluindo o [**Jupyter**](https://jupyter.org/), que poderá ser usado na análise dos dados.

```bash
  python -m venv venv
  source venv/bin/activate  # Em sistemas Unix/macOS
  venv\Scripts\activate  # Em Windows
  pip install -r requirements.txt
```
## Variáveis de Ambiente

Depois da instalação, adicionar as seguintes variáveis de ambiente no arquivo `.env`.

\
`API_WEATHER` - URL da API da HG Brasil responsável pela busca dos dados meteorológicos

`API_WEATHER_KEY` (*Opcional*) - Chave de acesso da *API_WEATHER*

`BACKUP_DB` - Determina se será feito o backup das buscas em arquivos JSON

`BACKUP_DIR` (*Opcional*) - Diretório de backup das buscas

`CONNECTION_STRING` - String de conexão do MongoDB

`DB_NAME` - Nome da coleção de dados

`DB_TABLE_WEATHER` - Nome da tabela com os dados meteorológicos históricos

## ⚡️ Estrutura e funcionalidades

O projeto conta com a seguinte estrutura.

```
/TCC_Engenharia_de_Computacao
  ├─ scripts/
  | └─ save_weather.py
  ├─ src/
  | ├─ __init__.py
  | ├─ config.py
  | ├─ db_config.py
  | └─ weather.py
  ├─ .env.example
  ├─ .gitignore
  ├─ main.ipynb
  ├─ README.md
  └─ requeriments.txt
```
\
Seu objetivo e funcionalidades serão descritos abaixo de forma resumida, porém todos os fontes disponibilizados possuem documentação sobre cada um dos aspectos relevantes para o entendimento da aplicação.

\
`scripts/save_weather.py` - Script que deverá executado para a extração dos dados que serão analisados

`src/db_config.py` - Funções responsáveis pela manipulação de dados no MongoDB

`src/weather.py` - Funções responsáveis pela leitura das APIs da HG Brasil

`main.ipynb` - Arquivo de notebook Jupyter usado para a análise dos dados

\
Todos os recursos foram homologados na IDE [**VSCode**](https://code.visualstudio.com/) com o uso da extensão [**Pylance**](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), recomendada para facilitar a leitura das documentações durante o desenvolvimento. Além disso, também foi realizado o teste usando **Jupyter** na análise de dados, sendo necessário executar o comando abaixo no terminal a partir da raiz do projeto.

```bash
  jupyter notebook
```
\
Esse recurso irá permitir acessar a estrutura pelo navegador pela URL http://localhost:8888/tree, podendo editar os arquivos `py` e executar os arquivos `ipynb`.

## Autor

[Guilherme Henrique de Andrade Zorzo](https://github.com/GHAZ25)