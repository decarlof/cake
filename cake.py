###############################################
# Lukas Vogt
# 3/23/23
# Period 5
# Object Composition and Inheritance Lab 10 Points?
###############################################

# Imports
import graphics

# Base of the Cake
class Layer(object):
    def __init__(self, x, y, width, height, color, win):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.win = win
        self.makeLayer()

    def makeLayer(self):
        base = graphics.Rectangle(graphics.Point(self.x, self.y), graphics.Point(self.x + self.width, self.y + self.height))
        base.setFill(self.color)
        base.draw(self.win)

class Cake(Layer):
    def __init__(self, x, y, width, height, nlayers, win):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.nlayers = nlayers
        self.win = win

        layer = 0
        while layer < self.nlayers:
            if (layer % 2) == 0:
                color = 'tan'
            else:
                color = 'red'
            Layer(self.x, self.y-layer * self.height, self.width, self.height, color, self.win)
            layer += 1

    def top(self):
        return (self.y - (self.height * self.nlayers))

class Candles(Layer):
    def __init__(self, x, y, cake_width, candle_width, candle_height, ncandles, win):
        self.x = x
        self.y = y
        self.cake_width = cake_width
        self.candle_height = candle_height
        self.candle_width = candle_width
        self.birthday_cake_top = y
        self.ncandles = ncandles
        self.win = win

    def draw(self):
        candle_counter = 0
        candle_delta_x = self.cake_width / self.ncandles
        while candle_counter < self.ncandles:
            candle_x_location = self.x + candle_delta_x * candle_counter
            candle = graphics.Rectangle(graphics.Point(candle_x_location, self.birthday_cake_top), graphics.Point(candle_x_location + self.candle_width, self.birthday_cake_top - self.candle_height))
            candle.setFill('red')
            candle.draw(self.win)
            candle_counter += 1

class BirtdayCake(Cake):
    def __init__(self, x, y, width, height, nlayers, ncandles, win):
        cake = Cake(x, y, width, height, nlayers, win)
        birthday_cake_top = cake.top()
        candels = Candles(x, birthday_cake_top, width, 10, 100, ncandles, win)
        candels.draw()

# Main Driver Code
def main():
    win = graphics.GraphWin('Cake', 1000, 600)
    # Layer(300, 500, 500, 10, 'tan', win)
    # cake = Cake(300, 500, 500, 5, 50, win)
    # print(cake.top())
    BirtdayCake(300, 500, 500, 5, 30, 17, win)

    win.getMouse()

main()