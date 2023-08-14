#text or a link to QR code using Pytho - pip install qrcode Image
#install all libraries needed
#create a functionthat collects text and converts it to a QR code
#save QR code as an image
#run the function directly
import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(  # type: ignore
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,  # type: ignore
        box_size = 10,
        border = 4
    )
    qr.add_data(text)
    qr.make(fit = True)
    #make the image of the QR code and everything

    img = qr.make_image(fill_color = "black", back_color = "white") #change the colors if you want to lol
    img.save("qrimg.jpg")
url = input("Enter the URL you want to get a QR code out of: ")
generate_qrcode(url) #image gets saved in our root directory, if you scan code, it shows you this URL
    