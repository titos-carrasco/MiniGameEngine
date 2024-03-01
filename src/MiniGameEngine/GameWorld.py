import sys
import time
import itertools
import ctypes
import tkinter as tk
import select
import socket

from MiniGameEngine.Camera import Camera


class GameWorld:
    """Clase que representa el mundo dentro del mini motor de juegos."""

    _instance_ = None

    @staticmethod
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
        world_size: (int, int) = None,
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
            world_size (int, int, optional): Tamaño del mundo del juego (por defecto similar al tamaño de la ventana)
        """
        if GameWorld._instance_:
            return

        self._gobjects = []
        self._images = {}
        self._keys = {}
        self._tick_prev = 0
        self._fps = 0
        self._fps_time = 0
        self._running = False
        self._delay = None
        self._sock = socket.socket()

        self._win = tk.Tk()
        self._win.geometry(f"{width}x{height}")
        self._win.title(title)
        self._win.resizable(False, False)
        self._screen_width = width
        self._screen_height = height
        if world_size:
            self._world_width = max(width, world_size[0])
            self._world_height = max(height, world_size[1])
        else:
            self._world_width = width
            self._world_height = height

        self._frame = tk.Frame(
            self._win,
            width=self._world_width,
            height=self._world_height,
            bg=bg_color,
            bd=0,
            highlightthickness=0,
        )
        self._frame.place(x=0, y=0)

        self._canvas = tk.Canvas(
            self._frame,
            width=self._world_width,
            height=self._world_height,
            bg=bg_color,
            bd=0,
            highlightthickness=0,
        )
        self._canvas.place(x=0, y=0)

        self._bg_pic = self._canvas.create_image(
            0, 0, image=None, anchor=tk.NW, state="hidden"
        )
        self.setBgPic(bg_path)

        if debug is not None:
            self._win.bind(f"<KeyRelease-{debug}>", self._doDebug)

        self._camera = Camera(
            0, 0, width, height, self._world_width, self._world_height
        )

        GameWorld._instance_ = self

    def gameLoop(self, fps: int, busy_wait: bool = False):
        """
        Inicia el loop principal del juego.

        Args:
            fps (int): Número de cuadros por segundo del juego.
            bw (bool): True para indicar que el sync de cada frame se hará con espera ocupada (por defecto es False)
        """
        self._win.protocol("WM_DELETE_WINDOW", self.exitGame)
        self._fps = fps
        self._fps_time = 1 / self._fps
        self._delay = self._mkDelay(busy_wait)
        self._tick_prev = time.perf_counter()
        self._running = True
        while self._running:
            # elimina los game objects destruidos
            gobjs = [o for o in self._gobjects if o.__status__ == "dead"]
            if gobjs:
                _ = [self._gobjects.remove(o) for o in gobjs]
                _ = [self._camera._delGameObject(o) for o in gobjs]

            # incorpora los game objects agregados
            gobjs = [
                setattr(o, "__status__", "alive")
                for o in self._gobjects
                if o.__status__ == "new"
            ]
            if gobjs:
                _ = [
                    self._canvas.tag_raise(f"Layer {layer:04d}", "all")
                    for layer in {o._layer for o in self._gobjects}
                ]

            # mueve la cámara segun su target
            cx, cy = self._camera._followTarget()
            self._frame.place(x=-cx, y=-cy)

            # actualiza el despliegue
            self._win.update()

            # se sincroniza a 1/fps
            dt = self._tick()

            # onUpdate para la app
            self.onUpdate(dt)

            # onUpdate para los game objects
            gobjs = [o for o in self._gobjects if o.__status__ == "alive"]
            _ = [o.onUpdate(dt) for o in gobjs]

            # onCollision para los game objects
            gobjs = [
                o for o in self._gobjects if o.__status__ == "alive" and o._can_collide
            ]
            _ = [
                (o1.onCollision(dt, o2), o2.onCollision(dt, o1))
                for o1, o2 in itertools.combinations(gobjs, 2)
                if o1.collides(o2)
            ]

        self._win.destroy()
        del self._win
        del self._gobjects
        del self._canvas
        del self._images
        del self._keys
        del GameWorld._instance_

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
        return self._world_width

    def getHeight(self) -> int:
        """
        Obtiene la altura del mundo de juego.

        Returns:
            int: Altura del mundo de juego.
        """
        return self._world_height

    def getCamera(self) -> Camera:
        """Obtiene la cámara del mundo del juego

        Returns:
            Camera: La cámara utilizada en el mundo del juego
        """
        return self._camera

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
        if not hasattr(gobj, "__status__"):
            gobj.__status__ = "new"
            self._gobjects.append(gobj)

    def _delGObject(self, gobj):
        if hasattr(gobj, "__status__"):
            gobj.__status__ = "dead"

    def _tick(self):
        t = self._fps_time + self._tick_prev
        while t - time.perf_counter() > 0:
            self._delay()
        now = time.perf_counter()
        dt = now - self._tick_prev
        self._tick_prev = now
        return dt

    if sys.platform == "win32":

        def _mkDelay(self, busy_wait: bool):
            if busy_wait:
                return lambda: 0
            return lambda: [
                ctypes.windll.winmm.timeBeginPeriod(1),
                select.select([self._sock], [], [], 0.0001),
                ctypes.windll.winmm.timeEndPeriod(1),
            ]

    else:

        def _mkDelay(self, busy_wait: bool):
            if busy_wait:
                return lambda: 0
            return lambda: select.select([], [], [], 0.0001)

    def _getCanvas(self) -> tk.Canvas:
        return self._canvas

    def _doDebug(self, _evt):
        items = self._canvas.find_all()
        print("Canvas items:", items)
        gobjs = sorted([(o._layer, o._element, o._tipo) for o in self._gobjects])
        print("gObjects:", gobjs)
