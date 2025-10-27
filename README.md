🚚 Rastreamento de Pedidos - MDF Móveis

Aplicação web desenvolvida em Flask (Python) para consulta de pedidos de clientes, com integração às APIs uMov.me (Entrega e Montagem) e ao banco de dados MySQL.
O sistema utiliza Google reCAPTCHA v2 para validação de usuários e Bootstrap 5 para o layout responsivo.

🧩 Estrutura do Projeto
📦 rastreio-entrega/
├── static/
│   ├── img/
│   │   └── logo mdf.png
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── .env                 # Variáveis de ambiente (não versionado)
├── .env.example         # Exemplo de configuração
├── .gitignore
├── api_umov_entrega.py  # Integração com API uMov.me (Entrega)
├── api_umov_montagem.py # Integração com API uMov.me (Montagem)
├── app.py               # Aplicação principal Flask
└── requirements.txt     # Dependências do projeto

⚙️ Pré-requisitos

Antes de executar, instale:

Python 3.10+

pip

Banco de dados MySQL

Chaves do Google reCAPTCHA v2 (Checkbox “Não sou um robô”)

🧾 Instalação
1. Clone o repositório
git clone https://github.com/seuusuario/rastreio-entrega.git
cd rastreio-entrega

2. Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate     # Windows
# ou
source .venv/bin/activate  # Linux/Mac

3. Instale as dependências
pip install -r requirements.txt

4. Configure as variáveis de ambiente

Copie o arquivo .env.example para .env:

cp .env.example .env


Edite o .env:

# Banco de dados
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASS=senha
DB_NAME=starmoveis_custom

# Flask
SECRET_KEY=sua_chave_segura

# Google reCAPTCHA
RECAPTCHA_SITE_KEY=sua_site_key
RECAPTCHA_SECRET_KEY=sua_secret_key

# APIs uMov.me
UMOV_TOKEN_ENTREGA=token_entrega
UMOV_TOKEN_MONTAGEM=token_montagem

🚀 Execução do Projeto
python app.py


A aplicação estará disponível em:
👉 http://127.0.0.1:5000

🧠 Funcionalidades

✅ Consulta de pedidos por CPF/CNPJ
✅ Exibição da situação atual (Entrega e Montagem)
✅ Histórico completo de etapas e eventos
✅ Integração com uMov.me via API
✅ Validação humana via Google reCAPTCHA v2
✅ Interface moderna e responsiva com Bootstrap 5

📡 Endpoints da API
/api/pedidos

Consulta os pedidos do cliente pelo CPF/CNPJ.

Exemplo:

GET /api/pedidos?cpf=123.456.789-00&captcha=<token>

/api/detalhes

Retorna informações completas de um pedido.

🧪 Teste Local do reCAPTCHA

Use as chaves de teste do Google:

RECAPTCHA_SITE_KEY=6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI
RECAPTCHA_SECRET_KEY=6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe


Essas chaves sempre validam o CAPTCHA e são seguras para ambiente local.

🔒 Segurança

Variáveis sensíveis armazenadas no .env

O arquivo .env não é versionado

O Flask usa SECRET_KEY para sessões seguras

🧩 Autor

👨‍💻 Roberto Alves
📧 roberto.alves@mdfmoveis.com.br

🏢 Projeto interno — MDF Móveis

🧾 Licença

Este projeto é de uso interno e restrito à MDF Móveis.
