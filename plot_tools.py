"""
plot_tools.py
Plotting tools using matplotlib
"""

# If matplotlib doesn't pop up a window, force it to use tkinter backend
# matplotlib.use("tkagg")

from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.collections import LineCollection

from render_settings import COSPECIATION_NODE_COLOR, \
    DUPLICATION_NODE_COLOR, TRANSFER_NODE_COLOR, HOST_NODE_COLOR, \
    PARASITE_EDGE_COLOR, RED, MAROON, GREEN, BLUE, PURPLE, BLACK, GRAY, \
        COSPECIATION_NODE_SHAPE, DUPLICATION_NODE_SHAPE, TRANSFER_NODE_SHAPE


LINEWIDTH = 2
LINE_Z_ORDER = 0
DOT_Z_ORDER = 1
FONTSIZE = 12
TRANSFERSIZE = 10
NODESIZE = 8

DEFAULT_ALIGNMENT = 'bottom'

class FigureWrapper:
    """ Class definining plotting methods """
    def __init__(self, title):
        self.fig = plt.figure()
        self.axis = self.fig.subplots(1, 1) # creates a figure with one Axes (plot)
        self.axis.autoscale()
        self.axis.margins(0.1)
        self.axis.axis("off")
        self.axis.set_title(title)


        legend_elements = [
                          Line2D([0], [0], marker= COSPECIATION_NODE_SHAPE, color='w', label='Cospeciation', \
                          markerfacecolor=COSPECIATION_NODE_COLOR, markersize=NODESIZE),
                          Line2D([0], [0], marker=DUPLICATION_NODE_SHAPE, color='w', label='Duplication', \
                          markerfacecolor=DUPLICATION_NODE_COLOR, markersize=NODESIZE),
                          Line2D([0], [0], marker=TRANSFER_NODE_SHAPE, color='w', label='Transfer', \
                          markerfacecolor=TRANSFER_NODE_COLOR, markersize=NODESIZE),\
                          LineCollection( [[(0, 0)]], linestyles = ['dashed'], \
                              colors = [PARASITE_EDGE_COLOR], label='Loss')
                
                          ] 
        
        self.axis.legend(handles=legend_elements, loc='lower left', fontsize = FONTSIZE)
        

    def line(self, point_1, point_2, col=BLACK, linestyle='-', marker=None):
        """
        Draw line from point p1 to p2
        """
        x_1, y_1 = point_1
        x_2, y_2 = point_2
        self.axis.plot([x_1, x_2], [y_1, y_2], color=col, linewidth=LINEWIDTH, linestyle=linestyle, zorder=LINE_Z_ORDER)

    def dot(self, point, marker = 'o', col=BLACK):
        """
        Plot dot at point p
        """
        x, y = point
        self.axis.plot(x, y, marker, color=col, zorder=DOT_Z_ORDER)
    
    def text(self, point, text, col=BLACK, font_size=FONTSIZE, vertical_alignment=DEFAULT_ALIGNMENT ):
        """
        Plot text at s at point p
        """
        x, y = point
        self.axis.text(x, y, text, color=col, fontsize=font_size, verticalalignment=vertical_alignment)

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