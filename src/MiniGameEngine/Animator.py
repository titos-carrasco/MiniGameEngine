import glob
import time


class Animator:
    """Clase que representa un secuenciador de imagenes."""

    def __init__(self, images_path: str, speed: float = 0.100, repeat=True):
        """
        Crea un objeto de la clase Animator.

        Args:
            images_path (str): Archivos con la imágenes para la animación (ej. "image-*.png").
            speed (float, opcional): Velocidad de la animación en segundos (por defecto es 0.100).
            repeat (bool, opcional): True si la animación se repite siempre (por defecto es True).
        """
        assert (
            images_path
        ), "Animator(): images_path debe contener los nombres de los archivos de imágenes."
        assert speed > 0, "Animator(): speed debe ser mayor que 0."

        self._images_path = sorted(glob.glob(images_path))
        self._speed = speed
        self._repeat = repeat
        self._idx = 0
        self._t = 0
        self._running = False

    def setSpeed(self, speed: float):
        """
        Cambia la velocidad de la animación.

        Args:
            speed (float): Velocidad de la animación en segundos.
        """
        assert speed > 0, "Animator.setSpeed(): speed debe ser mayor que 0."
        self._speed = speed

    def setRepeat(self, repeat: bool):
        """
        Cambia el atributo de repetición.

        Args:
            repeat (bool): True si la animación se repite siempre.
        """
        self._repeat = repeat

    def start(self) -> str:
        """
        Da inicio a la animación desde la primera imágen.

        Returns:
            str: Ruta con la imagen del primer cuadro.
        """
        self._idx = 0
        self._t = time.perf_counter()
        self._running = True
        return self._images_path[0]

    def stop(self):
        """Detiene la animación."""
        self._idx = 0
        self._t = 0
        self._running = False

    def next(self) -> str:
        """
        Avanza al siguiente frame según la velocidad configurada.

        Returns:
            str: Ruta con la imagen si es que se avanzó al siguiente cuadro. None en caso contrario.
        """
        if not self._running:
            return self.start()

        t = time.perf_counter()
        if t - self._t < self._speed:
            return None
        self._t = time.perf_counter()

        self._idx = self._idx + 1
        if self._idx >= len(self._images_path):
            if not self._repeat:
                self.stop()
                return None
            self._idx = 0

        return self._images_path[self._idx]

    def isRunning(self) -> bool:
        """
        Determina si el Animator se encuentra en ejecución.

        Returns:
            bool: True si está ejecutando. False en caso contrario.
        """
        return self._running

    def getPaths(self) -> []:
        """
        Retorna la lista de nombres de archivos de imágenes de este animador.

        Returns:
            []: La lista de nombres de archivos
        """
        return self._images_path
