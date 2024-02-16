import sys
import time
import itertools
import ctypes
import tkinter as tk


class GameWorld:
    """Clase que representa el mundo dentro del mini motor de juegos."""

    _instance_ = None

    def _getInstance():
        return GameWorld._instance_

    # ---

    def __init__(
        self,
        width: int,
        height: int,
        title: str = "MiniGameEngine",
        bg_color: str = "gray",
        bg_path: str = None,
        debug=None,
    ):
        """
        Crea un objeto de la clase GameWorld.

        Args:
            width (int): Ancho de la ventana del juego.
            height (int): Altura de la ventana del juego.
            title (str, optional): Título de la ventana del juego (por defecto es "MiniGameEngine").
            bg_color (str, optional): Color de fondo de la ventana del juego (por defecto es "gray").
            bg_path (str, optional): Ruta de la imagen de fondo de la ventana del juego (por defecto es None).
            debug (str, optional): La tecla a utilizar para mostrar los detalles del mini motor de juego (por defecto es None)
        """
        if GameWorld._instance_:
            return

        self._win = tk.Tk()
        self._win.geometry(f"{width}x{height}")
        self._win.title(title)
        self._win.resizable(False, False)

        self._canvas = tk.Canvas(
            self._win,
            width=width,
            height=height,
            bg=bg_color,
            bd=0,
            state="disabled",
        )
        self._canvas.place(x=0, y=0)
        self._canvas.update()

        self._images = {}

        self._bg_pic = self._canvas.create_image(
            0, 0, image=None, anchor=tk.NW, state="hidden"
        )
        self.setBgPic(bg_path)

        if debug is not None:
            self._win.bind(f"<KeyRelease-{debug}>", self._doDebug)

        self._keys = {}
        self._gobjects = []
        self._tick_prev = 0
        self._fps = 0
        self._fps_time = 0
        self._running = False
        GameWorld._instance_ = self

    def gameLoop(self, fps: int):
        """
        Inicia el loop principal del juego.

        Args:
            fps (int): Número de cuadros por segundo del juego.
        """
        self._win.protocol("WM_DELETE_WINDOW", self.exitGame)
        self._fps = fps
        self._fps_time = 1 / self._fps
        self._tick_prev = time.perf_counter()
        self._running = True
        while self._running:
            # se sincroniza a 1/fps
            dt = self._tick()

            # elimina los game objects destruidos
            gobjs = [o for o in self._gobjects if o.__status__ == "dead"]
            [self._gobjects.remove(o) for o in gobjs]

            # incorpora los game objects agregados
            [
                (o._layer, setattr(o, "__status__", "alive"))
                for o in self._gobjects
                if o.__status__ == "new"
            ]

            # onUpdate para la app
            self.onUpdate(dt)

            # onUpdate para los game objects
            gobjs = [o for o in self._gobjects if o.__status__ == "alive"]
            [o.onUpdate(dt) for o in gobjs]

            # onCollision para los game objects
            gobjs = [
                o for o in self._gobjects if o.__status__ == "alive" and o._can_collide
            ]
            [
                (o1.onCollision(dt, o2), o2.onCollision(dt, o1))
                for o1, o2 in itertools.combinations(gobjs, 2)
                if o1.collides(o2)
            ]

            # actualiza el despliegue
            self._win.update_idletasks()
            self._win.update()

        self._win.destroy()

        self._gobjects = None
        self._keys = None
        self._bg_pic = None
        self._images = None
        self._canvas = None
        self._win = None
        self._instance_ = None
        GameWorld._instance_ = None

    def onUpdate(self, dt: float):
        """
        Llamada por cada ciclo dentro del loop (fps veces por segundo).

        Args:
            dt (float): Tiempo en segundos desde la última llamada.
        """

    def exitGame(self):
        """Finaliza el loop principal del juego."""
        self._running = False

    def setBgPic(self, bg_path: str):
        """
        Cambia la imagen de fondo.

        Args:
            bg_path (str): Archivo con la imagen a establecer como fondo.
        """

        if bg_path is None:
            self._getCanvas().itemconfig(self._bg_pic, image=None, state="hidden")
        else:
            img = self.loadImage(bg_path)
            self._getCanvas().itemconfig(self._bg_pic, image=img, state="normal")
        self._canvas.tag_lower(self._bg_pic, "all")

    def isPressed(self, key_name: str) -> bool:
        """
        Verifica si una tecla específica está siendo presionada.

        Args:
            key_name (str): Nombre de la tecla a verificar.

        Returns:
            bool: True si la tecla está presionada, False en caso contrario.
        """
        if not key_name in self._keys:
            self._keys[key_name] = False
            self._win.bind(
                f"<KeyPress-{key_name}>", lambda e: self._setPressed(key_name, True)
            )
            self._win.bind(
                f"<KeyRelease-{key_name}>", lambda e: self._setPressed(key_name, False)
            )
        return self._keys[key_name]

    def _setPressed(self, key_name: str, pressed):
        self._keys[key_name] = pressed

    def getWidth(self) -> int:
        """
        Obtiene el ancho del mundo de juego.

        Returns:
            int: Ancho del mundo de juego.
        """
        return self._win.winfo_width()

    def getHeight(self) -> int:
        """
        Obtiene la altura del mundo de juego.

        Returns:
            int: Altura del mundo de juego.
        """
        return self._win.winfo_height()

    def loadImage(self, image_path: str) -> tk.PhotoImage:
        """
        Carga la imagen que se encuentra en la ruta especificada.

        Args:
            imagePath (str): Ruta de la imagen a cargar.

        Returns:
            tk.PhotoImage: La imagen cargada.
        """
        if not image_path in self._images:
            self._images[image_path] = tk.PhotoImage(file=image_path)
        return self._images[image_path]

    def loadImages(self, images_paths: list) -> list:
        """
        Carga las imagenes referenciadas por el arreglo de rutas.

        Args:
            images_paths (list[str]): Arreglo de rutas a las imagenes a cargar.

        Returns:
            list[tk.PhotoImage] : Arreglo con las imágenes cargadas.
        """
        return [self.loadImage(path) for path in images_paths]

    # ---

    def _addGObject(self, gobj):
        if hasattr(gobj, "__status__"):
            return
        gobj.__status__ = "new"
        self._gobjects.append(gobj)

        layers = sorted(set([o._layer for o in self._gobjects]))
        [
            (layer, self._canvas.tag_raise("Layer " + str(layer), "all"))
            for layer in layers
        ]

    def _delGObject(self, gobj):
        if hasattr(gobj, "__status__"):
            gobj.__status__ = "dead"

    if sys.platform == "win32":

        def _tick(self):
            ctypes.windll.winmm.timeBeginPeriod(1)
            while time.perf_counter() - self._tick_prev < self._fps_time:
                time.sleep(0.0001)
            ctypes.windll.winmm.timeEndPeriod(1)
            now = time.perf_counter()
            dt = now - self._tick_prev
            self._tick_prev = now
            return dt

    else:

        def _tick(self):
            while time.perf_counter() - self._tick_prev < self._fps_time:
                time.sleep(0.0001)
            now = time.perf_counter()
            dt = now - self._tick_prev
            self._tick_prev = now
            return dt

    def _getCanvas(self) -> tk.Canvas:
        return self._canvas

    def _doDebug(self, evt):
        items = self._canvas.find_all()
        print("Canvas items:", items)
        gobjs = sorted([(o._layer, o._element, o._tipo) for o in self._gobjects])
        print("gObjects:", gobjs)
