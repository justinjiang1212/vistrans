"""
tree.py
Defines classes related to host and parasite nodes and trees
"""

from enum import Enum

class TreeType(Enum):
    """ Defines type of the tree """
    HOST = 1
    PARASITE = 2

class Node:
    """ Defines a node of a tree """
    def __init__(self, name):
        self.name = name            # String; name of this host or parasite
        self.left_node = None       # Node:  left child Node or None
        self.right_node = None      # Node:  right child Node or None
        self.parent_node = None     # Node:  parent Node or None
        self.layout = None          # NodeLayout object: layout of this node

    # The @property decorator allows this to be called as .is_leaf rather than .is_leaf()
    @property
    def is_leaf(self):
        """ returns True iff this node is a leaf/tip of the tree """
        return self.left_node is None and self.right_node is None

    # The @property decorator allows this to be called as .is_root rather than .is_root()
    @property
    def is_root(self):
        """ returns True iff this node is the root of the tree """
        return self.parent_node is None

    def __repr__(self):
        return str(self.name)


    def get_layout(self):
        """ returns the four values listed in NodeLayout"""
        layout = self.layout
        return layout.row, layout.col, layout.x, layout.y

    def set_layout(self, row=None, col=None, x=None, y=None):
        """Sets the layout"""
        layout = self.layout
        layout.row = row if row else layout.row
        layout.col = col if col else layout.col
        layout.x = x if x else layout.x
        layout.y = y if y else layout.y

    def iter_track(self, track):
        """updates track number and returns previous track of host node"""
        if track == "H":
            self.layout.h_track = self.layout.h_track + 1
            return self.layout.h_track - 1
        
        if track == "UV":
            self.layout.upper_v_track += 1
            return self.layout.upper_v_track - 1
        
        if track == "LV":
            self.layout.lower_v_track += 1
            return self.layout.lower_v_track - 1
        
        


class NodeLayout:
    """ Defines node layout attributes for rendering """
    def __init__(self):
        self.row = None         # float: logical position of this Node in rendering

        # The self.col can be generated from a topological ordering of the temporal constraint graph
        self.col = None         # float: logical position of this Node in rendering
        self.x = None           # int: x-coordinate for rendering
        self.y = None           # int: y-coordinate for rendering
        self.upper_v_track = 0  # int: track number for upper vertical host edges
        self.lower_v_track = 0  # int: track number for lower vertical host edges
        self.h_track = 0        # int: track number for horizontal host edges


class Tree:
    """
    The Tree type defines a tree for use in rendering and other functions
    """
    def __init__(self):
        self.root_node = None       # Node:  Root Node of the Tree
        self.tree_type = None       # TreeType: HOST or PARASITE

    # The @property decorator allows this to be called as .leaf_list rather than .leaf_list()
    @property
    def leaf_list(self):
        """ Returns list of leaf Nodes from left to right. """
        return self._leaf_list_helper(self.root_node)

    def _leaf_list_helper(self, node):
        if node.is_leaf:
            return [node]
        list1 = self._leaf_list_helper(node.left_node)
        list2 = self._leaf_list_helper(node.right_node)
        list1.extend(list2)
        return list1

    # The @property decorator allows this to be called as .postorder_list
    # rather than .postorder_list()
    @property
    def postorder_list(self):
        """ returns list of all Nodes in postorder """
        return self._postorder_list_helper(self.root_node)

    def name_to_node_dict(self):
        """
        Returns a dictionary whose keys are names (strings) and values are the
        nodes whose .name is that string.
        Use case:  A parasite p finds its corresponding host h and then uses this
        dictionary to get the h's node which contains, among other things, its layout.
        This allows the parasite p to set its layout based on that of the host.
        """
        ntn_dict = {}
        self._name_to_node_dict_helper(self.root_node, ntn_dict)
        return ntn_dict

    def _name_to_node_dict_helper(self, node, ntn_dict):
        ntn_dict[node.name] = node
        if node.is_leaf:
            return
        self._name_to_node_dict_helper(node.left_node, ntn_dict)
        self._name_to_node_dict_helper(node.right_node, ntn_dict)

    def _postorder_list_helper(self, node):
        if node.is_leaf:
            return [node]
        list1 = self._postorder_list_helper(node.left_node)
        list2 = self._postorder_list_helper(node.right_node)
        list1.extend(list2)
        list1.append(node)
        return list1
