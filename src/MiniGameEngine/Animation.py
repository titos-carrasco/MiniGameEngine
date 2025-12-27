from MiniGameEngine.Sprite import Sprite
from MiniGameEngine.Animator import Animator


class Animation(Sprite):
    """Clase que representa una animación"""

    def __init__(
        self, x: int, y: int, images_path: str, speed: float = 0.6, repeat: bool = False
    ):
        """
        Crea un objeto de la clase Animation.
        Se autodestruye cuando la animacion finaliza

        Args:
            x (int): Coordenada x de este objeto
            y (int): Coordenada y de este objeto
            images_path (str): Archivos con la imágenes para la animación (ej. "image-*.png").
            speed (float, opcional): Velocidad de la animación en segundos (por defecto es 0.100).
            repeat (bool, opcional): True si la animación se repite siempre (por defecto es False).
        """
        super().__init__(x, y, layer=1, tipo="Animation")

        self.animator = Animator(images_path, self, speed=speed, repeat=repeat)
        self.animator.start()

    def onUpdate(self, dt, dt_optimal):
        if not self.animator.next():
            self.delete()
