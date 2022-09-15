from PIL import Image
from PIL import ImageEnhance

#To open the image
image = Image.open("C:\\Users\\gokul\\PycharmProjects\DIP\\tuberculosis.jpg")

#To show the image
image.show()

#Enhance sharpness
curvedImage = ImageEnhance.Contrast(image)
NewSharp = 8.3

#Sharpness enhanced by a factor of 8.3
SharpedImage = curvedImage.enhance(NewSharp)

SharpedImage.show()