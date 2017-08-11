from enum import Enum, auto


class TreeNode:
    def __init__(self, val=None):
        if val is not None:
            self.key = val
        self.right = None
        self.left = None
        self.p = None


class Color(Enum):
    RED = auto()
    BLACK = auto()


class RB_TreeNode(TreeNode):
    def __init__(self, val=None):
        super().__init__(val)
        self.__color = None

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


class Nil(RB_TreeNode):
    def __init__(self):
        super().__init__()
        self.color = Color.BLACK

class OS_TreeNode(RB_TreeNode):
    def __init__(self, val=None):
        super().__init__(val)
        self.size = 0

class OS_Nil(Nil):
    def __init__(self):
        super().__init__()
        self.size = 0
