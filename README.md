# API AgendaPet

API REST desenvolvida em Python com Flask para gerenciamento de dados relacionados a pets, incluindo cadastro, histórico de vacinas e visitas ao veterinário.

## 📁 Estrutura do Projeto

```
API-agendaPET/
├── .vscode/                  # Configurações do editor (VS Code)
│   └── settings.json
├── routes/                   # Rotas Flask e classes de CRUD
│   └── ...
├── agendapet.db              # Banco de dados SQLite
├── app.py                    # Arquivo principal da aplicação Flask
├── schema.sql                # Script para criação do banco de dados
├── requirements.txt          # Dependências do projeto
├── README.md                 # Documentação do projeto
├── LICENSE                   # Licença de uso
└── .gitignore                # Arquivos ignorados pelo Git
```

## 🚀 Funcionalidades

* Cadastro e gerenciamento de pets
* Histórico de vacinas e visitas
* API RESTful com rotas CRUD
* Integração com Swagger para documentação

## 🧰 Tecnologias Utilizadas

* Python 3.11+
* Flask
* SQLite3
* Flasgger (para Swagger UI)

## 🛠️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/Almeedus/API-agendaPET.git
cd API-agendaPET
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados (opcional se já existir `agendapet.db`)

```bash
sqlite3 agendapet.db < schema.sql
```

### 5. Execute a aplicação

```bash
python app.py
```

A aplicação estará disponível em: [http://localhost:5000](http://localhost:5000)

### 6. Acesse a documentação Swagger

```
http://localhost:5000/apidocs/
```

## 📄 Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

## 🤝 Contribuições

Sinta-se à vontade para abrir issues e pull requests. Toda ajuda é bem-vinda para melhorar o projeto!

---

Desenvolvido com 💙 por [Almeedus](https://github.com/Almeedus)
