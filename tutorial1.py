from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, green)
# A graphics asset that represents a rectangle
rectangle = PolygonAsset([(0,0), (20,5), (30,50), (0,0)], thinline, red)

# Now display a rectangle
Sprite(rectangle, (200, 50))

myapp = App()
myapp.run()