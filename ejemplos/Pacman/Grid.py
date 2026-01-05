from PIL import Image
import numpy as np
import math

CELL = 16

# Cargar imagen
#img = Image.open("./Recursos/Grid 16x16.png").convert("L")  # escala de grises
img = Image.open("./Recursos/Dots.png").convert("L")  # escala de grises
data = np.array(img)

height, width = data.shape

rows = math.ceil(height / CELL)
cols = math.ceil(width / CELL)

matrix = np.zeros((rows, cols), dtype=int)

for r in range(rows):
    for c in range(cols):
        y0 = r * CELL
        y1 = min((r + 1) * CELL, height)
        x0 = c * CELL
        x1 = min((c + 1) * CELL, width)

        block = data[y0:y1, x0:x1]

        # Si hay algún píxel distinto de negro
        if np.any(block > 0):
            matrix[r, c] = 1

np.set_printoptions(threshold=np.inf)
print(matrix)
