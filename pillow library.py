
from PIL import Image,ImageOps,ImageDraw

img = Image.open('farzin.JPG')
img = ImageOps.grayscale(img)
img = ImageOps.equalize(img)
dicew = 20

dicesize =int (img.width * 1.0/dicew)
diceh = int(img.height * 1.0/img.width * dicew)
print(img.width,img.height,dicew,diceh,dicesize)

nim = Image.new("L",(img.width,img.height),'white')
nimd = ImageDraw.Draw(nim)

for y in range (0,img.height- dicesize,dicesize):
    for x in range (0,img.width - dicesize,dicesize):
        thisSectorColor = 0
        for dicex in range(0,dicesize):
            for dicey in range(0,dicesize):
                thisColor = img.getpixel((x+dicex,y+dicey))
                thisSectorColor += thisColor
        thisSectorColor/=(dicesize**2)
        nimd.rectangle([(x,y),(x+dicesize,y+dicesize)],int(115))

nim.show()
