# Tree.py
# Defines classes related to host and parasite nodes and trees

from enum import Enum

class TreeType(Enum):
    HOST = 1
    PARASITE = 2

# The Node class defines a node of a tree
class Node:
    def __init__(self, name):
        self.name = name            # String; name of this host or parasite
        self.left_node = None       # Node:  left child Node or None
        self.right_node = None      # Node:  right child Node or None
        self.parent_node = None     # Node:  parent Node or None
        self.layout = None          # NodeLayout object: layout of this node

    # The @property decorator allows this to be called as .is_leaf rather than .is_leaf()
    @property
    def is_leaf(self):
        return self.left_node is None and self.right_node is None

    # The @property decorator allows this to be called as .is_root rather than .is_root()
    @property
    def is_root(self):
        return self.parent_node is None

    def __repr__(self):
        return str(self.name)

    def get_layout(self):
        row = self.layout.row
        col = self.layout.col
        x = self.layout.x
        y = self.layout.y
        return row, col, x, y

    def set_layout(self, row=None, col=None, x=None, y=None):
        self.layout.row = row if row else self.layout.row
        self.layout.col = col if col else self.layout.col
        self.layout.x = x if x else self.layout.x
        self.layout.y = y if y else self.layout.y
    
class NodeLayout:
    def __init__(self):
        self.row = None         # float: logical position of this Node in rendering

        # The self.col can be generated from a topological ordering of the temporal constraint graph
        self.col = None         # float: logical position of this Node in rendering 
 
        self.x = None           # int: x-coordinate for rendering
        self.y = None           # int: y-coordinate for rendering

# The Tree type defines a tree
class Tree:
    def __init__(self):
        self.root_node = None       # Node:  Root Node of the Tree 
        self.tree_type = None       # TreeType: HOST or PARASITE 

    # The @property decorator allows this to be called as .leaf_list rather than .leaf_list()
    @property
    def leaf_list(self):
        """ Returns list of leaf Nodes from left to right. """
        return self._leaf_list_helper(self.root_node)

    def _leaf_list_helper(self, node):
        if node.is_leaf: return [node]
        else:
            list1 = self._leaf_list_helper(node.left_node)
            list2 = self._leaf_list_helper(node.right_node)
            list1.extend(list2)
            return list1


    # The @property decorator allows this to be called as .postorder_list rather than .postorder_list()    
    @property
    def postorder_list(self):
        """ returns list of all Nodes in postorder """
        return self._postorder_list_helper(self.root_node)

    def name_to_node_dict(self):
        """ 
        Returns a dictionary whose keys are names (strings) and values are the the nodes whose .name is that string. 
        Use case:  A parasite p finds its corresponding host h and then uses this dictionary to 
        get the h's node which contains, among other things, its layout.  This allows the parasite p to set
        its layout based on that of the host. 
        """
        D = {}
        self._name_to_node_dict_helper(self.root_node, D)
        return D

    def _name_to_node_dict_helper(self, node, D):
        D[node.name] = node
        if node.is_leaf: return
        else:
            self._name_to_node_dict_helper(node.left_node, D)
            self._name_to_node_dict_helper(node.right_node, D)

    def _postorder_list_helper(self, node):
        if node.is_leaf: return [node]
        else:
            list1 = self._postorder_list_helper(node.left_node)
            list2 = self._postorder_list_helper(node.right_node)
            list1.extend(list2)
            list1.append(node)
            return list1


    
        



