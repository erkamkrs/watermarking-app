#Importing Libraries
from PIL import Image, ImageDraw, ImageFont


#Opening Image & Creating New Text Layer
image_name = "YOUR IMAGE"
image = Image.open(image_name).convert("RGBA")
text_layer = Image.new('RGBA', image.size, (255,255,255,0))

#Creating Text
text = "Sample Watermark"
font = ImageFont.truetype("arial.ttf", 40)

#Creating Draw Object
draw = ImageDraw.Draw(text_layer)

#Positioning Text
width, height = image.size
x=height/2 + 50
y=width/2
draw.textbbox(xy=(x,y), text="Sample Watermark", font=None, anchor=None, spacing=4, align='left')

#Applying Text
draw.text((x,y), text, fill=(255,255,255, 125), font=font)

#Combining Original Image with Text and Saving
watermarked = Image.alpha_composite(image, text_layer)
watermarked.show()
watermarked.save(r"watermarked-image.png")
