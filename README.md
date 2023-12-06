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

Este juego es episódico. En el momento en el que comenzamos a usar estrategias se vuelve secuencial. Un alto numero de victorias por parte de un agente en este test solo implica que, es mejor que el resto de los agentes contra los que compite, y no el mejor. Por este motivo la mejor estrategia será siempre elegir de forma aleatoria para maximizar los resultados ya que no sigue un patron que se pueda explotar como demuestra la grafica de desviacion estandar.

## Requisitos

- Python 3.12.0
- Pytest
- Numpy
- Matplotlib