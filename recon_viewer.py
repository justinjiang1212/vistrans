"""
recon_viewer.py
View a single reconciliation using matplotlib
"""

from recon import EventType
from math import exp, ceil
import utils
import plot_tools
from render_settings import LEAF_NODE_COLOR, COSPECIATION_NODE_COLOR, \
    DUPLICATION_NODE_COLOR, TRANSFER_NODE_COLOR, HOST_NODE_COLOR, HOST_EDGE_COLOR, \
    PARASITE_EDGE_COLOR, VERTICAL_OFFSET, COSPECIATION_OFFSET, TRACK_OFFSET, NODE_OFFSET, \
    TIP_TEXT_OFFSET, FONT_SIZE, MIN_FONT_SIZE, LEAF_NODE_SHAPE, COSPECIATION_NODE_SHAPE, \
        DUPLICATION_NODE_SHAPE, TRANSFER_NODE_SHAPE, TIP_ALIGNMENT

def render(host_dict, parasite_dict, recon_dict, show_internal_labels=False, show_freq=False):
    """ Renders a reconciliation using matplotlib
    :param host_dict:  Host tree represented in dictionary format
    :param parasite_dict:  Parasite tree represented in dictionary format
    :recon_dict: Reconciliation represented in dictionary format
    """
    host_tree, parasite_tree, recon, consistency_type = utils.convert_to_objects(host_dict, parasite_dict, recon_dict)

    give_childeren_parents(host_tree)

    fig = plot_tools.FigureWrapper("Reconciliation")

    num_tips = len(host_tree.leaf_list) + len(parasite_tree.leaf_list)
    font_size = calculate_font_size(num_tips)
    #print(font_size)
    render_host(fig, host_tree, show_internal_labels, font_size)
    host_lookup = host_tree.name_to_node_dict()
    render_parasite(fig, parasite_tree, recon, host_lookup, show_internal_labels, show_freq, font_size)
    fig.show()


#TODO Fix Bug
def give_childeren_parents(host_tree):
    for node in host_tree.postorder_list:
        if node.right_node:
            node.right_node.parent_node = node

def render_host(fig, host_tree, show_internal_labels, font_size):
    """ Renders the host tree """
    set_host_node_layout(host_tree)
    root = host_tree.root_node
    draw_host_handle(fig, root)
    render_host_helper(fig, root, show_internal_labels, font_size)

def draw_host_handle(fig, root):
    """ Draw edge leading to root of host tree. """
    fig.line((0, root.layout.y), (root.layout.x, root.layout.y), HOST_EDGE_COLOR)

def render_host_helper(fig, node, show_internal_labels, font_size):
    """ Helper function for rendering the host tree. """
    node_x, node_y = node.layout.x, node.layout.y
    node_xy = (node_x, node_y)
    if node.is_leaf:
        fig.dot(node_xy)
        fig.text((node_x + TIP_TEXT_OFFSET[0], node_y - TIP_TEXT_OFFSET[1]), node.name, font_size = font_size, vertical_alignment=TIP_ALIGNMENT)
    else:
        fig.dot(node_xy, col = HOST_NODE_COLOR)  # Render host node
        if show_internal_labels:
            fig.text(node_xy, node.name)
        left_x, left_y = node.left_node.layout.x, node.left_node.layout.y
        right_x, right_y = node.right_node.layout.x, node.right_node.layout.y
        fig.line(node_xy, (node_x, left_y), HOST_EDGE_COLOR)
        fig.line(node_xy, (node_x, right_y), HOST_EDGE_COLOR)
        fig.line((node_x, left_y), (left_x, left_y), HOST_EDGE_COLOR)
        fig.line((node_x, right_y), (right_x, right_y), HOST_EDGE_COLOR)
        render_host_helper(fig, node.left_node, show_internal_labels, font_size)
        render_host_helper(fig, node.right_node, show_internal_labels, font_size)

def render_parasite(fig, parasite_tree, recon, host_lookup, show_internal_labels, show_freq, font_size):
    """ Render the parasite tree. """
    root = parasite_tree.root_node
    render_parasite_helper(fig, root, recon, host_lookup, show_internal_labels, show_freq, font_size)

