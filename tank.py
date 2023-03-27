from PIL import Image, ImageDraw, ImageFont 




image = Image.open('/Volumes/Education/programming Files/watertank/img1.jpeg')
draw = ImageDraw.Draw(image)
font1 = ImageFont.truetype ("/Volumes/Education/programming Files/watertank/edosz.otf" ,30)




points= 450,530
string='8 mm bars @ 200 mm c/c'
draw.text(points,string,'blue',font=font1)

points= 400,380
string='12 mm bars @ 100 mm c/c'
draw.text(points,string,'blue',font=font1) 



points= 400,300
string='8 mm bars @150 mm c/c'
draw.text(points,string,'blue',font=font1) 


image.show()