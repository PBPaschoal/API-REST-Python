# API CRUD Simples com Python e FastAPI

Este repositório contém uma API RESTful desenvolvida com **Python** e **FastAPI**, ideal para aprender os conceitos básicos de criação, leitura e exclusão de itens (CRUD). A API utiliza uma estrutura modular e segue boas práticas para projetos escaláveis.

## 📋 **Funcionalidades**
- **Adicionar itens**: Endpoint `POST /items/` para cadastrar novos itens.
- **Listar itens**: Endpoint `GET /items/` para visualizar todos os itens cadastrados.
- **Deletar itens**: Endpoint `DELETE /items/{item_id}` para remover itens pelo índice.
- **Página inicial**: Endpoint `GET /` com uma mensagem de boas-vindas.

## 🛠 **Tecnologias Utilizadas**
- **Linguagem**: Python 3.10+
- **Framework**: FastAPI
- **Gerenciador de Dependências**: pip e virtualenv
- **Servidor**: Uvicorn
- **IDE**: Visual Studio Code

## 🚀 **Como Rodar o Projeto**

### **1. Clone o repositório**
```bash
git clone https://github.com/PBPaschoal/API-REST-Python.git
cd API-REST-Python
```
### **2.Crie um ambiente virtual**
```bash
python -m venv venv
```
### **3.Ative o ambiente virtual**
**Windows:**
```bash
venv\Scripts\activate
```
**Linux/MacOS:**
```bash
source venv/bin/activate
```

### **4.pip install fastapi uvicorn**
```bash
pip install fastapi uvicorn
```

### **5.Inicie o servidor**.**
```bash
uvicorn main:app --reload
```

### **6.Acesse a API**
- Documentação automática: http://127.0.0.1:8000/docs
- Documentação alternativa: http://127.0.0.1:8000/redoc
- Teste a API diretamente no navegador ou com ferramentas como Postman ou cURL.

### 📂 Estrutura do Projeto.
├── main.py            # Arquivo principal que inicia a aplicação
├── models
│   └── items.py       # Modelos de dados
├── routers
│   └── items.py       # Rotas para a manipulação de itens
└── README.md          # Documentação do projeto

### 📄 Rotas da API
#### **1. GET /**
- Retorna uma mensagem de boas-vindas.
- Exemplo de Resposta:
```bash
{
  "message": "Hello, World!"
}
```

### **2. POST /items/**
Adiciona um novo item.

**Parâmetros:**
- name (string): Nome do item (obrigatório).
- description (string): Descrição do item (opcional).
- price (float): Preço do item (obrigatório).
- tax (float): Taxa do item (opcional).

**Exemplo de Requisição:**

```bash
{
  "name": "Notebook",
  "description": "Um notebook potente.",
  "price": 2500.00,
  "tax": 250.00
}
```

**Exemplo de Resposta:**
```bash
{
  "item": {
    "name": "Notebook",
    "description": "Um notebook potente.",
    "price": 2500.00,
    "tax": 250.00
  }
}
```
### **3. GET /items/**
- Lista todos os itens cadastrados.
- Exemplo de Resposta:

```bash
{
  "items": [
    {
      "name": "Notebook",
      "description": "Um notebook potente.",
      "price": 2500.00,
      "tax": 250.00
    }
  ]
}
```

### **4. DELETE /items/{item_id}**
- Remove um item pelo índice.
- Exemplo de Resposta:

```bash
{
  "message": "Item removido com sucesso.",
  "item": {
    "name": "Notebook",
    "description": "Um notebook potente.",
    "price": 2500.00,
    "tax": 250.00
  }
}
```

## 🧑‍💻 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

## NOTA:
Eu procuro desenvolver meus projetos de forma independente, para praticar e consolidar meu aprendizado. No entanto, como ainda sou iniciante no desenvolvimento de APIs, contei com o apoio do ChatGPT para elaborar este projeto. Assim, consigo, na prática, entender, me familiarizar, testar, errar e aprender como funciona uma API REST. Este projeto é um passo importante no meu processo de evolução como desenvolvedor. @pbpaschoal