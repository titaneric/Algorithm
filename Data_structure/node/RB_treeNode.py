from enum import Enum, auto
from node.treeNode import TreeNode


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
