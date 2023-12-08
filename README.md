# RPS

Agente inteligente para Piedra, Papel, Tijeras

Este codigo permite enfrentar multiples agentes inteligentes y obtener graficos de los resultados

## Uso

- Añadir agentes en el archivo rps_agents.py y agregarlos en RPS_AGENTS
- Establecer las reglas y el numero de partidas en main
- Ejecutar

## Entorno de tareas

Entorno de tareas | Observable| Axentes | Determinista | Episódico | Estático | Discreto | Conocido
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
 RPS | Parcial | Multi | Estocástico | [Episódico](#conclusiones) | Estático | Discreto | Conocido |

## Conclusiones

El agente elegido que busca predecir al oponente es altamente efectivo contra otros agentes. 

![](./doc/full_view.png)

De todas formas este juego es episódico. En el momento en el que comenzamos a usar estrategias se vuelve secuencial. Un alto numero de victorias por parte de un agente en este test solo implica que, es mejor que el resto de los agentes contra los que compite, y no el mejor. La mejor estrategia será siempre elegir de forma aleatoria para maximizar los resultados, ya que no seguiremos un patron que se pueda explotar como se demuestra al enfrentarla contra la estrategía de predicciones y porque mantiene la varianza mas baja.

![](./doc/random_vs_predict.png)
![](./doc/variance.png)

## Requisitos

- Python 3.12.0
- Pytest
- Numpy
- Matplotlib