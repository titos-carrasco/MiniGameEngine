# MiniGameEngine
Mini motor de juegos escrito en python.

* Utiliza sólo tkinter y requierePython 3.8+
* La documentación se encuentra en doc/
* Algunos ejemplos se encuentran en ejemplos/

![Texto Alternativo](images/Aliens.png)

![Texto Alternativo](images/BlueBird.png)

![Texto Alternativo](images/DuckHunt.png)

![Texto Alternativo](images/Galaxian.png)

![Texto Alternativo](images/Invaders.png)

![Texto Alternativo](images/Monedas.png)

![Texto Alternativo](images/Platformer.png)

![Texto Alternativo](images/RallyX.png)


*La imágenes utilizadas en los ejemplos fueron obtenidas desde https://opengameart.org/*

## Nota
Tkinter es lento con muchas operaciones sobre el canvas.
En el ejemplo *"BlueBird/"* se utilizan 30 Sprites cambiando su imagen y moviéndose 1/60 veces por segundo.
Utilizando cProfile se observa que el método *'call'* de tkinter utiliza casi el 80% del tiempo de procesamiento en Linux


## Durante el desarrollo
* pip install -e .
* En VSCODE: File -> Preferences -> Settings: Buscar y Marcar "Python: Execute In File Dir"
* Verificación de código: ``$ pylint --module-naming-style PascalCase --method-naming-style camelCase src/MiniGameEngine/``
* Generación de documentación: ``$ pdoc -o doc --no-search --no-show-source -d google MiniGameEngine``
* Generación del WHL: ``$ python setup.py bdist_wheel``
