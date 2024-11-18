# Configuração do Ambiente de Desenvolvimento para o Projeto Django

Este guia descreve como configurar o ambiente de desenvolvimento para o projeto Django e criar o banco de dados MySQL.

---

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados:
- Python 3.8 ou superior
- MySQL Server
- `pip` (gerenciador de pacotes do Python)
- Virtualenv

---

## Passos de Configuração

### 1. Clonar o Repositório
git clone [<URL_DO_REPOSITORIO>](https://github.com/rb-alves/prova-integrada-senac.git)

### 2. Criar o ambiente virtual
Abra o terminal
python -m venv .venv

### 3. Ativar o ambiente virtual
Ainda no terminal
.\.venv\Scripts\activate

### 4. Instale as dependências listadas no arquivo requirements.txt
pip install -r requirements.txt

### 4. Abra o MySQL e crie o banco de dados 'avaliacoes' (Não é necessário criar tabelas apenas crie o banco vazio)
CREATE DATABASE avaliacoes;

### 5. Configurando o banco de dados
Edite o arquivo settings.py do projeto Django para adicionar as configurações do banco de dados:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'avaliacoes',
        'USER': 'seu_usuario_mysql',
        'PASSWORD': 'sua_senha_mysql',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

### 6. Aplique as migrações
No terminal
python manage.py migrate

### 7. Rode a aplicação
python manage.py runserver




