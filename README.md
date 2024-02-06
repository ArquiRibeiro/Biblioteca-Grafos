# Biblioteca Python para Grafos (Spider)

Esta biblioteca foi construída como trabalho prático para a disciplina de **Algoritmos em Grafos** no curso de **Sistemas de Informação**, 4° período, com as seguintes funcionalidades:

- Criação de grafos.
- Adição/remoção de vértices.
- Adição/remoção de arestas.
- Verificação de incidência entre vértices.
- Verificação se o grafo é vazio ou completo.
- Contagem de vértices/arestas.
- Visualização da lista de adjacência.
- Implementação do *algoritmo de Dijkstra*.
- Implementação do *algoritmo de Bellman-Ford*.
- Exportação no formato Pajek Net (dois arquivos de exemplo foram inclusos).

Como requisitos extras, arquivos de testes foram criados:

- **tests.py**: testes genéricos com a biblioteca, para comprovar seu funcionamento correto. Utiliza a biblioteca [unittest](https://docs.python.org/3/library/unittest.html) para a realização dos testes.
- **executionTimesTest.py**: testes de performance entre os algoritmos de *Dijkstra* e *Bellman-Ford*, com Grafos completos de 5, 50 e 500 vértices.