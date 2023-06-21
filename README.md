# Test Credor

## Running app

- run application: `docker-compose up --build`
- open form: `localhost:3000`
- django admin: `localhost:8000/admin`
  - default user: admin, password: admin
- seed: if you want to start the admin with default fields: 
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

## Observations

* formatted using black 23.3.0
