from node.RB_treeNode import RB_TreeNode, Nil

class OS_TreeNode(RB_TreeNode):
    def __init__(self, val=None):
        super().__init__(val)
        self.size = 0


class OS_Nil(Nil):
    def __init__(self):
        super().__init__()
        self.size = 0