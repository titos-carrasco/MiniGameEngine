import sys
import time
import ctypes
import glob
import tkinter as tk


class GameWorld:
    _instance_ = None

    def _getInstance():
        return GameWorld._instance_

    # ---

    def __init__(
        self,
        width: int,
        height: int,
        title: str = "MiniGameEngine",
        bgColor: str = "gray",
        bgPath: str = None,
        numLayers: int = 10,
    ):
        """
        Constructor de la clase GameWorld que inicializa una instancia del mundo de juego.

        Args:
            width (int): Ancho de la ventana del juego.
            height (int): Altura de la ventana del juego.
            title (str, optional): Título de la ventana del juego (por defecto es "MiniGameEngine").
            bgColor (str, optional): Color de fondo de la ventana del juego (por defecto es "gray").
            bgPath (str, optional): Ruta de la imagen de fondo de la ventana del juego (por defecto es None).
            numLayers (int, optional): Numero de capas a permitir en el juego (por defecto es 10).
        """
        if not GameWorld._instance_ is None:
            raise Exception("Ya existe una instancia de GameWorld activa!!!")

        self.win = tk.Tk()
        self.win.geometry("%dx%d" % (width, height))
        self.win.title(title)
        self.win.resizable(False, False)

        self.canvas = tk.Canvas(self.win, width=width, height=height, bg=bgColor)
        self.canvas.place(x=0, y=0)

        self.images = {}

        self.bgpic = None
        self.setBgPic(bgPath)

        self.numLayers = numLayers

        self.keys = {}
        self.tick_prev = 0
        self.fps = 0
        self.gObjects = []
        self.running = False
        GameWorld._instance_ = self

    def _getCanvas(self) -> tk.Canvas:
        return self.canvas

    def loadImage(self, imagePath: str) -> tk.PhotoImage:
        """
        Carga la imagen que se encuentra en la ruta especificada

        Args:
            imagePath (str): Ruta de la imagen a cargar.

        Returns:
            binary: La imagen cargada.
        """
        if not imagePath in self.images:
            self.images[imagePath] = tk.PhotoImage(file=imagePath)
        return self.images[imagePath]

    def loadImages(self, imagesPaths: list) -> list:
        """
        Carga las imagenes referenciadas por el arreglo de rutas

        Args:
            imagesPaths (list): Arreglo de rutas a las imagenes a cargar.

        Returns:
            list : Arreglo con las imágenes cargadas.
        """
        images = []
        [images.append(self.loadImage(path)) for path in imagesPaths]
        return images

    def setBgPic(self, bgPath: str):
        """
        Cambia la imagen de fondo

        Args:
            bgPath (str): Ruta a la imagen a utilizar como fondo
        """
        if not self.bgpic is None:
            self.canvas.delete(self.bgpic)
        img = self.loadImage(bgPath)
        self.bgpic = self.canvas.create_image(
            0, 0, image=img, anchor=tk.NW, tags=("Layer 0",)
        )
        self.canvas.tag_lower(self.bgpic, "all")

    def gameLoop(self, fps: int):
        """
        Inicia el loop principal del juego.

        Args:
            fps (int): Número de cuadros por segundo del juego.
        """
        self.fps = fps
        self.fps_time = 1 / self.fps
        self.tick_prev = time.perf_counter()

        self.running = True
        self.win.protocol("WM_DELETE_WINDOW", self.exitGame)
        while self.running:
            self._doAddGameObjects()
            dt = self._doRefresh()
            self.onUpdate(dt)
            self._doUpdateGameObjects(dt)
            self._doCheckCollisions(dt)
            self._doDelGameObjects()
        self.win.destroy()

        self.gObjects = None
        self.keys = None
        self.bgPic = None
        self.images = None
        self.canvas = None
        self.win = None
        self._instance_ = None

    def exitGame(self):
        """
        Finaliza el loop principal del juego
        """
        self.running = False

    def onUpdate(self, dt: float):
        """
        Llamada por cada ciclo dentro del loop (fps veces por segundo)

        Args:
            dt (float): Tiempo en segundos desde la última llamada
        """
        pass

    def _addGObject(self, gobj):
        if not hasattr(gobj, "__status__"):
            gobj.__status__ = "new"
            if gobj.layer < 1 or gobj.layer >= self.numLayers:
                gobj.layer = 1
            self.gObjects.append(gobj)
            [
                self.canvas.tag_raise("Layer " + str(layer), "all")
                for layer in range(1, self.numLayers + 1)
            ]
            self.canvas.tag_raise(TextObject._layer_, "all")

    def _doAddGameObjects(self):
        for o in self.gObjects:
            if o.__status__ == "new":
                if o.shape > 0:
                    self.canvas.itemconfig(o.shape, state="normal")
                o.__status__ = "alive"

    def _delGObject(self, gobj):
        if hasattr(gobj, "__status__"):
            gobj.__status__ = "dead"

    def _doDelGameObjects(self):
        gobjs = [o for o in self.gObjects if o.__status__ == "dead"]
        [self.gObjects.remove(o) for o in gobjs]

    def _doUpdateGameObjects(self, dt):
        [o.onUpdate(dt) for o in self.gObjects if o.__status__ == "alive"]

    def _doCheckCollisions(self, dt):
        gobjs1 = [o for o in self.gObjects if o.__status__ == "alive" and o.collisions]
        gobjs2 = gobjs1.copy()
        for o1 in gobjs1:
            gobjs2.pop(0)
            if o1.__status__ != "alive" or not o1.collisions or o1.shape < 0:
                continue
            for o2 in gobjs2:
                if o2.__status__ != "alive" or not o2.collisions or o2.shape < 0:
                    continue
                if self.collide(o1, o2):
                    o1.onCollision(dt, o2)
                    o2.onCollision(dt, o1)

    def collide(self, o1, o2) -> bool:
        """
        Detecta si dos GameObjects colisionan entre si

        Args:
            o1 (GameObject): El GameObject a verificar si colisiona con o2
            o2 (GameObject): El GameObject a verificar si colisiona con o1

        Returns:
            bool: True si colisionan. False en caso contrario.
        """
        if o1 == o2:
            return False
        if o1.__status__ != "alive" or o2.__status__ != "alive":
            return False

        if o1.shape < 0 or o2.shape < 0:
            return False

        o1x1 = o1.getX() - o1.getWidth() / 2
        o1y1 = o1.getY() - o1.getHeight() / 2
        o1x2 = o1x1 + o1.getWidth() - 1
        o1y2 = o1y1 + o1.getHeight() - 1

        o2x1 = o2.getX() - o2.getWidth() / 2
        o2y1 = o2.getY() - o2.getHeight() / 2
        o2x2 = o2x1 + o2.getWidth() - 1
        o2y2 = o2y1 + o2.getHeight() - 1

        return o1x1 <= o2x2 and o2x1 <= o1x2 and o1y1 <= o2y2 and o2y1 <= o1y2

    def _doRefresh(self):
        self.win.update_idletasks()
        self.win.update()

        now = self._tick()
        dt = now - self.tick_prev
        self.tick_prev = now

        return dt

    if sys.platform == "win32":

        def _tick(self):
            ctypes.windll.winmm.timeBeginPeriod(1)
            while time.perf_counter() - self.tick_prev < self.fps_time:
                time.sleep(0.0001)
            ctypes.windll.winmm.timeEndPeriod(1)
            return time.perf_counter()

    else:

        def _tick(self):
            while time.perf_counter() - self.tick_prev < self.fps_time:
                time.sleep(0.0001)
            return time.perf_counter()

    def isPressed(self, key_name: str) -> bool:
        """
        Verifica si una tecla específica está siendo presionada.

        Args:
            key_name (str): Nombre de la tecla a verificar.

        Returns:
            bool: True si la tecla está presionada, False en caso contrario.
        """
        if not key_name in self.keys:
            self.keys[key_name] = False
            self.win.bind(
                "<KeyPress-%s>" % key_name, lambda e: self._setPressed(key_name, True)
            )
            self.win.bind(
                "<KeyRelease-%s>" % key_name,
                lambda e: self._setPressed(key_name, False),
            )
        return self.keys[key_name]

    def _setPressed(self, key_name: str, pressed: bool):
        self.keys[key_name] = pressed

    def getWorldWidth(self) -> int:
        """
        Obtiene el ancho del mundo de juego.

        Returns:
            int: Ancho del mundo de juego.
        """
        return self.win.winfo_width()

    def getWorldHeight(self) -> int:
        """
        Obtiene la altura del mundo de juego.

        Returns:
            int: Altura del mundo de juego.
        """
        return self.win.winfo_height()


