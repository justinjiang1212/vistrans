# render_settings.py

VERTICAL_OFFSET = 0.3    # Offset for drawing parasite nodes above host nodes
COSPECIATION_OFFSET = .3    # Offest for drawing parasite nodes closer to host 
                            # nodes for speciation events
NODE_OFFSET = 0.3
TRACK_OFFSET = 0.3
TIP_TEXT_OFFSET = (.3, 0)
INTERNAL_TEXT_OFFSET = (.05, .05)


# Colors
# Define new colors as 4-tuples of the form (r, g, b, 1) where
# r, g, b are values between 0 and 1 indicating the amount of red, green, and blue.
RED = (1, 0, 0, 1)


MAROON = (0.5, 0, 0, 1)
GREEN = (0, 0.5, 0, 1)

PURPLE = (0.5, 0, 0.5, 1)
BLACK = (0, 0, 0, 1)
GRAY = (0.5, 0.5, 0.5, 1)
PURPLE = (.843, .00, 1.0, 1)

BLUE = (.09, .216, .584, 1)
ROYAL_BLUE = (.3, .4, .9, 1)
CYAN = (.3, .9, .75, 1)
RED_BLUSH = (.882, .255, .412, 1)
PRETTY_YELLOW = (.882, .725, .255, 1)
ORANGE_ORANGE = (1.00, .502, 0	, 1)

LEAF_NODE_COLOR = BLUE
COSPECIATION_NODE_COLOR = ORANGE_ORANGE
DUPLICATION_NODE_COLOR = PURPLE
TRANSFER_NODE_COLOR = RED_BLUSH
HOST_NODE_COLOR = BLACK
HOST_EDGE_COLOR = BLACK
PARASITE_EDGE_COLOR = ROYAL_BLUE
LOSS_EDGE_COLOR = GRAY

TRANSFER_TRANSPARENCY = 0.5

LEAF_NODE_SHAPE = "o"
COSPECIATION_NODE_SHAPE = "o"
DUPLICATION_NODE_SHAPE = "D"
TRANSFER_NODE_SHAPE = "s"

TIP_ALIGNMENT = 'center'

CENTER_CONSTANT = 3 / 8

FONT_SIZE = 20
MIN_FONT_SIZE = 0
MAX_FONT_SIZE = .3

INTERNAL_NODE_ALPHA = 0.7