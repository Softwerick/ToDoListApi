Como rodar o projeto:

- Para começar, baixe o projeto presente neste repositório
- Tenha certeza que o python3 e o pip estão instalados
- Em seguida, vá até a pasta que ele se encontra e crie um ambiente virtual com o comando: python3 -m venv nomedasuavenv
- Ative o ambiente virtual usando o comando source nomedasuavenv/bin/activate
- Instale as dependências do projeto utilizando o comando pip install -r requirements.txt
- Após isso, entre na pasta todoapi, que é onde se encontra o projeto
- Utilize os comandos python manage.py makemigrations e python manage.py migrate para migrar o banco de dados
- Feito isso, utilize o comando python manage.py runserver para que o projeto comece a ser executado

Observação1: Para que os testes funcionem, é necessrio que tenha uma / no final das urls. Exemplo: http://localhost:xxxx/api/tasks/
Observação2: Os testes realizados no terminal funcionam, mas para visualizar o tipo de resposta HTTP, é necessário utilizar a aplicação no navegador

Visualizar Resposta HTTP: 

Utilizei uma ferramenta do djangorestframework que me traz uma interface pronta para realizar as diversas operações propostas pelo desafio.
Então, entre nesta url preenchendo o número da porta utilizada pelo django: http://localhost:xxxx/api/tasks/


Essa url mostrará todas as tasks criadas, com a HTTP Response 200
Também terá um form para criação de uma nova task, que retorna a HTTP Response 201

Para editar ou deletar uma task, utilize o ID dela na url
Exemplo: http://localhost:xxxx/api/tasks/3/
Ao ser editada, retorna a HTTP Response 200 e ao ser deletada, retorna a HTTP Response 204.

