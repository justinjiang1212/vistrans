# render_settings.py

VERTICAL_OFFSET = 0.3    # Offset for drawing parasite nodes above host nodes
COSPECIATION_OFFSET = .3    # Offest for drawing parasite nodes closer to host 
                            # nodes for speciation events
NODE_OFFSET = 0.3
TRACK_OFFSET = 0.3
TIP_TEXT_OFFSET = (.3, 0)


# Colors
# Define new colors as 4-tuples of the form (r, g, b, 1) where
# r, g, b are values between 0 and 1 indicating the amount of red, green, and blue.
RED = (1, 0, 0, 1)


MAROON = (0.5, 0, 0, 1)
GREEN = (0, 0.5, 0, 1)

PURPLE = (0.5, 0, 0.5, 1)
BLACK = (0, 0, 0, 1)
GRAY = (0.5, 0.5, 0.5, 1)
PURPLE = (.459, .09, .584, 1)

BLUE = (.09, .216, .584, 1)
ROYAL_BLUE = (.255, .412, .882,.7 )
CYAN = (.255, .882, .725, 1)
RED_BLUSH = (.882, .255, .412, 1)
PRETTY_YELLOW = (.882, .725, .255, 1)
ORANGE_ORANGE = (.882, .412, .255, 1)

LEAF_NODE_COLOR = BLUE
COSPECIATION_NODE_COLOR = CYAN
DUPLICATION_NODE_COLOR = PRETTY_YELLOW
TRANSFER_NODE_COLOR = RED_BLUSH
HOST_NODE_COLOR = BLACK
HOST_EDGE_COLOR = BLACK
PARASITE_EDGE_COLOR = ROYAL_BLUE
LOSS_EDGE_COLOR = ORANGE_ORANGE

LEAF_NODE_SHAPE = "o"
COSPECIATION_NODE_SHAPE = "o"
DUPLICATION_NODE_SHAPE = "D"
TRANSFER_NODE_SHAPE = "s"

TIP_ALIGNMENT = 'center'

CENTER_CONSTANT = 3 / 8

FONT_SIZE = 20
MIN_FONT_SIZE = 8
