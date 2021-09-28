# Projeto 1B - Davi Reis

## Autor:

<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/DaviReisVieira"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/36394034?v=4" width="100px;" alt=""/><br /><sub><b>Davi Reis Vieira</b></sub></a><br /><a href="https://github.com/DaviReisVieira" title="Davi Reis Vieira">4º Semestre</a></td>
  </tr>
</table>

## Deploy

URL: https://murmuring-everglades-97875.herokuapp.com/

## Objetivos

- [x] Reimplementar o CRUD da parte A em Django, ou seja, implementar as funcionalidades de criação, listagem, edição e remoção de anotações aplicando o mesmo estilo (css).

- [x] Utilizar o PostgreSQL (em um container Docker) ao invés do SQLite.

- [x] Implementar o sistema de tags para as anotações.

- [x] Publicar a página.

## Adicionais

- [x] Filtro de Tags utilizando JS.

- [x] Responsividade do site.

- [x] Scrollbar do Filtro.

- [x] Edição do Post It no card.

- [x] Uso de Hamburguer Menu.

- [x] Animações em CSS.

## Iniciando a aplicação

Inicie um ambiente virtual:

```cmd
python -m venv env
```

Ative o env:

- Windows:

```cmd
env/Scripts/activate
```

- Linux/MacOS:

```cmd
source env/bin/activate
```

Instale as dependências:

```cmd
pip install -r requirements.txt
```

Comandos para gerar imagem Docker do Postgres:

```cmd
docker run --rm --name post-it -e POSTGRES_PASSWORD=tecweb123 -d -p 5432:5432 -v $HOME/docker/
```

```cmd
volumes/postgres:/var/lib/postgresql/data postgres
```

```cmd
docker exec -it post-it bash
```

```cmd
psql -h localhost -U postgres
```

```cmd
CREATE DATABASE getit;
CREATE USER getituser WITH PASSWORD 'getitsenha';
ALTER ROLE getituser SET client_encoding TO 'utf8';
ALTER ROLE getituser SET default_transaction_isolation TO 'read committed';
ALTER ROLE getituser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE getit TO getituser;
\q
```
