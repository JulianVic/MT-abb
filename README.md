# Simulación de una Máquina de Turing con Interfaz Gráfica

## Descripción

Este proyecto implementa una **Máquina de Turing (MT)** en Python con una interfaz gráfica desarrollada en **Tkinter**. La MT valida cadenas que siguen el patrón $(ab^2)^n$, donde $n > 0$. El sistema permite al usuario ingresar cadenas, validarlas y visualizar los resultados en una tabla interactiva.

### Características:
- Valida cadenas que cumplen con el patrón $(ab^2)^n$.
- Proporciona una interfaz gráfica para ingresar cadenas y ver resultados.
- Simula el comportamiento de una MT con expansión dinámica de la cinta y movimientos de la cabeza de lectura.
  
## Requisitos

Para ejecutar el proyecto necesitas tener instalado:

- **Python 3.x**
- **Tkinter** (viene preinstalado con la mayoría de las distribuciones de Python)

## Instalación

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2. Asegúrate de que tienes **Python** instalado. Si no lo tienes, puedes descargarlo [aquí](https://www.python.org/downloads/).

3. Ejecuta el archivo principal del proyecto:
    ```bash
    python main.py
    ```

## Uso

1. Ejecuta el archivo principal. Aparecerá una ventana con el título **MT abb**.
2. Ingresa una cadena en el campo de texto.
3. Haz clic en el botón **Validar**.
4. El resultado de la validación (válido/inválido) aparecerá en la tabla.

### Ejemplos de cadenas válidas:

- `abb`
- `abbabb`
- `abbabbabb`

### Ejemplos de cadenas no válidas:

- `ab`
- `abbb`
- `aaabb`

## Diagrama de la Máquina de Turing

Aquí tienes el diagrama de la Máquina de Turing que sigue el patrón $(ab^2)^n$:

![Diagrama de la MT](mt-design-jflap.png)

## Detalles Técnicos

### Máquina de Turing
La MT se define formalmente como una tupla $M = (Q, \Sigma, \Gamma, s, b, F, \delta)$, donde:
- $Q = \{ q_0, q_1, q_2, q_3, q_4 \}$ es el conjunto finito de estados.
- $\Sigma = \{ a, b \}$ es el alfabeto de entrada.
- $\Gamma = \{ a, b, \textvisiblespace \}$ es el alfabeto de la cinta.
- $s = q_0$ es el estado inicial.
- $b = \textvisiblespace$ es el símbolo de espacio en blanco.
- $F = \{ q_4 \}$ es el conjunto de estados de aceptación.
- $\delta$ es la función de transición que procesa la cinta y avanza la cabeza de la MT.

### Interfaz gráfica
La interfaz gráfica fue desarrollada utilizando Tkinter y proporciona una experiencia de usuario simple e intuitiva. Las principales funcionalidades son:
- Campo de texto para ingresar la cadena.
- Botón **Validar** para ejecutar la MT y ver los resultados.
- Tabla que muestra si las cadenas ingresadas son válidas o no.
  
## Pruebas realizadas

El sistema fue probado con varias cadenas para verificar su correcto funcionamiento:

- **Cadenas válidas** como `abb` y `abbabb` fueron correctamente validadas.
- **Cadenas inválidas** como `ab` y `abbb` fueron rechazadas apropiadamente.

## Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un **fork** de este repositorio.
2. Crea una nueva rama para tu función o corrección de errores.
    ```bash
    git checkout -b mi-rama
    ```
3. Realiza los cambios y commitea.
    ```bash
    git commit -m "Mi contribución"
    ```
4. Envía un **pull request** con tus mejoras.