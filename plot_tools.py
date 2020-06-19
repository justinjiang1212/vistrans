"""
plot_tools.py
Plotting tools using matplotlib
"""

# If matplotlib doesn't pop up a window, force it to use tkinter backend
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
GRAY = (0.5, 0.5, 0.5, 1)
LINEWIDTH = 2
LINE_Z_ORDER = 0
DOT_Z_ORDER = 1
FONTSIZE = 12
TRANSFERSIZE = 20

class FigureWrapper:
    """ Class definining plotting methods """
    def __init__(self, title):
        self.fig = plt.figure()
        self.axis = self.fig.subplots(1, 1) # creates a figure with one Axes (plot)
        self.axis.autoscale()
        self.axis.margins(0.1)
        self.axis.axis("off")
        self.axis.set_title(title)

    def line(self, point_1, point_2, col=BLACK, linestyle='-', marker=None):
        """
        Draw line from point p1 to p2
        """
        x_1, y_1 = point_1
        x_2, y_2 = point_2
        self.axis.plot([x_1, x_2], [y_1, y_2], color=col, linewidth=LINEWIDTH, linestyle=linestyle, zorder=LINE_Z_ORDER)

    def dot(self, point, col=BLACK):
        """
        Plot dot at point p
        """
        x, y = point
        self.axis.plot(x, y, 'o', color=col, zorder=DOT_Z_ORDER)
    
    def text(self, point, text, col=BLACK):
        """
        Plot text at s at point p
        """
        x, y = point
        self.axis.text(x, y, text, color=col, fontsize=FONTSIZE)

    def show(self):
        """ 
        Display figure
        """
        plt.figure(self.fig.number)
        plt.show()

    def save(self, filename):
        """
        Save figure to file
        """
        self.fig.savefig(filename)
    
    def half_arrow(self, point_1, point_2, col=BLACK):
        """
        Draw arrow from point p1 to p2
        """
        x_1, y_1 = point_1
        x_2, y_2 = point_2
        self.axis.arrow(x_1, y_1, 0, abs(y_2-y_1)/2, head_width=0.15, head_length=0.15, color=col, linewidth=LINEWIDTH/2, shape='full', length_includes_head=True, zorder=LINE_Z_ORDER)

    def up_triangle(self, point, col = BLACK, markersize=TRANSFERSIZE):
        """
        Draw an upwards triangle on point
        """
        x, y = point
        self.axis.plot(x, y, '^', color=col, zorder= LINE_Z_ORDER, markersize=TRANSFERSIZE)

    def down_triangle(self, point, col = BLACK, markersize=TRANSFERSIZE):
        """
        Draw an downwards triangle on point
        """
        x, y = point
        self.axis.plot(x, y, 'v', color=col, zorder= LINE_Z_ORDER, markersize=TRANSFERSIZE)