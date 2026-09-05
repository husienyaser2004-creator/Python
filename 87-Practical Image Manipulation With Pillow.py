#---------------------------------------------
#--Practical Image Manipulation With Pillow---
#---------------------------------------------

from PIL import Image

# Open The Image
myImage = Image.open(r"D:/Python/Files/play.jpg")

# Show The Image
myImage.show()

# My Cropped Image
myBox = (0, 0, 400, 400)
myNewImage = myImage.crop(myBox)

# Show The New Image 
myNewImage.show()

# My Converted Mode Image
myConverted = myImage.convert("L")
myConverted.show() 
