try:
	from PIL import Image, ImageDraw, ImageFont, ImageEnhance
except ImportError:
	print("please import pillow")
""" Barrowed function from a website eyesopen.com """
def add_logo(mfname, lfname):
	# resize logo
	wsize = int(min(mfname.size[0], mfname.size[1]) * 0.25)
	wpercent = (wsize / float(lfname.size[0]))
	hsize = int((float(mfname.size[1]) * float(wpercent)))
    
    # I think this part of code getting value of box. 
	simage = lfname.resize((wsize, hsize))
	mbox = mfname.getbbox()
	sbox = simage.getbbox()

	# right bottom corner
	box = (mbox[2] - sbox[2], mbox[3] - sbox[3])
	mfname.paste(simage,box)

# open the images.
image = Image.open("image.jpg")
logo = Image.open("kani_croped.jpeg")

# get width and height of the first image. 
width, height = image.size
d = ImageDraw.Draw(image)
text = "Kani Center"

# add a font to for the text.
font = ImageFont.truetype("/usr/share/fonts/truetype/defavu/DejaVuSansMono.ttf", 12, encoding="unic")
textwidth, textheight = d.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 350
x = width - textwidth - margin
y = height - textheight - margin

enhancer = ImageEnhance.Brightness(logo)
logo = enhancer.enhance(0.4)
# draw watermark in the bottom right corner
d.text((x,y), text, font=font, fill=(255,255,255,128))
add_logo(image, logo)

image.show()
