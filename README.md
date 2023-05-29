# Mini API Twitter

Bom, está é uma API feita com Django Rest Framework e Django.
O modelo é para simular algumas funcionalidades do twitter, como criar um user, logar, seguir um user, postar um tweet e ver o tweet de outros usuários que você segue.

## Configurando o projeto
* Ambiente virtual

Após baixar o projeto, na pasta onde ele estiver localizado use o comando 'python -m venv (nome que deseje)' para criar um ambiente virtual, assim quando for instalar suas dependencias, elas ficam em um único projeto evitando problemas de conflitos e etc.

* Dependencias

procure o arquivo requirements.txt pelo terminal e use o comando 'pip install -r requirements.txt'
dessa forma todas as dependencias são instaladas.

* Banco de dados

Eu uso no meu projeto o PostgreSQL, mas você pode usar qual desejar, apenas procure o arquivo settings.py e vá onde tem o objeto DATABASES, caso esteja usando o PostgreSQL, só precisa trocar os valores de conexão com o banco, se for outro banco, sugiro que pesquise as configurações dele para serem usadas com o Django.

* Variáveis de ambiente

Dentro do arquivo settings existem alguns dados sensíveis, então é ideal usar um .env para quando a aplicação estiver em produção. Eu subi um arquivo example_env.txt, você deve renomea-lo para .env e colocar os dados da sua aplicação como conexões com banco e a secret key do django.

* Comando antes de rodar a aplicação

Antes de rodar seu app você precisa rodar alguns comandos para criar as tabelas no banco, o django já cria automaticamente baseado em seus models.
comando 'python manage.py makemigrations' ele vai mapear as alterações e prepara-las para criar as tabelas
comando 'python manage.py migrate' agora ele cria as tabelas e estão prontas para serem usadas.

* Rodando a aplicação

Agora que já foi tudo configurado só precisamos rodar o comando 'python manage.py runserver' e acessar a url: http://http://127.0.0.1:8000/
você será redirecionado para a API ROOT do django rest framework, aqui tem alguns endpoints para navegar pela API.
