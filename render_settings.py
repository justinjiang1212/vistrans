# render_settings.py
import plot_tools

VERTICAL_OFFSET = 0.3      # Offset for drawing parasite nodes above host nodes
COSPECIATION_OFFSET = .4    # Offest for drawing parasite nodes closer to host 
                            # nodes for speciation events
NODE_OFFSET = 0.4
TRACK_OFFSET = 0.3
                        
LEAF_NODE_COLOR = plot_tools.MAROON
COSPECIATION_NODE_COLOR = plot_tools.BLUE
DUPLICATION_NODE_COLOR = plot_tools.GREEN
TRANSFER_NODE_COLOR = plot_tools.RED
HOST_NODE_COLOR = plot_tools.BLACK
HOST_EDGE_COLOR = plot_tools.BLACK
PARASITE_EDGE_COLOR = plot_tools.GRAY
