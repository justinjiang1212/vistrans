from recon import MappingNode, ReconGraph, Reconciliation, EventType
from recon import Cospeciation, Duplication, Transfer, Loss, TipTip
import utils
import plot_tools

VERTICAL_OFFSET = 0.1       # Offset for drawing parasite nodes above host nodes
COSPECIATION_OFFSET = 0.8   # Offest for drawing parasite nodes closer to host 
                            # nodes for speciation events

def render(host_dict, parasite_dict, recon_dict):
    """ Renders a reconciliation using matplotlib
    :param host_dict:  Host tree represented in dictionary format 
    :param parasite_dict:  Parasite tree represented in dictionary format
    :recon_dict: Reconciliation represented in dictionary format
    """
    host_tree, parasite_tree, recon = utils.convert_to_objects(host_dict, parasite_dict, recon_dict)
    fig = plot_tools.FigureWrapper("Reconciliation")
    render_host(fig, host_tree, show_internal_labels=True)
    host_lookup = host_tree.name_to_node_dict()
    render_parasite(fig, parasite_tree, recon, host_lookup)
    fig.show()

def render_host(fig, host_tree, show_internal_labels = False):
    """ Renders the host tree """
    set_host_node_layout(host_tree)
    root = host_tree.root_node
    draw_host_handle(fig, root)
    render_host_helper(fig, root, show_internal_labels)

def draw_host_handle(fig, root):
    """ Draw edge leading to root of host tree. """
    fig.line((0, root.layout.y), (root.layout.x, root.layout.y))

def render_host_helper(fig, node, show_internal_labels = False):
    """ Helper function for rendering the host tree. """
    node_x, node_y = node.layout.x, node.layout.y
    node_xy = (node_x, node_y)
    if node.is_leaf:
        fig.dot(node_xy)
        fig.text(node_xy, node.name)
    else:
        fig.dot(node_xy)
        if show_internal_labels:
            fig.text(node_xy, node.name)
        left_x, left_y = node.left_node.layout.x, node.left_node.layout.y
        right_x, right_y = node.right_node.layout.x, node.right_node.layout.y
        fig.line(node_xy, (node_x, left_y))
        fig.line(node_xy, (node_x, right_y))
        fig.line((node_x, left_y), (left_x, left_y))
        fig.line((node_x, right_y), (right_x, right_y))
        render_host_helper(fig, node.left_node)
        render_host_helper(fig, node.right_node)

def render_parasite(fig, parasite_tree, recon, host_lookup, show_internal_labels = False):
    """ Render the parasite tree. """
    # THIS IS WHAT NEEDS TO BE COMPLETED.
    # WE NEED TO DRAW THE EDGES CONNECTING THE PARASITE NODES.
    root = parasite_tree.root_node
    render_parasite_helper(fig, root, recon, host_lookup, show_internal_labels)

def render_parasite_helper(fig, node, recon, host_lookup, show_internal_labels = False):
    """ Helper function for rendering the parasite tree. """
    # mapping_node is of type MappingNode which associates
    # a parasite to a host in a reconciliation
    mapping_node = recon.mapping_of(node.name)  

    # A reconciliation has an event_of method which is an object of
    # type Event.
    event = recon.event_of(mapping_node)

    host_name = mapping_node.host

    # host_lookup is a dictionary computed in the Tree class
    # that associates a host name (a string) with the correspond node
    # object for that host.  The node object contains layout information
    # which we need here.
    host_node = host_lookup[host_name]

    host_row, host_col, host_x, host_y = host_node.get_layout()
    node.set_layout(row=host_row, x=node.layout.col, y=host_y + VERTICAL_OFFSET)
    color = event_color(event)

    if event.event_type is EventType.COSPECIATION: 
        node.layout.x += COSPECIATION_OFFSET
    point = (node.layout.x, node.layout.y)
    if node.is_leaf:
        fig.dot(point, color)
        fig.text(point, node.name, color)
    else:
        fig.dot(point, color)
        fig.text(point, node.name, color)
        render_parasite_helper(fig, node.left_node, recon, host_lookup, show_internal_labels)
        render_parasite_helper(fig, node.right_node, recon, host_lookup, show_internal_labels)   

def event_color(event):
    """ Return color for drawing event, depending on event type. """
    if event.event_type is EventType.TIPTIP:
        return plot_tools.MAROON
    elif event.event_type is EventType.COSPECIATION:
        return plot_tools.GREEN 
    elif event.event_type is EventType.DUPLICATION:
        return plot_tools.BLUE
    else: return plot_tools.PURPLE

def set_host_node_layout(host_tree):
    """ 
    Sets the logicalRow and logicalCol values of each Node in host_tree.
    Assumes that each host Node has its order set already and this function
    uses those values and structure of the tree to set the logicalRow and logicalCol
    :param host_tree:  A Tree object representing the host tree
    :return None
    """
 
    #sets logical row values for leaves in the order they appear in the list of host tree leaves
    logical_row_counter = 0
    for leaf in host_tree.leaf_list:
        leaf.layout.row = logical_row_counter
        leaf.layout.x = leaf.layout.col           # This can be scaled if desired
        leaf.layout.y = leaf.layout.row           # This can be scaled if desired
        logical_row_counter += 1
    
    #helper function to assign row values, postorder traversal
    set_internal_host_nodes(host_tree.root_node)

def set_internal_host_nodes(node):
    """ Helper function for set_host_node_layout. """
    if node.is_leaf: return
    else:
        set_internal_host_nodes(node.left_node)
        set_internal_host_nodes(node.right_node)
        node.layout.row = (node.left_node.layout.row + node.right_node.layout.row)/2
        node.layout.x = node.layout.col         # This can be scaled if desired
        node.layout.y = node.layout.row         # This can be scaled if desired






    

