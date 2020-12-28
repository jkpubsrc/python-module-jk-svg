


from jk_svg import *




def createCheckerboard(
	svg,
	width:float,
	height:float,
	tileWidth:float,
	tileHeight:float,
	cssColor1:str = "#303030",
	cssColor2:str = "#404040",
	):

	with svg.createRect() as rect:
		rect.x = 0
		rect.y = 0
		rect.width = width
		rect.height = height
		rect.style = "fill:" + cssColor2

	for iy in range(0, width, tileWidth):
		for ix in range(0, height, tileHeight):
			if ((ix // tileWidth + iy // tileHeight) % 2) == 0:
				with svg.createRect() as rect:
					rect.x = ix
					rect.y = iy
					rect.width = tileWidth
					rect.height = tileHeight
					rect.style = "fill:" + cssColor1
#







