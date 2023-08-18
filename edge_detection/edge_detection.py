from PIL import Image, ImageFilter


# Edge Detection    -   Using FIND_EDGES

img = Image.open('edge_detection/hand.jpg')

img_gray = img.convert('L')

edge_img = img_gray.filter(ImageFilter.FIND_EDGES)
edge_img.save('edge_detection/edge_detect.jpg')





# Edge Detection    -   Using Kernel

img = Image.open('edge_detection/hand.jpg')

img_gray = img.convert('L')
kernel = [-1, -1, -1,
          -1, 8, -1,
          -1, -1, -1]

edge_img = img_gray.filter(ImageFilter.Kernel((3,3), kernel, 1, 0))
edge_img.save('edge_detection/kernel_edge_detect.jpg')