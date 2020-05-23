from enum import Enum

# You should assume that you'll get the following from eMPRess:
# 1. Host tree:  A Tree object with all of its attributes already populated
# 2. Parasite tree:  A Tree object with all of its attributres already populated
# HOWEVER, the Node objects in these trees will NOT have their logicalRow/logicalCol
# nor their xcoord/ycoord computed yet.

# Type of a tree:  either a host tree or a parasite tree
class TreeType(Enum):
    HOST = 1
    PARASITE = 2

# Type of an event
class EventType(Enum):
    COSPECIATION = 0
    DUPLICATION = 1
    TRANSFER = 2
    LOSS = 3
    TIPTIP = 4  # Tip to Tip association; aka contemporaneous leaf association

# The Node class defines a node of a tree
class Node:
    def __init__(self, name=None):
        self.name = name        # String; name of this host or parasite
        self.root = False       # Boolean:  True iff this is the root
        self.leaf = False       # Boolean: True iff this is a leaf
        self.parent = None      # Node: parent of this Node
        self.leftChild = None   # Node: first child of this Node
        self.rightChild = None  # Node: second child of this Node
        self.order = None       # Int: order of this node; root will be at 0, 
                                #   all leaves share largest value
        self.logicalRow = None  # Float: logical position of this Node in rendering
        self.logicalCol = None  # Float: logical position of thss Node in rendering
                                #   Most likely, logicalCol = order, so this field is redundant 
        self.xcoord = None      # Int:  x-coordinate for rendering
        self.ycoord = None      # Int:  y-coordinate for rendering

# The Tree type defines a tree
class Tree:
    def __init__(self):
        self.rootNode = None    # Node:  Root Node of the Tree
        self.allNodes = None    # List of Nodes:  All Nodes in the tree
        self.leaves = None      # List of Nodes:  List of leaves in tree from left (top) to right (bottom)
        self.nameToNode = None  # Dictionary of Node name (string) to Node
        self.type = None        # TreeType (TreeType.HOST or TreeType.PARASITE)

    def updateLeaves(self):
        """ Sets self.leaves to the list of all leaf Nodes. """
        self.leaves = self.postOrder(self.rootNode)

    
    def postOrder(self, node):
        if node.leaf == True:
            return [node]
        
        else:
            leftSubtreeLeaves = self.postOrder(node.leftChild)
            rightSubtreeLeaves = self.postOrder(node.rightChild)
            return leftSubtreeLeaves + rightSubtreeLeaves
        
        

    




# An Event keeps the name of the parasite (a string; this is redundant 
# since it's just the key), the name of the host to which that parasite is mapped in the
# reconciliation (a string), the type of that event (an EventType), and the frequency of this 
# Event in MPR space.
class Event:
    def __init__(self, parasite=None, host=None, etype=None, freq=0):
        self.parsiteName = parasite # String:  Name of parasite (same as key value in ReconMap)
        self.hostName = host        # String:  Name of host
        self.eventType = etype      # EventType
        self.frequency = freq       # Float:  Frequency (support value) for this event

# The ReconMap is a representation of a DTL reconciliation.
# The primary component is a self.recon which is a dictionary which maps parasite names (strings)
# to Events.  
class ReconMap:
    def __init__(self):
        self.recon = None       # Dictionary:  Keys are parasite names (strings) and values 
                                # are Events

# This is the starter code for rendering; it should go in a different file from the class definitions!

def computetHostNodeLogicalPositions(host_tree):
    """ 
    Sets the logicalRow and logicalCol values of each Node in host_tree.
    Assumes that each host Node has its order set already and this function
    uses those values and structure of the tree to set the logicalRow and logicalCol
    :param host_tree:  A Tree object representing the host tree
    :return None
    """
    #set logical cols
    for node in host_tree.allNodes:
        node.logicalCol = node.order
    
    #helper function to sort leaves by clades

    for leaf in host_tree.allNodes:
        ###finish code later
        pass
    


    ### Here's what needs to happen here:
    ### The logicalCol of each Node is just its order.
    ### The logicalRows are computed as follows:
    ###     1.  For leaves, we iterate through the list of leaves for the tree from left (top)
    ###         to right (bottom) and make the logicalRow the indices 0 to numLeaves-1
    ###     2.  Moving up the tree, the logical row of a node is the midpoint (a float) of 
    ###         the logical rows of its two children.


