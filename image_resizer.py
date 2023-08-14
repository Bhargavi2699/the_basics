#install pillow and then import it
#open up image to be resized
#print the current size of that image
#specify the size we finally want it in
#save the new resized image

from PIL import Image

def resize_image(size1, size2): #parameters have the dimensions
    image = Image.open('face_detected.jpg')
    print(f"Current size : {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save('face_detected_' + str(size1) + '.jpeg')


size1 = int(input("Enter length:"))
size2 = int(input("Enter width:"))
resize_image(size1, size2)