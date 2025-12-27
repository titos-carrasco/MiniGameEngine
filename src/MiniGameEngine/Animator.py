import glob
import time
from MiniGameEngine.GameObject import GameObject


class Animator:
    """Clase que representa un secuenciador de imagenes."""

    def __init__(
        self, images_path: str, parent: GameObject, speed: float = 0.100, repeat=True
    ):
        """
        Crea un objeto de la clase Animator.

        Args:
            images_path (str): Archivos con la imágenes para la animación (ej. "image-*.png").
            parent(GameObject): El GameObject que modificará su shape
            speed (float, opcional): Velocidad de la animación en segundos (por defecto es 0.100).
            repeat (bool, opcional): True si la animación se repite siempre (por defecto es True).
        """
        assert (
            images_path
        ), "Animator(): images_path debe contener los nombres de los archivos de imágenes."
        assert speed > 0, "Animator(): speed debe ser mayor que 0."

        self._images_path = sorted(glob.glob(images_path))
        self.parent = parent
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

    def start(self):
        """
        Da inicio a la animación desde la primera imágen.
        """
        self._idx = 0
        self.parent.setShape(self._images_path[self._idx])
        self._t = time.perf_counter()
        self._running = True

    def stop(self):
        """Detiene la animación."""
        self._idx = 0
        self._t = 0
        self._running = False

    def next(self) -> bool:
        """
        Avanza al siguiente frame según la velocidad configurada.

        Returns:
            bool: True si aun está ejecutando. False en caso contrario
        """
        if not self._running:
            return False

        t = time.perf_counter()
        if t - self._t < self._speed:
            return True

        self._t = time.perf_counter()
        self._idx = self._idx + 1
        if self._idx >= len(self._images_path):
            if not self._repeat:
                self.stop()
                return False
            self._idx = 0

        self.parent.setShape(self._images_path[self._idx])
        return True
