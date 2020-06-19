"""
recon_viewer.py
View a single reconciliation using matplotlib
"""

from recon import EventType
import utils
import plot_tools
from render_settings import LEAF_NODE_COLOR, COSPECIATION_NODE_COLOR, \
    DUPLICATION_NODE_COLOR, TRANSFER_NODE_COLOR, HOST_NODE_COLOR, HOST_EDGE_COLOR, \
    PARASITE_EDGE_COLOR, VERTICAL_OFFSET, COSPECIATION_OFFSET, TRACK_OFFSET

def render(host_dict, parasite_dict, recon_dict, show_internal_labels=False, show_freq=False):
    """ Renders a reconciliation using matplotlib
    :param host_dict:  Host tree represented in dictionary format
    :param parasite_dict:  Parasite tree represented in dictionary format
    :recon_dict: Reconciliation represented in dictionary format
    """
    host_tree, parasite_tree, recon = utils.convert_to_objects(host_dict, parasite_dict, recon_dict)
    print(recon._parasite_map) #TODO get this parasite map to include losses?
    fig = plot_tools.FigureWrapper("Reconciliation")
    render_host(fig, host_tree, show_internal_labels)
    host_lookup = host_tree.name_to_node_dict()
    render_parasite(fig, parasite_tree, recon, host_lookup, show_internal_labels, show_freq)
    fig.show()

def render_host(fig, host_tree, show_internal_labels):
    """ Renders the host tree """
    set_host_node_layout(host_tree)
    root = host_tree.root_node
    draw_host_handle(fig, root)
    render_host_helper(fig, root, show_internal_labels)

def draw_host_handle(fig, root):
    """ Draw edge leading to root of host tree. """
    fig.line((0, root.layout.y), (root.layout.x, root.layout.y), HOST_EDGE_COLOR)

def render_host_helper(fig, node, show_internal_labels):
    """ Helper function for rendering the host tree. """
    node_x, node_y = node.layout.x, node.layout.y
    node_xy = (node_x, node_y)
    if node.is_leaf:
        fig.dot(node_xy)
        fig.text(node_xy, node.name)
    else:
        fig.dot(node_xy, HOST_NODE_COLOR)  # Render host node
        if show_internal_labels:
            fig.text(node_xy, node.name)
        left_x, left_y = node.left_node.layout.x, node.left_node.layout.y
        right_x, right_y = node.right_node.layout.x, node.right_node.layout.y
        fig.line(node_xy, (node_x, left_y), HOST_EDGE_COLOR)
        fig.line(node_xy, (node_x, right_y), HOST_EDGE_COLOR)
        fig.line((node_x, left_y), (left_x, left_y), HOST_EDGE_COLOR)
        fig.line((node_x, right_y), (right_x, right_y), HOST_EDGE_COLOR)
        render_host_helper(fig, node.left_node, show_internal_labels)
        render_host_helper(fig, node.right_node, show_internal_labels)

def render_parasite(fig, parasite_tree, recon, host_lookup, show_internal_labels, show_freq):
    """ Render the parasite tree. """
    root = parasite_tree.root_node
    render_parasite_helper(fig, root, recon, host_lookup, show_internal_labels, show_freq)

def render_parasite_helper(fig, node, recon, host_lookup, show_internal_labels, show_freq):
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

    # Set parasite node layout
    host_row = host_node.layout.row
    # host_col = host_node.layout.col
    # host_x = host_node.layout.x
    host_y = host_node.layout.y
    node.set_layout(row=host_row, x=node.layout.col, y=host_y + VERTICAL_OFFSET)
    
    if event.event_type is EventType.COSPECIATION:
        node.layout.x += COSPECIATION_OFFSET
    # Render parasite node and recurse if not a leaf
    
    if node.is_leaf:
        render_parasite_node(fig, node, event)
        return

    render_parasite_helper(fig, node.left_node, recon, host_lookup, \
        show_internal_labels, show_freq)
    render_parasite_helper(fig, node.right_node, recon, host_lookup, \
        show_internal_labels, show_freq)
    
    render_parasite_branches(fig, node, recon, host_lookup)
    render_parasite_node(fig, node, event, show_internal_labels, show_freq)

def render_parasite_node(fig, node, event, show_internal_labels=False, show_freq=False):
    """
    Renders a single parasite node
    """
    node_xy = (node.layout.x, node.layout.y)
    render_color = event_color(event)
    
    fig.dot(node_xy, render_color)
    fig.text(node_xy, node.name, render_color)

    if show_freq:
        fig.text(node_xy, event.freq, render_color)

def render_parasite_branches(fig, node, recon, host_lookup):
    """ Very basic branch drawing """
    node_xy = (node.layout.x, node.layout.y)

    left_xy = (node.left_node.layout.x, node.left_node.layout.y)
    right_xy = (node.right_node.layout.x, node.right_node.layout.y)
    

    mapping_node = recon.mapping_of(node.name)
    event = recon.event_of(mapping_node)

    if event.event_type is EventType.COSPECIATION:
        render_cospeciation_branch(node_xy, left_xy, right_xy, fig)
        
    if event.event_type is EventType.DUPLICATION:
        render_duplication_branch(node_xy, mapping_node, host_lookup, fig, recon, node)
        

    if event.event_type is EventType.TRANSFER:
        render_transfer_branch(node_xy, left_xy, right_xy, fig)
                
    if event.event_type is EventType.LOSS: 
        #render_loss_branch(node_xy, left_xy, mapping_node, host_lookup, fig)
        pass




