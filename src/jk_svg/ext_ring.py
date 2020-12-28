
#
# This extension has been inspired by:
# https://stackoverflow.com/questions/22579508/subtract-one-circle-from-another-in-svg
#




from jk_svg import *





def createRing(
	svg,
	cx:float,
	cy:float,
	rOuter:float,
	rInner:float,
	cssColor:str = "orange",
	):

	assert rOuter >= rInner

	maskID = svg.generateUniqueID("hole")

	with svg.createMask() as mask:
		mask.id = maskID

		with mask.createRect() as rect:
			rect.width = "100%"
			rect.height = "100%"
			rect.style = "fill:white"

		with mask.createCircle() as circle:
			circle.r = rInner
			circle.cx = cx
			circle.cy = cy
			circle.style = "fill:black"

	with svg.createCircle() as circle:
		circle.r = rOuter
		circle.cx = cx
		circle.cy = cy
		circle.mask = maskID
		circle.style = "fill:" + cssColor
#







