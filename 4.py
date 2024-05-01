from PIL import Image
image = Image.open('лаба.png')
image2 = Image.open('водяной знак.png')

image.paste(image2, (480, 960), image2)
image.show()