# ---


class GameObject:
    def __init__(
        self,
        x: int,
        y: int,
        imagePath: str = None,
        tipo: str = "undef",
        collisions: bool = False,
        layer: int = 1,
    ):
        """
        Constructor de la clase GameObject que inicializa un objeto en el mundo de juego.

        Args:
            x (int): Coordenada x inicial del objeto.
            y (int): Coordenada y inicial del objeto.
            imagePath (str): Ubicación de la imagen del objeto (por defecto None).
            tipo (str, optional): Tipo del objeto (por defecto es "undef").
            collisions (bool, optional): True si este objeto participara de las colisiones (por defecto es False)
            layer (int, optional): capa en que se colocara este objeto (por defecto es 1)
        """
        self.gw = GameWorld._getInstance()
        if self.gw is None:
            raise ("No existe una instancia de GameWorld activa!!!")
        self.canvas = self.gw._getCanvas()

        self.x = x
        self.y = y
        self.tipo = tipo
        self.collisions = collisions
        self.layer = layer

        if imagePath is None:
            self.shape = -1
            self.width = 0
            self.height = 0
        else:
            self.shape, self.width, self.height = self._createImage(imagePath)

        self.gw._addGObject(self)

    def _createImage(self, imagePath):
        img = self.loadImage(imagePath)
        shape = self.canvas.create_image(
            self.x,
            self.y,
            image=img,
            anchor=tk.CENTER,
            state="hidden",
            tags=("Layer " + str(self.layer),),
        )
        width = img.width()
        height = img.height()
        return shape, width, height

    def getX(self) -> int:
        """
        Obtiene la coordenada x actual del objeto.

        Returns:
            int: Coordenada x del objeto.
        """
        return self.x

    def getY(self) -> int:
        """
        Obtiene la coordenada y actual del objeto.

        Returns:
            int: Coordenada y del objeto.
        """
        return self.y

    def setPosition(self, x: int, y: int):
        """
        Establece la posición del objeto en el mundo de juego.

        Args:
            x (int): Nueva coordenada x del objeto.
            y (int): Nueva coordenada y del objeto.
        """
        x, y = int(x), int(y)
        if self.shape > 0:
            dx = x - self.x
            dy = y - self.y
            self.canvas.move(self.shape, dx, dy)
        self.x, self.y = x, y

    def setShape(self, imagePath: str):
        """
        Cambia la imagen del objeto

        Args:
            imagePath (str): Ubicación de la nueva imagen para el objeto
        """
        if self.shape > 0:
            img = self.loadImage(imagePath)
            self.width = img.width()
            self.height = img.height()
            self.canvas.itemconfig(self.shape, image=img)
        else:
            self.shape, self.width, self.height = self._createImage(imagePath)

    def getWidth(self) -> int:
        """
        Obtiene el ancho del objeto.

        Returns:
            int: Ancho del objeto.
        """
        return self.width

    def getHeight(self) -> int:
        """
        Obtiene la altura del objeto.

        Returns:
            int: Altura del objeto.
        """
        return self.height

    def getTipo(self) -> str:
        """
        Obtiene el tipo del objeto.
        Returns:
            str: Tipo del objeto.
        """
        return self.tipo

    def setCollisions(self, collisions: bool):
        """
        Habilita o deshabilita participar del procesamiento de colisiones

        Args:
            collisions (bool): True para habilitar, False para deshabilitar
        """
        self.collisions = collisions

    def destroy(self):
        """
        Elimina el objeto del mundo de juego.
        """
        if self.shape > 0:
            self.canvas.delete(self.shape)
        self.gw._delGObject(self)
        self.canvas = None
        self.gw = None

    def collidesWith(self, obj) -> bool:
        """
        Determina si este GameObject colisiona con otro

        Args:
            obj (GameObject): GameObject a detectar si colision con este

        Returns:
            bool: True si colisiona. False en caso contrario
        """
        return self.gw.collides(self, obj)

    def onUpdate(self, dt: float):
        """
        Llamado en cada actualización del juego para el objeto.

        Args:
            dt (float): Tiempo en segundos desde la ultima llamada.
        """
        pass

    def onCollision(self, dt: float, gobj):
        """
        Llamado cuando el objeto colisiona con otro objeto.

        Args:
            dt (float): Tiempo en segundos desde la ultima llamada.
            gobj (GameObject): Objeto con el que colisiona.
        """
        pass

    def getWorldWidth(self) -> int:
        """
        Obtiene el ancho del mundo de juego.

        Returns:
            int: Ancho del mundo de juego.
        """
        return self.gw.getWorldWidth()

    def getWorldHeight(self) -> int:
        """
        Obtiene la altura del mundo de juego.

        Returns:
            int: Altura del mundo de juego.
        """
        return self.gw.getWorldHeight()

    def isPressed(self, key_name: str) -> bool:
        """
        Verifica si una tecla específica está siendo presionada.

        Args:
            key_name (str): Nombre de la tecla a verificar.

        Returns:
            bool: True si la tecla está siendo presionada, False en caso contrario.
        """
        return self.gw.isPressed(key_name)

    def loadImage(self, imagePath: str) -> tk.PhotoImage:
        """
        Carga la imagen que se encuentra en la ruta especificada

        Args:
            imagePath (str): Ruta de la imagen a cargar.

        Returns:
            binary: La imagen a cargar.
        """
        return self.gw.loadImage(imagePath)

    def loadImages(self, imagesPaths: list) -> list:
        """
        Carga las imagenes referenciadas por el arreglo de paths

        Args:
            imagesPaths (list): Arreglo de imagenes cargadas
        """
        return self.gw.loadImages(imagesPaths)

    def setBgPic(self, bgPath: str):
        """
        Cambia la imagen de fondo

        Args:
            bgPath (str): Ruta de la imagen a utilizar como fondo
        """
        self.gw.setBgPic(bgPath)


