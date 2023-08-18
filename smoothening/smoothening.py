from PIL import Image, ImageFilter

# Image SOOMTHENING     -   Using ImageFilter.SMOOTH

img = Image.open('smoothening/elephant_rock.jpg')
smoothened_img = img.filter(ImageFilter.SMOOTH)
smoothened_img.save('smoothening/soomth.jpg')



# Image SOOMTHENING     -   Using ImageFilter.SMOOTH_MORE

img = Image.open('smoothening/elephant_rock.jpg')
smoothened_img = img.filter(ImageFilter.SMOOTH_MORE)
smoothened_img.save('smoothening/soomthmoore.jpg')




# Image SOOMTHENING     -   Using Custom kernel filter

img = Image.open('smoothening/elephant_rock.jpg')

kernel = [2, 4, 2,
          4, 8, 4,
          2, 4, 2]

#  Note:
#           ImageFilter.Kernel(<matrix_size>, <matrix_values>, <calculated_value_divsor>, 
#                               <value_added_after_division>)

kernel_filter = ImageFilter.Kernel((3,3), kernel, scale=32, offset=0)

smoothened_img = img.filter(kernel_filter)
smoothened_img.save('smoothening/kernel_soomthened.jpg')