def render_parasite_helper(fig, node, recon, host_lookup, show_internal_labels, show_freq, font_size):
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
        node.layout.y += host_node.iter_track("C") * NODE_OFFSET
    if event.event_type is EventType.TIPTIP:
        node.layout.y += host_node.iter_track("T") * NODE_OFFSET
    # Render parasite node and recurse if not a leaf
    
    if node.is_leaf:
        render_parasite_node(fig, node, event, font_size)
        return

    render_parasite_helper(fig, node.left_node, recon, host_lookup, \
        show_internal_labels, show_freq, font_size)
    render_parasite_helper(fig, node.right_node, recon, host_lookup, \
        show_internal_labels, show_freq, font_size)
    
    render_parasite_branches(fig, node, recon, host_lookup)
    render_parasite_node(fig, node, event, font_size, show_internal_labels, show_freq)

def render_parasite_node(fig, node, event, font_size, show_internal_labels=False, show_freq=False):
    """
    Renders a single parasite node
    """
    node_xy = (node.layout.x, node.layout.y)
    render_color, render_shape = event_color_shape(event)
    
    fig.dot(node_xy, col = render_color, marker = render_shape)

    if node.is_leaf:
        fig.text((node.layout.x + TIP_TEXT_OFFSET[0], node.layout.y - + TIP_TEXT_OFFSET[1]), node.name, render_color, font_size = font_size, vertical_alignment=TIP_ALIGNMENT)
    else:
        fig.text(node_xy, node.name, render_color)

    if show_freq:
        fig.text(node_xy, event.freq, render_color)

def calculate_font_size(n):
    """Calculates the font_size given a number"""
    output = FONT_SIZE - n

    if output < MIN_FONT_SIZE:
        return MIN_FONT_SIZE
    else:
        return output

def render_parasite_branches(fig, node, recon, host_lookup):
    """ Very basic branch drawing """
    node_xy = (node.layout.x, node.layout.y)

    left_xy = (node.left_node.layout.x, node.left_node.layout.y)
    right_xy = (node.right_node.layout.x, node.right_node.layout.y)
    

    mapping_node = recon.mapping_of(node.name)
    event = recon.event_of(mapping_node)

    if event.event_type is EventType.COSPECIATION:
        render_cospeciation_branch(node, host_lookup, recon, fig)
        #connect_children(node, host_lookup, recon, fig)
        
    if event.event_type is EventType.DUPLICATION:
        #render_duplication_branch(node_xy, mapping_node, host_lookup, fig, recon, node)
        connect_children(node, host_lookup, recon, fig)

    if event.event_type is EventType.TRANSFER:
        connect_child_to_parent(node, node.left_node, host_lookup, recon, fig)
        render_transfer_branch(node_xy, left_xy, right_xy, fig, node, host_lookup, recon)
                
    if event.event_type is EventType.LOSS: 
        #render_loss_branch(node_xy, left_xy, fig)
        pass


def connect_children(node, host_lookup, recon, fig):
    connect_child_to_parent(node, node.left_node, host_lookup, recon, fig)
    connect_child_to_parent(node, node.right_node, host_lookup, recon, fig)

def render_loss_branch(node_xy, next_xy, fig):

    #Create vertical line to next node
    mid_xy = (node_xy[0],next_xy[1])
    fig.line(node_xy, mid_xy, PARASITE_EDGE_COLOR, linestyle='--')
    fig.line(mid_xy, next_xy, PARASITE_EDGE_COLOR)

