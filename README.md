# Conecta +

O “Conecta +”, irá servir como o facilitador de comunicações e organizações de projetos dos Caçadores de Bons Exemplos. 

Ele vai funcionar como uma plataforma de gerência dos caçadores onde será possível organizar contatos, conversas e informações de projetos e eventos diversos dos caçadores, aperfeiçoando a situação atual deles. 

Além disso, para amenizar a questão de resistência a novas tecnologia, planejamos implementar uma Inteligência Artificial que, através de um chatbot via whatsapp, fará o cadastramento e atualizações das informações de projetos ou de voluntários, a IA mandará as informações que ele recebeu do whatsapp para um banco de dados e essas informações serão organizadas no site de gerência de forma organizada e intuitiva para os voluntários dos caçadores e gestores dos Caçadores de Bons Exemplos.


<br>![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)



# Tutorial: Como rodar o nosso Projeto 

Este tutorial fornecerá instruções detalhadas sobre como configurar o ambiente, instalar as dependências e rodar o projeto Django. Certifique-se de seguir cada passo cuidadosamente.

##  Configurando o Ambiente Virtual

Certifique-se de ter o Python e o pip instalados. Em seguida, siga os passos abaixo:

## Instalando o ambiente virtual(venv)
pip install virtualenv

## Criando e ativando o Ambiente Virtual (No diretório do seu projeto)
virtualenv venv

## Ativando a venv
### No Windows
venv\Scripts\activate

### No Linux/Mac
source venv/bin/activate

O prompt de comando ou terminal agora deve exibir (venv) indicando que o ambiente virtual está ativado.

## Instalando Dependências
Certifique-se de estar com o ambiente virtual ativado. Em seguida, instale as dependências do projeto:

pip install -r requirements.txt

## Configurando o Banco de Dados 
Execute as migrações para configurar o banco de dados:

python manage.py makemigrations

python manage.py migrate

## Rodando o Projeto
Agora, você está pronto para iniciar o servidor Django. Certifique-se de estar no diretório do projeto e execute:

python manage.py runserver

Isso iniciará o servidor de desenvolvimento. Abra o navegador e acesse http://127.0.0.1:8000/ para visualizar o projeto!
Qualquer duvida só procurar algum dos integrantes do grupo!

# Colaboradores

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/114592376?s=48&v=4" width=115><br><sub>Danilo Albuquerque</sub>](https://github.com/dan-albuquerque) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/116087739?v=4" width=115><br><sub>Diogo Henrique</sub>](https://github.com/Fiend3333) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/111147078?s=48&v=4" width=115><br><sub>Gabriel Pires</sub>](https://github.com/gabrielpires-1) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/125616055?s=64&v=4" width=115><br><sub>João Pedro Araujo</sub>](https://github.com/joaopedrofds) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/117311923?s=64&v=4" width=115><br><sub>Matheus Canel</sub>](https://github.com/matheuscanel) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/103130662?v=4" width=115><br><sub>Yara Rodrigues</sub>](https://github.com/Yara-R) |
| :---: | :---: | :---: | :---: | :---: | :---: |