def sort_leaves(tree):
    """"sorts leaves of host tree by genetic distance"""
    return 


def computeParasiteNodeLogicalPositions(parasite_tree, host_tree, recon_map):
    """
    Sets the logicalRow and logicalCol values of each Node in parasite_tree.
    Assumes that each parasite Node has its order set already and this function
    uses those values and the reconfiguration to set logicalRow and logicalCol
    :param parasite_tree:  A Tree object representing the parasite tree
    :param host_tree:  A Tree object representing the host tree
    :param recon_map: A ReconMap object with the reconciliation
    :return None
    """

    ### Here's what needs to happen here:
    ### The logicalCol of each Node is just its order.
    ### The logicalRows are computed as follows:
    ###     1.  For each node v of the parasite tree, its logicalRow is the same
    ###         as the logicalRow of the host node to which it is mapped.  That's it!

def computeHostNodeActualPositions(host_tree, x_min, x_max, y_min, y_max):
    """
    Sets the xcoord and ycoord for rendering the Node host tree
    :param host_tree:  A Tree object representing the host tree
    :parem x_min: Integer; minimum x-coordinate for tree rendering
    :param x_max: Integer; maximum y-coordinate for tree rendering
    :param y_min: Integer; minimum y-coordinate for tree rendering
    :param y_max: Integer; maximum y-coordinate for tree rendering
    :return: None
    """


def computeParasiteNodeActualPositions(parasite_tree, x_min, x_max, y_min, y_max):
    """
    Sets the xcoord and ycoord for rendering the Node of the parasite tree
    This will require some additional input arguments to indicate offsets
    such as how far below a host edge we draw the parasite node, etc.
    :param host_tree:  A Tree object representing the host tree
    :parem x_min: Integer; minimum x-coordinate for tree rendering
    :param x_max: Integer; maximum y-coordinate for tree rendering
    :param y_min: Integer; minimum y-coordinate for tree rendering
    :param y_max: Integer; maximum y-coordinate for tree rendering
    :return: None
    """


def renderHostTree(host_tree):
    """
    Renders the host tree using the drawing commands.
    :param host_tree:  A Tree object with xcoord, ycoords already established for every
        Node in that tree.
    :return:  None
    """
    
def renderParasiteTree(parasite_tree, host_tree, recon_map):
    """
    Renders the parasite tree and events using the drawing commands.
    Each parasite node is color-coded according to its event type.
    :param parasite_tree:  A Tree object with xcoord, ycoords already established for every
        Node in that tree.
    :param parasite_tree:  A Tree object with xcoord, ycoords already established for every
        Node in that tree.
    :recon_map: A ReconMap object specifying the reconciliation
    :return:  None
    """
    ### Hint:  I think that it's easiest to render backwards, starting at the leaves.  
    ### For each parasite node, find
    ### it's parent.  Then, draw the path from the parent node to the current parasite node.
    ### This is useful since each node has just one parent.  This makes it much easier to 
    ### draw the edges of the parasite tree and, in particular, to draw the losses correctly.




#host tree for testing
root = Node("root")
root.root = True
root.order = 0

internal1 = Node("internal") # parent of 4 and 5
internal1.leaf = False
internal1.parent = root
internal1.order = 2

leaf4 = Node("4")
leaf4.leaf = True
leaf4.parent = internal1
leaf4.order = 4

leaf5 = Node("5")
leaf5.leaf = True
leaf5.parent = internal1
leaf5.order = 4

leaf3 = Node("3")
leaf3.leaf = True
leaf3.parent = root
leaf3.order = 4

root.leftChild = internal1
root.rightChild = leaf3
internal1.leftChild = leaf4
internal1.rightChild = leaf5

hostTree = Tree()
hostTree.rootNode = root
hostTree.allNodes = [root, internal1, leaf4, leaf5, leaf3]
hostTree.type = 1