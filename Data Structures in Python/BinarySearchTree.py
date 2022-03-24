
class TreeNode:
    def __init__(self,key):
        self.left = None
        self.right= None
        self.val  = key

class BinarySearchTree:
    def __init__(self):
        self.root = None # 根节点
        self.count = -1 # 遍历计算顺序序号

    def get(self,key):
        """
        查询功能
        """
        cur = self.root

        # recursive loop
        while cur!= None and cur.val !=key:
            if key<cur.val:
                cur = cur.left
            elif key > cur.val:
                cur = cur.right

        # Verdict on whether cur exists
        if cur is not None:
            return cur
        else:
            return None

    def insert(self,key):
        """
        whether you can insert a new kye into the tree:return
        """
        if self.root is None:
            self.root = TreeNode(key)
            return
        else:
            cur = self.root
            parent = None
            while True:
                parent = cur
                if key < parent.val:
                    cur = parent.left
                    if cur is None:
                        parent.left = TreeNode(key)
                        return
                elif key>parent.val:
                    cur = parent.right
                    if cur is None:
                        parent.right = TreeNode(key)
                        return
                else:
                    return # BST 不允许相同的值存在

    def delete(self,key):
        """
        三种情况：
            1.删除Leaf
            2.删除只有一个Child的节点
            3.删除有两个Child的节点
        """
        parent = self.root
        cur = self.root
        isLeftChild = False # 判断要删除节点与父节点的关系
        while cur != None and cur.val != key:
            parent = cur
            if key < cur.val:
                isLeftChild = True
                cur = cur.left
            elif key > cur.val:
                isLeftChild = False
                cur = cur.right

        if cur is None:#如果不存在该key
            return False

        # case 1: 没有子节点的Leaf
        if cur.left is None and cur.right is None:
            if cur == self.root:#如果是头节点，且只有一个元素
                self.root = None
            elif isLeftChild == True:
                parent.left = None
            else:
                parent.right = None

        # case 2: 如果节点只有一个子节点
        elif cur.right is None: #只有左子树，没有右子树
            if cur == self.root:
                self.root = cur.left
            elif isLeftChild == True:
                parent.left = cur.left
            elif isLeftChild == False:
                parent.right = cur.left

        elif cur.left is None:  # 只有右子树，没有左子树
            if cur == self.root:
                self.root = cur.right
            elif isLeftChild == True:
                parent.left = cur.right
            elif isLeftChild == False:
                parent.right = cur.right

        # case 3： 如果节点有两个子树 cur.left is not None and cur.right is not None
        else:
            #这里我们找右子树最小节点来替代要删除的点
            successor = self.getSuccessor(cur) #找右子树最小的节点，successor即胜出的最小节点，也把关系都清理了
            if cur == self.root:
                self.root = successor
            elif isLeftChild == True:
                parent.left = successor
            else:
                parent.right = successor

        return True


    def getSuccessor(self,node:TreeNode):
        """:arg
        找右子树最小值
        """
        successor = None #最后替代的节点
        successor_parent = None
        cur = node.right
        while cur!=None:
            successor_parent = successor
            successor = cur
            cur = cur.left

        if successor!=node.right:
            successor_parent.left = successor.right
            successor.right = node.right

        successor.left = node.left

        return successor

    def traversal(self,type=1):
        self.count = -1
        cur = self.root
        if type ==1:#前序遍历
            self.pre_orderTraversal(cur)
        elif type ==2:#中序遍历
            self.interim_orderTraversal(cur)
        elif type ==3:#后序遍历
            self.post_orderTraversal(cur)

    def pre_orderTraversal(self,cur):
        """
        前序遍历
        """
        if cur is None:
            return
        else:
            self.count +=1
            print("No {a} of Traversal is: {b}\n".format(a=self.count,b=cur.val))
            self.pre_orderTraversal(cur.left)
            self.pre_orderTraversal(cur.right)


    def interim_orderTraversal(self,cur):
        """
        中序遍历
        """
        if cur is None:
            return
        else:
            self.count +=1
            self.pre_orderTraversal(cur.left)
            print("No {a} of Traversal is: {b}\n".format(a=self.count,b=cur.val))
            self.pre_orderTraversal(cur.right)

    def post_orderTraversal(self,cur):
        """
        后序遍历
        """
        if cur is None:
            return
        else:
            self.count +=1
            self.pre_orderTraversal(cur.left)
            self.pre_orderTraversal(cur.right)
            print("No {a} of Traversal is: {b}\n".format(a=self.count, b=cur.val))


if __name__ =="__main__":
    list_insert = [2,1,5,4,-3,43,22,5,8,21,16]
    bst = BinarySearchTree()
    for each in list_insert:
        bst.insert(each)

    print(bst.get(21).val)
    bst.traversal()
    bst.delete(16)
    bst.traversal(type=3)