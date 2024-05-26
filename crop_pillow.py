
#pillow
from PIL import Image


name = []
name.append("스크린샷")
name.append("(")
name.append(").png")



def crop(n):
    filename = name[0]+name[1]+str(n)+name[2]    
    image = Image.open("target/"+filename)
    print(image.size)
    image = image.crop((10,110,950, 1000))
    image.save("rsult/"+filename)



for i in range(3087,3348+1):
    crop(i)
    #print(i)

