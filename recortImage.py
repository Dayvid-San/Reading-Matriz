from PIL import Image 

adressImage = 'img/baixados.jfif'
#adressImage = str(input("Qual o caminho da imagem?"))
Image1 = Image.open(adressImage) 
left, up, rigth, bottom = (130, 120, 200, 200)

croppedIm = Image1.crop((left, up, rigth, bottom)) 
croppedIm.show() 
