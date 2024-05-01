from PIL import Image
image = Image.open('лаба.png')
image.show()

res_img3 = image.reduce(3)
res_img3.save('resize_image.png')

left_image = image.transpose(Image.FLIP_LEFT_RIGHT)
left_image.save('left_image.png')

bottom_image = image.transpose(Image.FLIP_TOP_BOTTOM)
bottom_image.save('bottom_image.png')