# ---


class TextObject:
    _layer_ = "Layer Top"

    def __init__(
        self,
        x: int,
        y: int,
        text: str,
        font: str = "Arial",
        size: int = 10,
        bold: bool = False,
        italic: bool = False,
        color: str = "black",
    ):
        """
        Constructor de la clase TextObject que agrega un Texto al mundo del juego

        Args:
            x (int): Coordenada x del texto
            y (int): Coordenada y del texto
            text (str): Texto para este objeto
            font (str, optional): Font a utilizar para el texto (por defecto es "Arial").
            size (int, optional): Tamano a utilizar para el texto (por defecto es 10).
            bold (bool, optional): Especifica que el texto estara en bold (por defecto es False).
            italic (bool, optional): Especifica que el texto estara en italic (por defecto es False).
            color (str, optional): Color a utilizar para el texto (por defecto es "black").
        """
        self.gw = GameWorld._getInstance()
        if self.gw is None:
            raise ("No existe una instancia de GameWorld activa!!!")
        self.canvas = self.gw._getCanvas()

        self.text = self.canvas.create_text(
            0, 0, text=text, anchor=tk.NW, tags=(TextObject._layer_,)
        )
        self.setText(x, y, text, font, size, bold, italic, color)
        self.canvas.tag_raise(TextObject._layer_, "all")

    def setText(
        self,
        x: int = None,
        y: int = None,
        text: str = None,
        font: str = None,
        size: int = None,
        bold: bool = None,
        italic: bool = None,
        color: str = None,
    ):
        """
        Modifica el texto desplegado y sus atributos. Si no se especifican atributos se convservan los existentes

        Args:
            x (int, optional): Coordenada x del texto.
            y (int, optional): Coordenada y del texto
            text (str, optional): Texto para este objeto
            font (str, optional): Font a utilizar para el texto
            size (int, optional): Tamano a utilizar para el texto
            bold (bool, optional): Especifica que el texto estara en bold
            italic (bool, optional): Especifica que el texto estara en italic
            color (str, optional): Color a utilizar para el texto
        """
        # la posicion del texto
        _x, _y = self.canvas.coords(self.text)
        if x is None:
            x = _x
        if y is None:
            y = _y
        x, y = int(x), int(y)
        dx = x - _x
        dy = y - _y
        self.canvas.move(self.text, dx, dy)

        # los atributos
        kwargs = {}
        if not text is None:
            kwargs["text"] = text
        f = []
        if not font is None:
            f.append(font)
        if not size is None:
            f.append(size)
        t = ""
        if bold:
            t = t + " bold "
        if italic:
            t = t + " italic "
        if t:
            f.append(t)
        if f:
            kwargs["font"] = tuple(f)
        if not color is None:
            kwargs["fill"] = color
        self.canvas.itemconfig(self.text, kwargs)

    def destroy(self):
        """
        Elimina este texto del mundo del juego
        """
        self.canvas.delete(self.text)
        self.text = None
        self.canvas = None
        self.gw = None


