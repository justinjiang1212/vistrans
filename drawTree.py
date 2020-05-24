import RenderStarter


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

    #sets logical row values for leaves in the order they appear in host_tree.leaves
    logical_row_counter = 0
    for leaf in host_tree.leaves:
        leaf.logicalRow = logical_row_counter
        logical_row_counter += 1
    
    #helper function to assign row values, postorder traversal
    calcLogRow(host_tree.rootNode)

    
def calcLogRow(node):
    """takes a Node, usually the root of the tree, and traverses the tree until it finds nodes with row values, usually leaves"""

    #if both children of node have a logical row value, we can calculate the logical row value of node
    if node.rightChild.logicalRow is not None and node.leftChild.logicalRow is not None:
        node.logicalRow = ((node.rightChild.logicalRow+node.leftChild.logicalRow)/2)
        return

    #recursively calculate logical row values of the right subtree 
    if node.rightChild.logicalRow == None:
        calcLogRow(node.rightChild)
    #recursively calculate logical row values of the left subtree
    if node.leftChild.logicalRow == None:
        calcLogRow(node.leftChild)
    
    #finally, calculate logical row value of node using just-calculated children values
    node.logicalRow = ((node.rightChild.logicalRow+node.leftChild.logicalRow)/2)


    ### Here's what needs to happen here:
    ### The logicalCol of each Node is just its order.
    ### The logicalRows are computed as follows:
    ###     1.  For leaves, we iterate through the list of leaves for the tree from left (top)
    ###         to right (bottom) and make the logicalRow the indices 0 to numLeaves-1
    ###     2.  Moving up the tree, the logical row of a node is the midpoint (a float) of 
    ###         the logical rows of its two children.


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




root = Node("root")
root.root = True
root.order = 0

internal1 = Node("internal") # parent of 4 and 5
internal1.is_leaf = False
internal1.parent = root
internal1.order = 2

leaf4 = Node("4")
leaf4.is_leaf = True
leaf4.parent = internal1
leaf4.order = 4

leaf5 = Node("5")
leaf5.is_leaf = True
leaf5.parent = internal1
leaf5.order = 4

leaf3 = Node("3")
leaf3.is_leaf = True
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