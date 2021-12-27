from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

#fonts
font = ImageFont.truetype("verdana.ttf", 34)
font_bold=ImageFont.truetype("Verdana Bold.ttf",34)
font_slash =ImageFont.truetype("verdana.ttf",50)

#IEEE icon and background white
img_background = Image.open('IEEE.png')
img_icon=Image.open('IEEE-icon.png')

#adding two images to a single one and positioning the icon
background_image=img_background.copy()
background_image.paste(img_icon,(150,170))

draw = ImageDraw.Draw(background_image)

#Font area
# draw.text((212, 175),"I E E E",fill="RGB(0,103,154)",font=font,stroke_width=2,stroke_fill="RGB(0,103,154)")
draw.text((212,175),"IEEE",fill="RGB(0,103,154)",font=font_bold)
draw.text((325,165),"|" ,fill="RGB(0,103,154)",font=font_slash)
draw.text((350,175),"SB GCEK",fill="RGB(0,103,154)",font=font)

#creating the required image
background_image.save('IEEEnew.png')
