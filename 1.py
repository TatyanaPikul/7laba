from PIL import Image
image = Image.open('лаба.png')
image.show()

import os
file = os.stat('лаба.png')
file_size = file.st_size
print('Размер файла:', file_size, 'байт')
print("Формат фото: ", image.format)
print("Цветовая модель: ", image.mode)