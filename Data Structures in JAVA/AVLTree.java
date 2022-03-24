package DataStructure;

import java.util.Scanner;
public class AVLTree {
    public static class TreeNode{
        int key, height;
        TreeNode left,right;
        public TreeNode(int key){
            this.key = key;
            this.height = 1;
        }
    }

    TreeNode root;

    private void insert(int key){
        if(root==null){
            root = new TreeNode(key);
            return;
        }
        insertNode(key,root);
    }
    private TreeNode insertNode(int key, TreeNode current){
        //先插入到leaf，然后再从leaf不断往上进行调整，所以是一个递归recursive的结构
        if(current==null){
            return new TreeNode(key);
        }
        if(key<current.key){
            // 进入左子树有可能导致左子树整体变化，所以要返回左子树
            current.left = insertNode(key,current.left);
        }
        else if(key>current.key){
            // 进入右子树有可能导致右子树整体变化，所以要返回右子树
            current.right = insertNode(key,current.right);
        }
        // 以上会一路跑到leaf，此时current就是leaf的parent node
        // height永远根据左右子树最高的那一支来判断
        current.height=1+Math.max(getHeight(current.left),getHeight(current.right));

        // update the balance factor and balance the tree
        // balance factor: 这里是插入leaf后，parent node 的balanceFactor变化，然后依次往上
        int balanceFactor = getBalance(current);//这里插入到底，上一层的节点就只是加1，不构成影响，再往上一层才构成影响。
        if(balanceFactor>1){
            //即左子树过高
            if(key<current.left.key){
                //提取中间值为新节点，将另外两个节点变为子节点
                return rightRotate(current);
            }
            else{
                current.left = leftRotate(current.left);//先调换中间值
                return rightRotate(current);
            }
        }
        // 同理处理右子树
        else if(balanceFactor<-1){
            if(key>current.right.key){
                return leftRotate(current);
            }
            else{
                current.right = rightRotate(current.right);
                return leftRotate(current);
            }
        }
        // 最后调整结束，或者该层符合AVL Tree要求，就往上传递
        return current;
    }

    private void delete(int key){
        if(root==null){
            return;
        }
        deleteNode(key,root);
    }

    private TreeNode deleteNode(int key, TreeNode current){
        if(current==null){//搜到leaf也没发现目标
            return current;
        }
        //通过递归不断寻找目标
        if(key<current.key){
            current.left = deleteNode(key,current.left);
        }
        else if(key>current.key){
            current.right = deleteNode(key,current.right);
        }

        //接下来是找到目标该怎么处理
        else{
            //单子树情况
            if(current.left ==null){
                TreeNode temp=current.right;
                current = null;
                return temp;
            }
            else if(current.right == null){
                TreeNode temp=current.left;
                current = null;
                return temp;
            }
            //双子树情况  -> 获得右子树最小或左子树最大值，这里选择了右子树最小
            TreeNode temp = getMinKeyNode(current.right);
            current.key=temp.key;
            // 这里需要把已经赋值给root的leaf节点数据删除
            current.right = deleteNode(temp.key,current.right);
        }
        // 接下来开始平衡因子的计算及树的调整
        current.height=1+Math.max(getHeight(current.left),getHeight(current.right));
        int balanceFactor = getBalance(current);

        // 接下来同insert，开始平衡树
        if(balanceFactor>1){
            //即左子树过高
            if(key<current.left.key){
                //提取中间值为新节点，将另外两个节点变为子节点
                return rightRotate(current);
            }
            else{
                current.left = leftRotate(current.left);//先调换中间值
                return rightRotate(current);
            }
        }
        // 同理处理右子树
        else if(balanceFactor<-1){
            if(key>current.right.key){
                return leftRotate(current);
            }
            else{
                current.right = rightRotate(current.right);
                return leftRotate(current);
            }
        }
        // 最后调整结束，或者该层符合AVL Tree要求，就往上传递
        return current;
    }

    private TreeNode leftRotate(TreeNode z){
        TreeNode y= z.right;
        TreeNode T2=y.left;
        y.left=z;
        z.right=T2;
        z.height=1+Math.max(getHeight(z.left),getHeight(z.right));
        y.height=1+Math.max(getHeight(y.left),getHeight(y.right));
        return y;
    }

    private TreeNode rightRotate(TreeNode z){
        TreeNode y=z.left;
        TreeNode T2=y.right;
        y.right=z;
        z.left=T2;
        z.height=1+Math.max(getHeight(z.left),getHeight(z.right));
        y.height=1+Math.max(getHeight(y.left),getHeight(y.right));
        return y;
    }


    private int getBalance(TreeNode current){
        if(current==null){
            return 0;
        }
        return getHeight(current.left)-getHeight(current.right);
    }

    private int getHeight(TreeNode current) {
        if(current==null){
            return 0;
        }
        return current.height;
    }

    private TreeNode getMinKeyNode(TreeNode current){
        /*通过递归获得最小值的节点*/
        if(current==null||current.left==null){
            return current;
        }
        return getMinKeyNode(current.left);
    }

    private void preOrderTraversal(){
        /*先序遍历，本质上是DFS*/
        if(root==null){
            System.out.println("root is null!!!");
            return;
        }
        preOrder(root);
    }
    private void preOrder(TreeNode cur){
        if(cur==null){
            return;
        }
        System.out.println(cur.key+" -> ");
        preOrder(cur.left);
        preOrder(cur.right);
    }

    public static void main(String[] args){
        Scanner obj = new Scanner(System.in);
        AVLTree avl = new AVLTree();
        System.out.println("please enter the key with \' \' as splitting symbol: ");
        while(obj.hasNextInt()){
            int key = obj.nextInt();
            avl.insert(key);
        }
        avl.preOrderTraversal();
        avl.delete(4);
        avl.delete(9);
        System.out.println("after deletion:");
        avl.preOrderTraversal();
    }
}
