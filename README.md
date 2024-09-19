# Delivery Chooser
An avaliation for AI class.

# Table of Contents

<!-- TOC -->
* [Delivery Chooser](#delivery-chooser)
* [Table of Contents](#table-of-contents)
* [Members](#members)
* [Getting Started](#getting-started)
  * [Run Tests](#run-tests)
  * [APIs](#apis)
* [Examples](#examples)
  * [No AI](#no-ai)
  * [With AI](#with-ai)
<!-- TOC -->

# Members

- [x] Cristian Prochnow
- [x] Gustavo Henrique Dias
- [x] Lucas Willian de Souza Serpa
- [x] Marlon de Souza
- [x] Ryan Gabriel Mazzei Bromati

# Getting Started

## Run Tests
```bash
$ python3 TestExtractor.py
```

## APIs
```python
from Extractor import Extractor

# get converted content from input/connections.csv
Extractor.get_connections()

# get converted content from input/deliveries.csv
Extractor.get_deliveries()
```

# Examples

## No AI

```text
2024-09-19 00:05:45,983 - INFO - Iniciando DeliveryOptimizer...
2024-09-19 00:05:45,983 - INFO - Processando conexões...
2024-09-19 00:05:45,983 - INFO - Conexões processadas com sucesso.
2024-09-19 00:05:45,983 - INFO - Dados carregados. Conexões e entregas foram processadas.
2024-09-19 00:05:45,983 - INFO - Iniciando o cálculo das entregas...
2024-09-19 00:05:45,983 - INFO - Processando entrega para B com bônus de 1 e tempo de início 0.
2024-09-19 00:05:45,983 - INFO - Calculando o caminho mais curto a partir de A...
2024-09-19 00:05:45,983 - INFO - Caminho mais curto calculado: {'A': 0, 'B': 5, 'C': 8, 'D': 2}
2024-09-19 00:05:45,983 - INFO - Entrega para B atrasada. Nenhum bônus.
2024-09-19 00:05:45,983 - INFO - Processando entrega para C com bônus de 10 e tempo de início 5.
2024-09-19 00:05:45,983 - INFO - Calculando o caminho mais curto a partir de A...
2024-09-19 00:05:45,983 - INFO - Caminho mais curto calculado: {'A': 0, 'B': 5, 'C': 8, 'D': 2}
2024-09-19 00:05:45,983 - INFO - Entrega para C no tempo! Bônus ganho: 10
2024-09-19 00:05:45,983 - INFO - Processando entrega para D com bônus de 8 e tempo de início 10.
2024-09-19 00:05:45,983 - INFO - Calculando o caminho mais curto a partir de A...
2024-09-19 00:05:45,983 - INFO - Caminho mais curto calculado: {'A': 0, 'B': 5, 'C': 8, 'D': 2}
2024-09-19 00:05:45,983 - INFO - Entrega para D no tempo! Bônus ganho: 8
2024-09-19 00:05:45,983 - INFO - Bônus total ganho: 18
```

## With AI

```text
2024-09-19 00:05:45,984 - INFO - Building graph with nodes: ['A', 'B', 'C', 'D']
2024-09-19 00:05:45,984 - INFO - Adding edge from A to B with time 5
2024-09-19 00:05:45,984 - INFO - Adding edge from A to D with time 2
2024-09-19 00:05:45,984 - INFO - Adding edge from B to A with time 5
2024-09-19 00:05:45,984 - INFO - Adding edge from B to C with time 3
2024-09-19 00:05:45,984 - INFO - Adding edge from C to B with time 3
2024-09-19 00:05:45,984 - INFO - Adding edge from C to D with time 8
2024-09-19 00:05:45,984 - INFO - Adding edge from D to A with time 2
2024-09-19 00:05:45,984 - INFO - Adding edge from D to C with time 8
2024-09-19 00:05:45,984 - INFO - Graph built: {'A': [('B', 5), ('D', 2), ('B', 5), ('D', 2)], 'B': [('A', 5), ('A', 5), ('C', 3), ('C', 3)], 'D': [('A', 2), ('C', 8), ('A', 2), ('C', 8)], 'C': [('B', 3), ('B', 3), ('D', 8), ('D', 8)]}
2024-09-19 00:05:45,984 - INFO - Initial deliveries: [{'start_time': 0, 'target': 'B', 'bonus': 1}, {'start_time': 5, 'target': 'C', 'bonus': 10}, {'start_time': 10, 'target': 'D', 'bonus': 8}]
2024-09-19 00:05:45,984 - INFO - Exploring: current_time=0, current_bonus=0, current_location=A, path=[]
2024-09-19 00:05:45,984 - INFO - Considering delivery to B: new_time=5, delivery_start_time=0
2024-09-19 00:05:45,984 - INFO - Pushing to queue: new_time=10, new_bonus=1, path=['B']
2024-09-19 00:05:45,984 - INFO - Considering delivery to D: new_time=10, delivery_start_time=10
2024-09-19 00:05:45,984 - INFO - Pushing to queue: new_time=12, new_bonus=8, path=['D']
2024-09-19 00:05:45,984 - INFO - Exploring: current_time=10, current_bonus=1, current_location=A, path=['B']
2024-09-19 00:05:45,984 - INFO - Considering delivery to D: new_time=12, delivery_start_time=10
2024-09-19 00:05:45,984 - INFO - Pushing to queue: new_time=14, new_bonus=9, path=['B', 'D']
2024-09-19 00:05:45,984 - INFO - Exploring: current_time=12, current_bonus=8, current_location=A, path=['D']
2024-09-19 00:05:45,984 - INFO - Considering delivery to B: new_time=17, delivery_start_time=0
2024-09-19 00:05:45,984 - INFO - Pushing to queue: new_time=22, new_bonus=9, path=['D', 'B']
2024-09-19 00:05:45,984 - INFO - Exploring: current_time=14, current_bonus=9, current_location=A, path=['B', 'D']
2024-09-19 00:05:45,984 - INFO - Exploring: current_time=22, current_bonus=9, current_location=A, path=['D', 'B']
2024-09-19 00:05:45,984 - INFO - Best delivery sequence: ['B', 'D']
2024-09-19 00:05:45,984 - INFO - Total profit: 9
2024-09-19 00:05:45,985 - INFO - Best solution found: (9, ['B', 'D'])
```