def render_loss_branch(node_xy, next_xy, mapping_node, host_lookup, fig):

    #Create vertical line to next node
    mid_xy = (node_xy[0],next_xy[1])
    fig.line(node_xy, mid_xy, PARASITE_EDGE_COLOR, linestyle='--')
    fig.line(mid_xy, next_xy, PARASITE_EDGE_COLOR)

def render_cospeciation_branch(node_xy, left_xy, right_xy, fig):
    """
    Renders the a cospeciation branch.
    :param 
    """
    #Draw left node
    mid_xy = (node_xy[0], left_xy[1])
    fig.line(node_xy, mid_xy, PARASITE_EDGE_COLOR)


    fig.line(mid_xy, left_xy, PARASITE_EDGE_COLOR)

    #Draw Right node
    mid_xy = (node_xy[0], right_xy[1])
    fig.line(node_xy, mid_xy, PARASITE_EDGE_COLOR)
    fig.line(mid_xy, right_xy, PARASITE_EDGE_COLOR)

def render_transfer_branch(node_xy, left_xy, right_xy, fig):
    #Draw left node
    mid_xy = (node_xy[0], left_xy[1])
    fig.line(node_xy, mid_xy, PARASITE_EDGE_COLOR)
    fig.line(mid_xy, left_xy, PARASITE_EDGE_COLOR)

    #Draw right node, which is transfered
    mid_xy = (node_xy[0], right_xy[1])          #xy coords of midpoint
    y_midpoint = abs(mid_xy[1]+ node_xy[1])/2   #value of midpoint between mid_xy and parent node

    #determine if transfer is upwards or downwards, and draw trianle accordingly
    is_upwards = True if y_midpoint < mid_xy[1] else False
    if is_upwards:
        fig.up_triangle((node_xy[0], y_midpoint), PARASITE_EDGE_COLOR)
    else:
        fig.down_triangle((node_xy[0], y_midpoint), PARASITE_EDGE_COLOR)

    #draw branch to midpoint, then draw branch to child
    fig.line(node_xy, mid_xy, PARASITE_EDGE_COLOR)
    fig.line(mid_xy, right_xy, PARASITE_EDGE_COLOR)


def render_duplication_branch(node_xy, mapping_node, host_lookup, fig, recon, node):
    host_node = host_lookup[mapping_node.host]
    
    #using the coords of the host node, figure out where associated parasite node is
    dup_xy = (host_node.layout.x - (VERTICAL_OFFSET*2), host_node.layout.y + VERTICAL_OFFSET)



    #draw first track
    h_track = host_node.layout.h_track
    track_offset = h_track * TRACK_OFFSET           #computes an offset based on how many parasite edges are on host edge

    mid_xy = (node_xy[0], dup_xy[1] + track_offset)
    end_xy = (dup_xy[0], dup_xy[1] + track_offset)

    fig.line(node_xy, mid_xy, PARASITE_EDGE_COLOR)
    fig.line(mid_xy, end_xy, PARASITE_EDGE_COLOR)

    host_node.layout.h_track += 1                   #update the counter for keeping track of how many edges are on host

    #Render a loss on the left end
    next_xy = (node.left_node.layout.x, node.left_node.layout.y)
    render_loss_branch(end_xy, next_xy, mapping_node, host_lookup, fig)


    #TODO check what event to render at the end of a duplication
    

    #draw second track
    h_track = host_node.layout.h_track
    track_offset = h_track * TRACK_OFFSET
    mid_xy = (node_xy[0], dup_xy[1] + track_offset)
    end_xy = (dup_xy[0], dup_xy[1] + track_offset)
    
    fig.line(node_xy, mid_xy, PARASITE_EDGE_COLOR)
    fig.line(mid_xy, end_xy, PARASITE_EDGE_COLOR)

    host_node.layout.h_track += 1

    #Render a loss on the right end
    next_xy = (node.right_node.layout.x, node.right_node.layout.y)
    render_loss_branch(end_xy, next_xy, mapping_node, host_lookup, fig)
    

    


def event_color(event):
    """ Return color for drawing event, depending on event type. """
    if event.event_type is EventType.TIPTIP:
        return LEAF_NODE_COLOR
    if event.event_type is EventType.COSPECIATION:
        return COSPECIATION_NODE_COLOR
    if event.event_type is EventType.DUPLICATION:
        return DUPLICATION_NODE_COLOR
    if event.event_type is EventType.TRANSFER:
        return TRANSFER_NODE_COLOR
    return plot_tools.BLACK

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
    if node.is_leaf:
        return
    set_internal_host_nodes(node.left_node)
    set_internal_host_nodes(node.right_node)
    node.layout.row = (node.left_node.layout.row + node.right_node.layout.row)/2
    node.layout.x = node.layout.col         # This can be scaled if desired
    node.layout.y = node.layout.row         # This can be scaled if desired
