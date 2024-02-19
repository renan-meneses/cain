# Cain
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/cookiecutter/cookiecutter-django/master.svg)](https://results.pre-commit.ci/latest/github/enan-meneses/cain/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![GNU AGPLv3 License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/agpl-3.0/)


## Project

Sistema voltado a gerenciamento de associados, ME e MEI, sistema construído com Python 3.11, utilizando os frameworks Django.

## Prerequisites Libs

- amqp==5.2.0
- asgiref==3.7.2
- billiard==4.2.0
- celery==5.3.6
- certifi==2024.2.2
- cffi==1.16.0
- cfgv==3.4.0
- charset-normalizer==3.3.2
- click==8.1.7
- click-didyoumean==0.3.0
- click-plugins==1.1.1
- click-repl==0.3.0
- coreapi==2.3.3
- coreschema==0.0.4
- cron-descriptor==1.4.3
- cryptography==42.0.3
- defusedxml==0.7.1
- distlib==0.3.8
- Django==4.2.10
- django-celery-beat==2.5.0
- django-celery-results==2.5.1
- django-cors-headers==4.3.1
- django-debug-toolbar==4.3.0
- django-filter==23.5
- django-rest-swagger==2.2.0
- django-seed==0.3.1
- django-templated-mail==1.1.1
- django-timezone-field==6.1.0
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.3.1
- djoser==2.2.2
- drf-access-policy==1.5.0
- drf-yasg==1.21.7
- et-xmlfile==1.1.0
- Faker==23.2.1
- filelock==3.13.1
- identify==2.5.34
- idna==3.6
- inflection==0.5.1
- itypes==1.2.0
- Jinja2==3.1.3
- kombu==5.3.5
- MarkupSafe==2.1.5
- nodeenv==1.8.0
- oauthlib==3.2.2
- openapi-codec==1.3.2
- openpyxl==3.1.2
- packaging==23.2
- platformdirs==4.2.0
- pre-commit==3.6.1
- prompt-toolkit==3.0.43
- pycparser==2.21
- PyJWT==2.8.0
- pyparsing==3.1.1
- python-crontab==3.0.0
- python-dateutil==2.8.2
- python3-openid==3.2.0
- pytz==2024.1
- PyYAML==6.0.1
- redis==5.0.1
- requests==2.31.0
- requests-oauthlib==1.3.1
- sentry-sdk==1.40.4
- simplejson==3.19.2
- six==1.16.0
- social-auth-app-django==5.4.0
- social-auth-core==4.5.3
- sqlparse==0.4.4
- toposort==1.10
- tzdata==2024.1
- uritemplate==4.1.1
- urllib3==2.2.1
- vine==5.1.0
- virtualenv==20.25.0
- wcwidth==0.2.13
- python-decouple==3.8
- psycopg2-binary==2.9.9



 ## [Quick start](#quickstart)


### Development

#### Instale pre-commit hooks para linting e formatação

Todo código submetido deve ser checado quanto à formatação (black/prettier) e linting (flake8/isort).
Configure seu editor ou IDE de acordo com esses padrões.

Adicionalmente, para garantir que esses checks sejam realizadas a cada commit, instale os pre-commit hooks definidos para o projeto.
Para isso, faça o download da ferramenta `pre-commit` (https://pre-commit.com) e execute:

```sh
pre-commit install
```

#### Instale docker e docker-compose

Instale o `docker` e `docker-compose` segundo a documentação oficial.

No Ubuntu, as linhas abaixo podem ser usadas para instalar ambos.
Porém, versões mais atualizadas do `docker-compose` podem ser encontradas no [repositório oficial](https://github.com/docker/compose) :

```
# docker-ce-edge:
curl -L  "https://get.docker.com"  -o get-docker.sh
sh get-docker.sh
sudo usermod -aG docker `whoami`

# docker-compose:
sudo curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Você deve precisar reiniciar o seu computador para que o Docker Daemon inicie corretamente.

Para inciar a aplicação com docker compose, basta rodar o comando abaixo:

```sh
docker compose up -d
```
