# Simulador de Antena Parabólica

## Descripción
Este proyecto simula la reflexión de ondas electromagnéticas en una antena parabólica, demostrando visualmente cómo una superficie con forma de parábola concentra rayos paralelos en un único punto focal. La simulación es interactiva, permitiendo al usuario modificar la curvatura de la parábola y observar cómo esto afecta la ubicación del punto focal y la reflexión de los rayos.

## Características
- Simulación visual de rayos paralelos incidiendo en una superficie parabólica
- Control interactivo de la curvatura de la parábola mediante un slider
- Visualización dinámica de la ecuación de la parábola (y = ax²)
- Cálculo y visualización de la posición del foco en tiempo real
- Animación de la reflexión de rayos

## Fundamento Científico

### ¿Cómo funciona una antena parabólica?
Una antena parabólica aprovecha una propiedad matemática fundamental de las parábolas: todos los rayos que inciden paralelos al eje de simetría se reflejan hacia un único punto, llamado foco.

### Principios físicos y matemáticos

#### Ecuación de la parábola
La parábola está definida por la ecuación:
```
y = ax²
```
Donde `a` es el parámetro que define la curvatura de la parábola.

#### Cálculo del foco
La posición del foco para una parábola con ecuación y = ax² se encuentra en el punto:
```
F = (0, 1/(4a))
```
Esto significa que:
- Cuanto mayor sea el valor de `a`, más cerrado será el foco (más cerca del vértice)
- Cuanto menor sea el valor de `a`, más abierto será el foco (más lejos del vértice)

#### Ley de reflexión
La simulación implementa la ley de reflexión de la óptica:
- El ángulo de incidencia es igual al ángulo de reflexión
- En una parábola, esta propiedad hace que todos los rayos paralelos al eje converjan en el foco

### Aplicaciones prácticas
Las antenas parabólicas se utilizan en numerosas aplicaciones:

1. **Telecomunicaciones**: Recepción de señales de satélite para televisión, internet y telefonía
2. **Radioastronomía**: Captación de ondas de radio procedentes del espacio
3. **Energía solar**: Concentradores solares parabólicos
4. **Radar**: Sistemas de detección y seguimiento
5. **Linternas y faros**: Concentración de luz en un haz

## Interpretación de la simulación

En la simulación:
- La **curva azul** representa la superficie parabólica (antena)
- El **punto negro** representa el foco
- Las **líneas rojas punteadas** representan los rayos incidentes (paralelos al eje Y)
- Las **líneas verdes** representan los rayos reflejados que convergen en el foco

Al mover el slider, se puede observar:
1. Cómo cambia la curvatura de la parábola
2. Cómo se desplaza el punto focal
3. Cómo los rayos reflejados siempre convergen en el foco independientemente de la curvatura

## Requisitos
- Python 3.6 o superior
- Matplotlib
- NumPy

## Ejecución
Para ejecutar la simulación:
```
python parabola_simulator.py
```

## Consideraciones para diseño de antenas reales
En la práctica, el diseño de antenas parabólicas considera factores adicionales:
- **Relación focal** (f/D): La relación entre la distancia focal y el diámetro de la antena
- **Eficiencia de apertura**: Qué porcentaje de la señal incidente se captura efectivamente
- **Ganancia**: Capacidad de la antena para concentrar la señal
- **Lóbulos laterales**: Patrones de radiación no deseados

## Conclusión
Esta simulación proporciona una representación visual del principio fundamental que hace que las antenas parabólicas sean tan efectivas para concentrar ondas electromagnéticas en un único punto. La propiedad matemática de la parábola permite diseñar receptores altamente eficientes para comunicaciones, astronomía y muchas otras aplicaciones.