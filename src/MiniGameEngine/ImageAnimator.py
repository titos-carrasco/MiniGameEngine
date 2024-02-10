import glob
import time


class ImageAnimator:
    """
    Clase que representa un secuenciador de imagenes
    """

    def __init__(self, imagesPath: str, speed: float = 0.100, repeat=True):
        """
        Constructor de la clase ImageAnimator

        Args:
            imagesPath (str): Archivos con la imágenes para la animación (ej. "image-*.png").
            speed (float, optional): Velocidad de la animación en segundos (por defecto es 0.100).
            repeat (bool, optional): True si la animación se repite siempre (por defecto es True).
        """
        self.imagesPath = sorted(glob.glob(imagesPath))
        self.speed = speed
        self.repeat = repeat
        self.idx = 0
        self.t = 0
        self.running = False

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
        Da inicio a la animación desde la primera imágen
        """
        self.idx = 0
        self.t = time.perf_counter()
        self.running = True

    def stop(self):
        """
        Detiene la animación.
        """
        self.idx = 0
        self.t = 0
        self.running = False

    def next(self) -> str:
        """
        Avanza al siguiente frame según la velocidad configurada

        Returns:
            str: Archivo con la imagen si es que se avanzó al siguiente cuadro. None en caso contrario
        """
        if not self.running:
            return None

        t = time.perf_counter()
        if t - self.t < self.speed:
            return None
        self.t = time.perf_counter()

        self.idx = self.idx + 1
        if self.idx >= len(self.imagesPath):
            if not self.repeat:
                self.stop()
                return None
            self.idx = 0

        return self.imagesPath[self.idx]
