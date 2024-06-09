## Versão do projeto

- Django Framework v5.0.2
- Python v3.10.10

## Comandos

- Criar Migrations, é necessário executar os seguintes comandos:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

- Popular o banco de dados

```
python3 manage.py populate_db
```

- Rodar o servidor

```
python3 manage.py runserver
```

## Rotas disponíveis para teste

Enquanto servidor estiver rodando, acessar a porta disponivel em seu ambiente, geralmente é a 8000

Ex: localhost:8000/rotas-listadas-abaixo

- /usuarios
- /cargos
- /componentes
- /tipos
- /kits
- /kit-componentes
- /historico-producao

