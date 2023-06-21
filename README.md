# Test Credor

## Rodando a aplicação

- rodar a aplicação: `docker-compose up --build`
- abrir o formulário: `localhost:3000`
- abrir o django admin: `localhost:8000/admin`
  - default user: admin, senha: admin
- rode a seed se desejar que o formulário inicie com alguns campos pré cadastrados: 
  - ` cd backend/desafiocredor` ,
  - `python manage.py create_seed_data`


## Requirements

* docker, docker-compose
* postgres latest
* rabbitmq latest
* python 3.10
* node 18
* react 18.2.0
* typescript 4.9.5

## Observações

* O estilo do cógido foi formatado utilizando black 23.3.0
* Caso não rode a seed, o frontend inicia sem os campos do formulário,
que poderão ser cadastrados no django admin > proposal fields > add proposal field;
