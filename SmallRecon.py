from RenderStarter import Node, Event, ReconMap, EventType
### Host Tree

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

### Parasite Tree

### Reconciliation

R = ReconMap()
Event1 = Event("7", "4", EventType.TIPTIP)
Event2 = Event("9", "5", EventType.TIPTIP)
Event3 = Event("10", "3", EventType.TIPTIP)
Event4 = Event("pInternal", "5", EventType.TRANSFER)