def render_cospeciation_branch(node, host_lookup, recon, fig):
    """
    Renders the a cospeciation branch.
    :param 
    """

    left_node = node.left_node
    right_node = node.right_node

    node_xy = (node.layout.x, node.layout.y)
    left_xy = (left_node.layout.x, left_node.layout.y)
    right_xy = (right_node.layout.x, right_node.layout.y)

    mapping_node = recon.mapping_of(node.name)
    host_node = host_lookup[mapping_node.host]


    left_mapping_node = recon.mapping_of(left_node.name)
    left_host_node = host_lookup[left_mapping_node.host]

    right_mapping_node = recon.mapping_of(right_node.name)
    right_host_node = host_lookup[right_mapping_node.host]
    
    #Draw left node
    if host_node.left_node.name == left_host_node.name:
        render_line_to(node_xy, left_xy, fig)
        host_node.layout.lower_v_track += (host_node.layout.x - node_xy[0]) / TRACK_OFFSET
    else:
        stop_row = host_node.left_node.layout.row
        host_node.layout.h_track += 1
        connect_child_to_parent(node, left_node, host_lookup, recon, fig, stop_row=stop_row)

    #Draw Right node
    if host_node.right_node.name == right_host_node.name:
        render_line_to(node_xy, right_xy, fig)
        host_node.layout.upper_v_track += (host_node.layout.x - node_xy[0]) / TRACK_OFFSET
    else:
        stop_row = host_node.right_node.layout.row
        host_node.layout.h_track += 1
        connect_child_to_parent(node, right_node, host_lookup, recon, fig, stop_row=stop_row)

#TODO change this name
def render_line_to(node_xy, other_xy, fig):
    mid_xy = (node_xy[0], other_xy[1])
    fig.line(node_xy, mid_xy, PARASITE_EDGE_COLOR)
    fig.line(mid_xy, other_xy, PARASITE_EDGE_COLOR)

def render_transfer_branch(node_xy, left_xy, right_xy, fig, node, host_lookup, recon):
    #Draw left node
    #mid_xy = (node_xy[0], left_xy[1])
    #fig.line(node_xy, mid_xy, PARASITE_EDGE_COLOR)
    #fig.line(mid_xy, left_xy, PARASITE_EDGE_COLOR)
    mapping_node = recon.mapping_of(node.name)
    host_node = host_lookup[mapping_node.host]

    if host_node.parent_node.layout.col < node.layout.col:
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
    else:
        fig.line(node_xy, right_xy, PARASITE_EDGE_COLOR)


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
    render_loss_branch(end_xy, next_xy, fig)
    

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
    render_loss_branch(end_xy, next_xy, fig)
    

def connect_child_to_parent(node, child_node, host_lookup, recon, fig, stop_row=None):
    """
    Connects a child node to its parent node
    param
    """
    mapping_node = recon.mapping_of(child_node.name)
    host_node = host_lookup[mapping_node.host]
    
    if not(stop_row):
        stop_row = node.layout.row

    current_xy = (child_node.layout.x, child_node.layout.y)


    while host_node.layout.row != stop_row:
        parent_node = host_node.parent_node
        if parent_node.layout.row < host_node.layout.row:
            v_track = parent_node.iter_track("UV")
        else:
            v_track = parent_node.iter_track("LV")
        h_track = parent_node.iter_track("H")


        sub_parent_xy = (parent_node.layout.x - (TRACK_OFFSET * v_track) - VERTICAL_OFFSET, \
            parent_node.layout.y + (TRACK_OFFSET * h_track) + VERTICAL_OFFSET)

        render_loss_branch(sub_parent_xy, current_xy, fig)

        host_node = parent_node
        current_xy = sub_parent_xy
    
    node_xy = (node.layout.x, node.layout.y)

    mid_xy = (node_xy[0], current_xy[1])

    fig.line(node_xy, mid_xy, PARASITE_EDGE_COLOR)
    fig.line(mid_xy, current_xy, PARASITE_EDGE_COLOR)

    

def set_parasite_bend(host_node, VERTICAL_OFFSET):
    """return the translated coordinates where the branch bends"""
    return (host_node.layout.x - (VERTICAL_OFFSET*2), host_node.layout.y + VERTICAL_OFFSET)

def event_color_shape(event):
    """ Return color for drawing event, depending on event type. """
    if event.event_type is EventType.TIPTIP:
        return LEAF_NODE_COLOR, LEAF_NODE_SHAPE
    if event.event_type is EventType.COSPECIATION:
        return COSPECIATION_NODE_COLOR, COSPECIATION_NODE_SHAPE
    if event.event_type is EventType.DUPLICATION:
        return DUPLICATION_NODE_COLOR, DUPLICATION_NODE_SHAPE
    if event.event_type is EventType.TRANSFER:
        return TRANSFER_NODE_COLOR, TRANSFER_NODE_SHAPE
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
