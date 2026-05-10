# 🛡️ Sistema de Playlist - Checklist de Desenvolvimento

Este checklist detalha as etapas de construção do backend para o aplicativo de músicas, focando na implementação manual de estruturas de dados e organização orientada a objetos, conforme os requisitos da disciplina.

## 🟢 1. Configuração e Infraestrutura
- [x] Inicializar repositório Git e configurar `.gitignore`.
- [x] Criar ambiente virtual Python (`python -m venv .venv`).
- [x] Ativar o ambiente virtual e criar o arquivo `requirements.txt`.
- [x] **Estrutura de Pastas:** Criar diretório `classes/` para os módulos e `main.py` para o ponto de entrada.

## 🔵 2. Modelagem de Dados (POO & Nodos)
- [x] **Classe `Musica`:** Implementar atributos `id`, `titulo`, `artista`, `genero` e `bpm`.
- [x] **ID Sequencial:** Implementar lógica para gerar IDs automáticos que não se repetem, mesmo após remoções.
- [ ] **Classe `NodoLista`:** Criar o nó para a lista encadeada (armazenar objeto `Musica` e referência `proximo`).
- [ ] **Classe `NodoFila`:** Criar o nó encadeado usado internamente pela fila.

## 🟡 3. Implementação das Estruturas Manuais
- [ ] **Classe `Biblioteca` (Lista Encadeada Simples):**
    - [ ] Implementar inserção ao final da lista.
    - [ ] Implementar remoção por ID com ajuste de ponteiros.
    - [ ] Implementar busca por ID ou Título.
    - [ ] Implementar percurso para listagem completa.
- [ ] **Classe `Fila` (FIFO):**
    - [ ] Implementar método `enqueue` (enfileirar).
    - [ ] Implementar método `dequeue` (desenfileirar).
    - [ ] Implementar percurso para exibir a fila sem remover elementos.

## 🟠 4. Lógica de Negócio e Playlists
- [ ] **Classificação por Humor:** Criar lógica baseada nas faixas de BPM (Relaxar, Focar, Animar, Treinar).
- [ ] **Sincronização:** Implementar a limpeza das filas de humor antes de remontá-las a partir da biblioteca atual.
- [ ] **Sistema de Reprodução:** Lógica para retirar da fila de humor (`dequeue`) e inserir automaticamente na instância de **Histórico**.
- [ ] **Estatísticas:** Implementar contadores para o total da biblioteca, tamanho de cada fila e total reproduzido.

## ⚪ 5. Interface e Robustez
- [ ] **Menu Principal:** Criar interface interativa com as 10 operações solicitadas.
- [ ] **Tratamento de Exceções:**
    - [ ] Validar se BPM é numérico e > 0.
    - [ ] Tratar busca por ID inexistente.
    - [ ] Validar tentativa de reprodução em fila vazia.

## 🔴 6. Finalização e Entrega
- [ ] **Restrição Técnica:** Garantir que **nenhuma** estrutura pronta (`list`, `deque`, etc.) seja usada nas coleções principais.
- [ ] **Histórico:** Garantir que a fila de histórico seja uma instância separada da classe `Fila`.
- [ ] **GitHub:** Realizar entregas incrementais (commits regulares) para cumprir o critério de avaliação.
- [ ] **Documentação:** Atualizar o `README.md` com as instruções de execução e status.

---
*Status Atual: 🚧 Em desenvolvimento*