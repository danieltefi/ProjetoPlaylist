# 🛡️ Sistema de Playlist - Checklist de Desenvolvimento

Este checklist detalha as etapas de construção do backend para o aplicativo de músicas, focando na implementação manual de estruturas de dados e organização orientada a objetos, conforme os requisitos da disciplina.

## 🟢 1. Configuração e Infraestrutura
- [x] Inicializar repositório Git e configurar `.gitignore`.
- [x] Criar o arquivo `requirements.txt`.
- [x] **Estrutura de Pastas:** Criar diretório `classes/` para os módulos e `main.py` para o ponto de entrada.

## 🔵 2. Modelagem de Dados (POO & Nodos)
- [x] **Classe `Musica`:** Implementar atributos `id`, `titulo`, `artista`, `genero` e `bpm`.
- [x] **ID Sequencial:** Implementar lógica para gerar IDs automáticos que não se repetem, mesmo após remoções.
- [x] **Classe `NodoLista`:** Criar o nó para a lista encadeada (armazenar objeto `Musica` e referência `proximo`).
- [x] **Classe `NodoFila`:** Criar o nó encadeado usado internamente pela fila.

## 🟡 3. Implementação das Estruturas Manuais
- [x] **Classe `Biblioteca` (Lista Encadeada Simples):**
    - [x] Implementar inserção ao final da lista.
    - [x] Implementar remoção por ID com ajuste de ponteiros.
    - [x] Implementar busca por ID ou Título.
    - [x] Implementar percurso para listagem completa.
- [x] **Classe `Fila` (FIFO):**
    - [x] Implementar método `enqueue` (enfileirar).
    - [x] Implementar método `dequeue` (desenfileirar).
    - [x] Implementar percurso para exibir a fila sem remover elementos.

## 🟠 4. Lógica de Negócio e Playlists
- [x] **Classificação por Humor:** Criar lógica baseada nas faixas de BPM (Relaxar, Focar, Animar, Treinar).
- [x] **Sincronização:** Implementar a limpeza das filas de humor antes de remontá-las a partir da biblioteca atual.
- [x] **Sistema de Reprodução:** Lógica para retirar da fila de humor (`dequeue`) e inserir automaticamente na instância de **Histórico**.
- [x] **Estatísticas:** Implementar contadores para o total da biblioteca, tamanho de cada fila e total reproduzido.

## ⚪ 5. Interface e Robustez
- [x] **Menu Principal:** Criar interface interativa com as 10 operações solicitadas.
- [x] **Tratamento de Exceções:**
    - [x] Validar se BPM é numérico e > 0.
    - [x] Tratar busca por ID inexistente.
    - [x] Validar tentativa de reprodução em fila vazia.

## 🔴 6. Finalização e Entrega
- [x] **Restrição Técnica:** Garantir que **nenhuma** estrutura pronta (`list`, `deque`, etc.) seja usada nas coleções principais.
- [x] **Histórico:** Garantir que a fila de histórico seja uma instância separada da classe `Fila`.
- [x] **GitHub:** Realizar entregas incrementais (commits regulares) para cumprir o critério de avaliação.
- [ ] **Documentação:** Atualizar o `README.md` com as instruções de execução e status.

---
*Status Atual: 🚧 Em desenvolvimento*