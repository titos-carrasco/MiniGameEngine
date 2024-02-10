import sys
import time
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
    ):
        """
        Constructor de la clase GameWorld que inicializa una instancia del mundo de juego.

        Args:
            width (int): Ancho de la ventana del juego.
            height (int): Altura de la ventana del juego.
            title (str, optional): Título de la ventana del juego (por defecto es "MiniGameEngine").
            bgColor (str, optional): Color de fondo de la ventana del juego (por defecto es "gray").
            bgPath (str, optional): Ruta de la imagen de fondo de la ventana del juego (por defecto es None).
        """
        if GameWorld._instance_:
            return

        self.win = tk.Tk()
        self.win.geometry("%dx%d" % (width, height))
        self.win.title(title)
        self.win.resizable(False, False)

        self.canvas = tk.Canvas(self.win, width=width, height=height, bg=bgColor)
        self.canvas.place(x=0, y=0)

        self.images = {}

        self.bgPic = None
        self.setBgPic(bgPath)

        self.keys = {}
        self.gObjects = []
        self.tick_prev = 0
        self.fps = 0
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
            tk.PhotoImage: La imagen cargada.
        """
        if not imagePath in self.images:
            self.images[imagePath] = tk.PhotoImage(file=imagePath)
        return self.images[imagePath]

    def loadImages(self, imagesPaths: list[str]) -> list[tk.PhotoImage]:
        """
        Carga las imagenes referenciadas por el arreglo de rutas

        Args:
            imagesPaths (list[str]): Arreglo de rutas a las imagenes a cargar.

        Returns:
            list[tk.PhotoImage] : Arreglo con las imágenes cargadas.
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
        if not self.bgPic is None:
            self.canvas.delete(self.bgpic)
        img = self.loadImage(bgPath)
        self.bgPic = self.canvas.create_image(
            0, 0, image=img, anchor=tk.NW, tags=("Layer 0",)
        )
        self.canvas.tag_lower(self.bgPic, "all")

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
            self.gObjects.append(gobj)
            [
                self.canvas.tag_raise("Layer " + str(layer), "all")
                for layer in range(1, 100)
            ]

    def _doAddGameObjects(self):
        for o in self.gObjects:
            if o.__status__ == "new":
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
        gobjs1 = self.gObjects.copy()
        gobjs2 = gobjs1.copy()
        for o1 in gobjs1:
            gobjs2.pop(0)
            if o1.__status__ != "alive" or not o1._collisions:
                continue
            for o2 in gobjs2:
                if o2.__status__ != "alive" or not o2._collisions:
                    continue
                if o1.collides(o2):
                    o1.onCollision(dt, o2)
                    o2.onCollision(dt, o1)

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

    def getWidth(self) -> int:
        """
        Obtiene el ancho del mundo de juego.

        Returns:
            int: Ancho del mundo de juego.
        """
        return self.win.winfo_width()

    def getHeight(self) -> int:
        """
        Obtiene la altura del mundo de juego.

        Returns:
            int: Altura del mundo de juego.
        """
        return self.win.winfo_height()
