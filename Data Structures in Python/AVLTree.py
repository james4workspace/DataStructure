import sys

class TreeNode(object):
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):

    def insertNode(self,root,key):
        """
        :param root:
        :param key:
        :return:
        Function to insert a node
        """
        # 先插入到leaf，然后再从leaf不断往上进行调整，所以是一个递归recursive的结构
        if not root:
            return TreeNode(key)
        elif key < root.key:
            # 进入左子树有可能导致左子树整体变化，所以要返回左子树
            root.left = self.insertNode(root.left, key)
        else:
            # 同理，进入右子树，有可能导致右子树整体变化，所以要返回右子树
            root.right = self.insertNode(root.right,key)
        # 这里假设我们抵达了leaf，此时root是leaf的parent_node
        # height 永远是根据左右子树最高的那一支来判断的
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        # update the balance factor and balance the tree
        # balance factor：这里是插入leaf后，parent_node的balance_factor变化，然后依次往上
        balance_factor = self.getBalance(root) #这里插入到底，上一层的节点就只是加1，不构成影响，再往上一层才构成影响。
        if balance_factor > 1:
            #即左子树太高
            if key < root.left.key:
                return self.rightRotate(root) # 提取中间值为新节点，把上下两层节点都变为子节点
            else:
                root.left = self.leftRotate(root.left) # 先调转取中间值
                return self.rightRotate(root)

        #同理处理右子树
        if balance_factor <-1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        # 如果该层符合AVL Tree要求，就往上传递
        return root

    def deleteNode(self,root,key):
        """
        Function to find the node to be deleted and remove it
        :param root: TreeNode
        :param key: int
        :return: TreeNode
        """
        if not root: #搜到leaf也依然没发现目标
            return root
        # 递归 -> 不断地通过二叉树分列来寻找目标
        if key < root.key:
            root.left = self.deleteNode(root.left,key)
        elif key > root.key:
            root.right = self.deleteNode(root.right,key)

        # 接下来是找到了目标
        else:
            # 单子树情况
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # 双子树情况 -> 获得右子树最小或左子树最大值，这里选择了右子树最小
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            # 这里需要把已经赋值给root的leaf节点数据删除
            root.right = self.deleteNode(root.right,temp.key)

        if root is None:
            return root

        # 下面与insert相同，都需要平衡一下平衡因子
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balance_factor = self.getBalance(root)

        # balance the tree
        # 左子树过高
        if balance_factor > 1:
            if self.getBalance(root.left) >=0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balance_factor < -1:
            if self.getBalance(root.right) <=0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def leftRotate(self,z):
        """
        Function to perform left rotation
        """
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y

    def rightRotate(self,z):
        """
        Function to perform right rotation
        :param z: TreeNode
        :return: TreeNode
        """
        y=z.left
        T2=y.right
        y.right = z
        z.left = T2
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def getHeight(self,root):
        """
        Function to get the height of the node
        :param root: TreeNode
        :return: int
        """
        if not root:
            return 0
        return root.height

    def getBalance(self,root):
        """
        Function to get balanced factor of the node
        :param root: TreeNode
        :return: int
        """
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self,root):
        """
        Function to get the min value of the right tree. 递归的方法
        """
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self,root):
        """
        先序遍历，本质上是DFS
        :param root: TreeNode
        :return: TreeNode
        """
        if not root:
            return
        print("{0} ".format(root.key),end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def printHelper(self,cur,indent,last):
        if cur!=None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent = "     "
            else:
                sys.stdout.write("L----")
                indent = "|    "
            print(cur.key)
            self.printHelper(cur.left,indent,False)
            self.printHelper(cur.right,indent,True)

#测试代码
if __name__ == '__main__':
    my_tree = AVLTree()
    root = None
    nums = [33, 13, 52, 9, 21, 61, 8, 11]
    for num in nums:
        root = my_tree.insertNode(root,num)
    my_tree.printHelper(root,"",True)
    key = 13
    root = my_tree.deleteNode(root,key)
    print("after deletion:")
    my_tree.printHelper(root,"",True)
