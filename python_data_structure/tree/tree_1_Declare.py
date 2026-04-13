'''
二元樹需要兩個指標，一個指向左子樹，另一個指向右子樹，
若子樹是空的時候設定為NULL，NULL就是空指標，程式會以數值0取代，
在二元樹走訪時遇到NULL，就不能再走訪下去，必須倒退回去
'''
class node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    def setLeft(self, left):
        self.left = left
    def setRight(self, right):
        self.right = right