# ---


class ObjectAnimator:
    def __init__(
        self, gobj: GameObject, imagesPath: str, speed: float = 0.100, repeat=True
    ):
        """_summary_

        Args:
            gobj (GameObject): _description_
            imagesPath (str): Ubicación de las imágenes para la animación (ej. "image-*.png").
            speed (float, optional): Velocidad de la animación en segundos (por defecto es 0.100).
            repeat (bool, optional): True si la animación se repite siempre (por defecto es True).
        """
        self.gobj = gobj
        self.speed = speed
        self.repeat = repeat
        self.idx = 0
        self.t = 0
        self.running = False

        self.imagesPath = sorted(glob.glob(imagesPath))
        gobj.loadImages(self.imagesPath)

    def setSpeed(self, speed: float):
        """
        Cambia la velocidad de la animación

        Args:
            speed (float): Velocidad de la animación en segundos
        """
        self.speed = speed

    def setRepeat(self, repeat: bool):
        """
        Cambia el atributo de repetición

        Args:
            repeat (bool): True si la animación se repite siempre
        """
        self.repeat = repeat

    def start(self):
        """
        Da inicio a la animación desde el primer frame
        """
        self.gobj.setShape(self.imagesPath[0])
        self.idx = 0
        self.t = time.perf_counter()
        self.running = True

    def stop(self):
        """
        Detiene la animación. La imagen que queda es la del último frame mostrado
        """
        self.idx = 0
        self.t = 0
        self.running = False

    def reset(self):
        """
        Resetea la animación dejándola detenida en el primer frame
        """
        self.gobj.setShape(self.imagesPath[0])
        self.idx = 0
        self.t = 0
        self.running = False

    def animate(self) -> bool:
        """
        Avanza al siguiente frame según la velocidad configurada

        Returns:
            bool: True si la animación continua. False en caso contrario
        """
        if not self.running:
            return False

        t = time.perf_counter()
        if t - self.t < self.speed:
            return False
        self.t = time.perf_counter()

        self.idx = self.idx + 1
        if self.idx >= len(self.imagesPath):
            if not self.repeat:
                self.stop()
                return False
            self.idx = 0
        self.gobj.setShape(self.imagesPath[self.idx])
        return True

        def destroy(self):
            """
            Destruye este animador de objetos
            """
            self.imagesPath = None
            self.gobj = None
