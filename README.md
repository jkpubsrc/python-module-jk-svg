jk_svg
==========

Introduction
------------

This python module implements a set of classes for easy programmatic create of SVG graphics.

Information about this module can be found here:

* [github.com](https://github.com/jkpubsrc/python-module-jk-svg)
* [pypi.python.org](https://pypi.python.org/pypi/jk_svg)

Why this module?
----------------

Sometimes it is easier to create SVG graphics (or parts of SVG graphics) programmatically than drawing them by hand. This module assists in this task of creating such SVG graphics as there is no comparable module offering these kind of features.

Limitations of this module
--------------------------

This module currently only supports these kind of shapes:

* `circle`
* `ellipse`
* `g`
* `line`
* `polygon`
* `polyline`
* `rect`

Additionally arbitrary elements of any kind can be provided, but those listed above will have a more beautiful API.

How to use this module
----------------------

### Import this module

Please include this module into your application using the following code:

```python
import jk_svg
```

### Create an SVG graphic main node

To be able to create geometry nodes we need to create a SVG graphic object first:

```python
svg = SVGGraphic()
```

Now we will be able to add arbitrary graphical SVG objects.

### How to build SVG graphics

SVG elements form a hierarchical structure. In order to stack SVG elements you therefore require nodes and subnodes that represent graphical shapes. Have a look at this SVG file:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
	xmlns:svg="http://www.w3.org/2000/svg"
	height="297mm"
	width="210mm"
	version="1.1"
	>
	<g>
		<line
			style="opacity:1;fill:none;fill-opacity:1;stroke:#008000;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:5;stroke-dasharray:none;stroke-opacity:1"
			y1="100"
			x2="300"
			x1="100"
			y2="200"
			/>
		<ellipse
			style="opacity:1;fill:none;fill-opacity:1;stroke:#0000c0;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:5;stroke-dasharray:none;stroke-opacity:1"
			cx="250"
			cy="140"
			ry="50"
			rx="75"
			/>
		<polygon
			style="opacity:1;fill:none;fill-opacity:1;stroke:#c00000;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:5;stroke-dasharray:none;stroke-opacity:1"
			points="120,100 200,120 180,200 100,180"
			/>
	</g>
</svg>
```

This file can be created using the following python code:

```python
with svg.createGroup() as g:

	with g.createLine() as line:
		line.style = STYLE_GREEN
		line.x1 = 100
		line.y1 = 100
		line.x2 = 300
		line.y2 = 200

	with g.createEllipse() as ellipse:
		ellipse.style = STYLE_BLUE
		ellipse.cx = 250
		ellipse.cy = 140
		ellipse.rx = 75
		ellipse.ry = 50

	with g.createPolygon() as poly:
		poly.style = STYLE_RED
		poly.points.append( (20, 0) )
		poly.points.append( (100, 20) )
		poly.points.append( (80, 100) )
		poly.points.append( (0, 80) )
		poly.move(100, 100)
```

The `with` statements shown in this example are just a convenience to allow the source code to better reflect the hierarchical structure of the resulting SVG file. In this specific case there are no specific actions involved in entering or leaving this context. So the code shown above is equivalent to the following example:

```python
g = svg.createGroup()

line = g.createLine()
line.style = STYLE_GREEN
line.x1 = 100
line.y1 = 100
line.x2 = 300
line.y2 = 200

ellipse = g.createEllipse()
ellipse.style = STYLE_BLUE
ellipse.cx = 250
ellipse.cy = 140
ellipse.rx = 75
ellipse.ry = 50

poly = g.createPolygon()
poly.style = STYLE_RED
poly.points.append( (20, 0) )
poly.points.append( (100, 20) )
poly.points.append( (80, 100) )
poly.points.append( (0, 80) )
poly.move(100, 100)
```

The mechanism is always the same: Create a subcomponent that will be a child component to its parent. In this example `g` is created which is then used to create a `line`, a an`ellipse` and a `polygon` subcomponent. While every component is basically the same ans contains an `attributes` and `children` member that holds the attributes and children, additional convenience members are provided. Here they are used to specify location, shape and style data. These convenience members depend on the specific shape: Therefore if you use `createLine()` you will get a slightly different SVG object compared to calling `createEllipse()` or any other create-method. This aspect assists in working with SVG data as it makes defining geometries very easy.

Contact Information
-------------------

This work is Open Source. This enables you to use this work for free.

Please have in mind this also enables you to contribute. We, the subspecies of software developers, can create great things. But the more collaborate, the more fantastic these things can become. Therefore Feel free to contact the author(s) listed below, either for giving feedback, providing comments, hints, indicate possible collaborations, ideas, improvements. Or maybe for "only" reporting some bugs:

* Jürgen Knauth: pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



