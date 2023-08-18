from PIL import Image


# GRAY-SCALING Image

img_rgb = Image.open('gray-scaling/elephant_rock.jpg')
# print(img_rgb.__dict__)
# print(img_rgb.format)
img_gray = img_rgb.convert('L')
img_gray.save('gray-scaling/elephant_rock_gray.jpg')
