import matplotlib
# if your matplotlib doesn't pop up a window, force it to use tkinter backend
# matplotlib.use("tkagg")

from matplotlib import pyplot as plt

# Colors
# Define new colors as 4-tuples of the form (r, g, b, 1) where
# r, g, b are values between 0 and 1 indicating the amount of red, green, and blue.
RED = (1, 0, 0, 1)
MAROON = (0.5, 0, 0, 1)
GREEN = (0, 0.5, 0, 1)
BLUE = (0, 0, 1, 1)
PURPLE = (0.5, 0, 0.5, 1)
BLACK = (0, 0, 0, 1)
LINEWIDTH = 2
FONTSIZE = 12

class FigureWrapper:
    def __init__(self, title):
        self.fig = plt.figure()
        self.ax = self.fig.subplots(1, 1) # creates a figure with one Axes (plot)
        self.ax.autoscale()
        self.ax.margins(0.1)
        self.ax.axis("off")
        self.ax.set_title(title)
    
    def line(self, p1, p2, col=BLACK):
        x0, y0 = p1
        x1, y1 = p2
        self.ax.plot([x0, x1], [y0, y1], color=col, linewidth=LINEWIDTH)
    
    def dot(self, p, col=BLACK):
        x, y = p
        self.ax.plot(x, y, 'o', color=col)
    
    def text(self, p, s, col=BLACK):
        x, y = p
        self.ax.text(x, y, s, color=col, fontsize=FONTSIZE)
    
    def show(self):
        plt.figure(self.fig.number)
        plt.show()

    def save(self, filename):
        self.fig.savefig(filename)