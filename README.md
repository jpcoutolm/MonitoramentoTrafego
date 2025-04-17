# 📡 Monitoramento de Tráfego de Rede

Este projeto simula um sistema de monitoramento de dispositivos conectados a uma rede local. Utiliza um backend em Flask, frontend com Streamlit e visualizações interativas com Plotly, tudo containerizado com Docker.

---

## 🚀 Funcionalidades

- Registro de dispositivos com IP, nome e tráfego
- Visualização da lista de dispositivos cadastrados
- Gráficos de tráfego por dispositivo (barras)
- Indicadores de rede: total, média e status de tráfego
- Remoção de dispositivos diretamente pela interface
- Banco de dados SQLite gerado automaticamente

---

## 🛠 Tecnologias Utilizadas

- **Python**
- **Flask** (API backend)
- **Streamlit** (frontend interativo)
- **Plotly** (gráficos)
- **SQLite** (banco de dados local)
- **Docker & Docker Compose**

---

## 🗂 Estrutura de Diretórios

```
.
├── backend/
│   ├── app.py         # Código da API Flask
│   └── db.py          # Criação automática do banco SQLite
│
├── frontend/
│   └── app-front.py         # Interface com Streamlit e gráficos
│
├── database/          # Pasta onde o banco SQLite é gerado (vazia no repositório)
│
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
└── requirements.txt
```

---

## 🐳 Como Executar (com Docker)

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/monitoramento-rede.git
cd monitoramento-rede
```

### 2. Crie a pasta de banco (se não existir)

```bash
mkdir database
```

### 3. Suba os containers

```bash
docker-compose down --volumes --remove-orphans
docker-compose build --no-cache
docker-compose up
```

### 4. Acesse no navegador

- Frontend (Streamlit): [http://localhost:8501](http://localhost:8501)
- API (opcional): [http://localhost:5000/devices](http://localhost:5000/devices)

---

## 📸 Print da aplicação

> ⚠️ Adicione aqui uma imagem da interface depois de subir no GitHub:

```md
![Interface](./assets/print.png)
```

---

## 📄 Licença

Este projeto é de uso acadêmico e pode ser utilizado como base para estudos ou melhorias.

---
