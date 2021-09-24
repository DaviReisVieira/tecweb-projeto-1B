# Projeto 1B - Davi Reis

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
