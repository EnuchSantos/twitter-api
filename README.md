# Mini API Twitter

Bom, está é uma API feita com Django Rest Framework e Django.
O modelo é para simular algumas funcionalidades do twitter, como criar um user, logar, seguir um user, postar um tweet e ver o tweet de outros usuários que você segue.


## Docker
O projeto está num formato para ser rodado dentro do ambiente docker, ou seja caso você utilize o docker só precisa seguir o tutorial abaixo normalmente e no final dar o comando "docker-compose up --build"

Para caso você não tenha o docker instalado e quer rodar o projeto no seu pc, aqui vai um pequeno passo a passo:
No arquivo settings, onde tiver "os.getenv('algo', 'change-me') no change-me você pode passar o valor correto, isso é para as conexões de banco em DATABASE e hosts em ALLOWED_HOSTS, DEBUG e SECRET_KEY
obs: caso não saiba os valores padrões, pode buscar no site: https://www.django-rest-framework.org/

ou também pode baixar essa versão onde do aplicativo ser dockerizado: https://github.com/EnuchSantos/twitter-api/tree/885b609289c68c3935af75400a9b9611192b101c

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

Agora que já foi tudo configurado só precisamos rodar o comando 'python manage.py runserver' e acessar a url: http://127.0.0.1:8000/
você será redirecionado para a API ROOT do django rest framework, aqui tem alguns endpoints para navegar pela API.

* Endpoints

No arquivo endpoints.json é possível importar as rotas prontas para testar a API, basta ter o insomnia baixar e ir em configurações > importar

* Modelagem do banco de dados

link: https://lucid.app/lucidchart/a24655dd-a715-411c-a41b-9a318eafac3b/edit?viewport_loc=-1295%2C-637%2C1692%2C1038%2C0_0&invitationId=inv_1874edcd-c396-491b-86d4-b4bfff6121b7

caso não tenha conta, segue o link da imagem: https://github.com/EnuchSantos/twitter-api/blob/main/database_model.png