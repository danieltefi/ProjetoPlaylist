# Segundo Projeto: Sistema de Playlist

## Sobre o Projeto
Este projeto consiste no desenvolvimento do backend de um aplicativo de gerenciamento de músicas. O sistema permite que o usuário gerencie sua biblioteca pessoal, organize filas de reprodução baseadas no humor (BPM) e consulte um histórico de reproduções.

O foco principal é a implementação manual de estruturas de dados fundamentais, como **Listas Encadeadas Simples** e **Filas (FIFO)**, utilizando o paradigma de **Orientação a Objetos** em Python.

### Operações Implementadas
*   **Gestão de Biblioteca:** Adição de músicas no final da lista e remoção por ID único.
*   **Busca Avançada:** Localização de faixas por ID ou título.
*   **Classificação por Humor (BPM):** Distribuição automática das músicas em filas específicas (Relaxar, Focar, Animar e Treinar).
*   **Sistema de Reprodução:** Consumo de músicas da fila (FIFO) com registro automático em uma fila de histórico separada.
*   **Estatísticas:** Monitoramento do total de músicas na biblioteca, tamanho das filas e histórico.

## 🛠️ Tecnologias e Conceitos
*   **Linguagem:** Python 3.
*   **Bibliotecas:** 
*   **Paradigma:** Orientação a Objetos (Classes, Atributos e Métodos).
*   **Estruturas de Dados Manuais:**
    *   **Lista Encadeada Simples:** Para armazenamento da biblioteca.
    *   **Fila FIFO (Linked Queue):** Para filas de reprodução e histórico.
*   **Estruturas Proibidas:** Não foram utilizadas estruturas *built-in* como `list` ou `deque` para as coleções principais.

## ⚙️ Configuração do Ambiente
O projeto utiliza um **ambiente virtual (venv)** para isolamento de dependências.

### Instalação e Ativação
1.  **Criar o Ambiente Virtual:**
    ```
    python -m venv .venv
    ```
2.  **Ativar o ambiente:**
    *   **Windows (PowerShell):** `.\.venv\Scripts\Activate.ps1`
    *   **Windows (CMD):** `.\.venv\Scripts\activate.bat`
    *   **Linux/macOS:** `source .venv/bin/activate`
3.  **Instalar Dependências:**
    ```
    pip install -r requirements.txt
    ```
**Execução:**
    * Com o venv ativo: main.py

## 📂 Estrutura de Arquivos
```text
├── .venv/               # Ambiente virtual isolado
├── classes/             # Módulos contendo as definições de Musica, Nodo e Fila
├── main.py              # Ponto de entrada com o menu interativo
├── .gitignore           # Define arquivos que o Git deve ignorar
├── README.md            # Documentação do projeto
└── requirements.txt     # Lista de dependências
```

## 📋 Requisitos Técnicos Respeitados
*   **ID Sequencial:** Gerado automaticamente sem reutilização após remoção.
*   **Tratamento de Erros:** Validação de entradas para BPM (numérico e > 0), IDs inexistentes e fila vazia ao tentar reproduzir.
*   **Gestão de Memória:** Implementação total baseada em nós encadeados e referências de ponteiros, sem o uso de estruturas prontas do Python.

## 🚧 Status do Projeto
**Em desenvolvimento**