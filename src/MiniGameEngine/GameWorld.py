import sys
import time
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
    ):
        """
        Crea un objeto de la clase GameWorld.

        Args:
            width (int): Ancho de la ventana del juego.
            height (int): Altura de la ventana del juego.
            title (str, optional): Título de la ventana del juego (por defecto es "MiniGameEngine").
            bg_color (str, optional): Color de fondo de la ventana del juego (por defecto es "gray").
            bg_path (str, optional): Ruta de la imagen de fondo de la ventana del juego (por defecto es None).
        """
        if GameWorld._instance_:
            return

        self._win = tk.Tk()
        self._win.geometry(f"{width}x{height}")
        self._win.title(title)
        self._win.resizable(False, False)

        self._canvas = tk.Canvas(
            self._win, width=width, height=height, bg=bg_color, bd=0
        )
        self._canvas.place(x=0, y=0)
        # self._canvas.pack()

        self._images = {}

        self._bg_pic = None
        self.setBgPic(bg_path)

        self._keys = {}
        self._gobjects = []
        self._layers = {}
        self._tick_prev = 0
        self._fps = 0
        self._fps_time = 0
        self._running = False
        GameWorld._instance_ = self

    def _getCanvas(self) -> tk.Canvas:
        return self._canvas

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

    def loadImages(self, images_paths: list[str]) -> list[tk.PhotoImage]:
        """
        Carga las imagenes referenciadas por el arreglo de rutas.

        Args:
            images_paths (list[str]): Arreglo de rutas a las imagenes a cargar.

        Returns:
            list[tk.PhotoImage] : Arreglo con las imágenes cargadas.
        """
        images = []
        for path in images_paths:
            images.append(self.loadImage(path))
        return images

    def setBgPic(self, bg_path: str):
        """
                Cambia la imagen de fondo.
        protectedlizar como fondo.
        """
        if not self._bg_pic is None:
            self._canvas.delete(self._bg_pic)
        img = self.loadImage(bg_path)
        self._bg_pic = self._canvas.create_image(
            0, 0, image=img, anchor=tk.NW, state="hidden", tags=("Layer 0",)
        )
        self._canvas.tag_lower(self._bg_pic, "all")

    def gameLoop(self, fps: int):
        """
        Inicia el loop principal del juego.

        Args:
            fps (int): Número de cuadros por segundo del juego.
        """
        self._fps = fps
        self._fps_time = 1 / self._fps
        self._tick_prev = time.perf_counter()

        self._running = True
        self._win.protocol("WM_DELETE_WINDOW", self.exitGame)
        while self._running:
            self._doAddGameObjects()
            dt = self._doRefresh()
            self.onUpdate(dt)
            self._doUpdateGameObjects(dt)
            self._doCheckCollisions(dt)
            self._doDelGameObjects()
        self._win.destroy()

        self._layers = None
        self._gobjects = None
        self._keys = None
        self._bg_pic = None
        self._images = None
        self._canvas = None
        self._win = None
        self._instance_ = None
        GameWorld._instance_ = None

    def exitGame(self):
        """Finaliza el loop principal del juego."""
        self._running = False

    def onUpdate(self, dt: float):
        """
        Llamada por cada ciclo dentro del loop (fps veces por segundo).

        Args:
            dt (float): Tiempo en segundos desde la última llamada.
        """

    def _addGObject(self, gobj):
        if not hasattr(gobj, "__status__"):
            gobj.__status__ = "new"
            self._gobjects.append(gobj)
            layer = gobj.getLayer()
            if not layer in self._layers:
                self._layers[layer] = 0
            self._layers[layer] += 1

    def _doAddGameObjects(self):
        update_layers = False
        for o in self._gobjects:
            if o.__status__ == "new":
                o.__status__ = "alive"
                update_layers = True

        if update_layers:
            for layer in sorted(self._layers.keys()):
                self._canvas.tag_raise("Layer " + str(layer), "all")

    def _delGObject(self, gobj):
        if hasattr(gobj, "__status__"):
            gobj.__status__ = "dead"
            layer = gobj.getLayer()
            self._layers[layer] -= 1
            if self._layers[layer] == 0:
                del self._layers[layer]

    def _doDelGameObjects(self):
        gobjs = [o for o in self._gobjects if o.__status__ == "dead"]
        [self._gobjects.remove(o) for o in gobjs]

    def _doUpdateGameObjects(self, dt):
        gobjs = [o for o in self._gobjects if o.__status__ == "alive"]
        [o.onUpdate(dt) for o in gobjs]

    def _doCheckCollisions(self, dt):
        gobjs1 = [
            o for o in self._gobjects if o.__status__ == "alive" and o._can_collide
        ]
        gobjs2 = gobjs1.copy()
        for o1 in gobjs1:
            gobjs2.pop(0)
            for o2 in gobjs2:
                if o1.collides(o2):
                    o1.onCollision(dt, o2)
                    o2.onCollision(dt, o1)

    def _doRefresh(self):
        [
            self._canvas.itemconfig(item, state="normal")
            for item in self._canvas.find_all()
        ]
        # self._win.update_idletasks()
        self._win.update()
        [
            self._canvas.itemconfig(item, state="hidden")
            for item in self._canvas.find_all()
        ]

        now = self._tick()
        dt = now - self._tick_prev
        self._tick_prev = now

        return dt

    if sys.platform == "win32":

        def _tick(self):
            ctypes.windll.winmm.timeBeginPeriod(1)
            while time.perf_counter() - self._tick_prev < self._fps_time:
                time.sleep(0.0001)
            ctypes.windll.winmm.timeEndPeriod(1)
            return time.perf_counter()

    else:

        def _tick(self):
            while time.perf_counter() - self._tick_prev < self._fps_time:
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
        if not key_name in self._keys:
            self._keys[key_name] = False
            self._win.bind(
                f"<KeyPress-{key_name}>", lambda e: self._setPressed(key_name, True)
            )
            self._win.bind(
                f"<KeyRelease-{key_name}>",
                lambda e: self._setPressed(key_name, False),
            )
        return self._keys[key_name]

    def _setPressed(self, key_name: str, pressed: bool):
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
