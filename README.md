# Projeto de Gestão de Plantio e Análises Climáticas

Este projeto combina **Python** e **R** para gerenciar dados de plantio e executar análises estatísticas e climáticas.

## 📁 Estrutura do Projeto

```
projeto_r/
│── services/
│   └── weatherLocationService.R
│── webservices/
│   ├── locationWS.R
│   ├── weatherWS.R
│   └── main.R
│── src/
│   ├── __pycache__/
│   ├── engine.py
│   ├── menu.py
│── tb1-env/
│── .gitignore
│── main.py
│── requirements.txt
│── storage.json
```

- **`main.py`**: Arquivo principal que gerencia o fluxo do programa.
- **`src/engine.py`**: Funções para manipulação dos dados de plantio.
- **`src/menu.py`**: Exibição do menu interativo.
- **`projeto_r/`**: Scripts em **R** para análises estatísticas e climáticas.
- **`storage.json`**: Armazena os dados de plantio.
- **`requirements.txt`**: Dependências do projeto.

## 🚀 Como Executar

### 1️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2️⃣ Executar o Projeto

```bash
python main.py
```

## 🔧 Funcionalidades

1. **Adicionar dados de plantio**  
2. **Visualizar dados cadastrados**  
3. **Atualizar dados existentes**  
4. **Excluir registros**  
5. **Executar análises estatísticas (R)**  
6. **Obter dados climáticos de uma cidade (R)**  
7. **Sair do programa**  

## 📊 Execução de Scripts em R

Os scripts em **R** podem ser acionados pelo `main.py` para:
- **Estatísticas de plantio:** `projeto_r/main.R`
- **Dados climáticos por cidade:** `projeto_r/services/weatherLocationService.R`

## 📌 Observações
- Os dados de plantio são armazenados em `storage.json`.
- O programa requer **Python 3.x** e **R instalado no sistema** para executar os scripts.

---

Desenvolvido para integração entre **Python** e **R**, facilitando o gerenciamento agrícola e análises meteorológicas. 🌱🌤️
```

Esse README fornece uma visão geral do projeto, suas funcionalidades e como executá-lo. Quer adicionar algo específico? 🚀
