package DataStructure;

import java.util.Scanner;

enum NodeType{
    UNKNOWN, NO_CHILD, ONE_CHILD,DOUBLE_CHILDREN
}
enum OrderType{
    PRE_ORDER,INTERIM_ORDER,POST_ORDER
}
public class BinarySearchTree {
    static class TreeNode{
        //建立节点
        protected int key;
        protected String value;
        protected TreeNode left;
        protected TreeNode right;
        public TreeNode(int key, String value){
            this.key = key;
            this.value = value;
            this.left = null;
            this.right = null;
        }
    }

    private TreeNode root;//记录根节点
    private int count;

    public void insert(int key,String value){
        /*插入函数*/
        if(root==null){
            root = new TreeNode(key,value);
            return;
        }
        TreeNode current = root;
        TreeNode parent = null;
        while(true){
            parent = current;
            if(key<parent.key){
                current = parent.left;
                if(current == null){
                    parent.left = new TreeNode(key,value);
                    return;
                }
            }
            else if(key>parent.key){
                current = parent.right;
                if(current==null){
                    parent.right = new TreeNode(key,value);
                    return;
                }
            }
            else{
                return;//BST doesn't allow nodes with same key
            }
        }
    }

    public TreeNode get(int key){
        /*查询方法*/
        TreeNode current = root;
        while(current!=null && current.key!=key){
            if(key<current.key){
                current = current.left;
            }
            else{
                current = current.right;
            }
        }
        return current == null ? null:current;
    }

    public boolean delete(int key){
        TreeNode parent = root;
        TreeNode current = root;
        boolean isLeftChild = false;
        while(current!=null && current.key!=key){
            //先找到该节点
            parent = current;
            if(key<current.key){
                //在左节点
                isLeftChild=true;
                current =current.left;
            }
            else{
                //在右节点
                isLeftChild=false;
                current = current.right;
            }
        }
        if(current==null){
            return false;//没有该节点
        }
        // case 1: if node to be deleted has no children
        NodeType nodeType = NodeType.UNKNOWN;
        if(current.left==null && current.right==null){
            nodeType = NodeType.NO_CHILD;
        }
        // case 2: if node to be deleted has onley one child
        else if((current.right==null)^(current.left==null)){
            // ^ 表示相异
            nodeType = NodeType.ONE_CHILD;
        }
        // case 3: if node to be deleted has double children
        else{
            nodeType = NodeType.DOUBLE_CHILDREN;
        }
        switch(nodeType){
            case NO_CHILD:
                if(current==root){
                    root = null;//只有一个节点
                }
                else if(isLeftChild){
                    //如果是左节点
                    parent.left =null;
                }else if(isLeftChild==false){
                    parent.right =null;
                }
                break;
            case ONE_CHILD:
                if(current==root){
                    if(isLeftChild){
                        root = current.left;
                    }
                    else{
                        root = current.right;
                    }
                }
                else if(isLeftChild){
                    parent.left = current.left;
                }
                else{
                    parent.right = current.right;
                }
                break;
            case DOUBLE_CHILDREN:
                TreeNode successor = getSuccessor(current);
                if(current == root){
                    root = successor;
                }
                else if(isLeftChild){
                    parent.left = successor;
                }else{
                    parent.right = successor;
                }
                successor.left = current.left;
                break;
            default:
                //以上都没选到
                break;
        }
        return true;
    }

    private TreeNode getSuccessor(TreeNode node){
        /* 找到右子树最小值，则需要在右子树下一直往左找，找左子节点leaf node
        * */
        TreeNode successor = null;//最后替代的节点
        TreeNode successorParent = null;//遍历记录父节点
        TreeNode current = node.right;//进入右子树
        while(current!=null){
            successorParent=successor;
            successor=current;
            current=current.left;
        }
        if(successor!=node.right){
            successorParent.left=successor.right;
            successor.right = node.right;
        }
        return successor;
    }

    private void traversal(OrderType _type){
        /*这里开始选择何种遍历方式进行遍历*/
        count =0;
        TreeNode current = root;
        switch(_type){
            case PRE_ORDER:
                System.out.println("preOrderTraversal below:");
                preOrderTraversal(current);
                break;
            case INTERIM_ORDER:
                System.out.println("interimOrderTraversal below:");
                interimOrderTraversal(current);
                break;
            case POST_ORDER:
                System.out.println("postOrderTraversal below:");
                postOrderTraversal(current);
                break;
        }
    }

    private void preOrderTraversal(TreeNode current){
        if(current==null){
            return;
        }
        count+=1;
        System.out.println("No "+count+" of Traversal is: key: "+current.key+" value: "+current.value);
        preOrderTraversal(current.left);
        preOrderTraversal(current.right);
    }

    private void interimOrderTraversal(TreeNode current){
        if(current==null){
            return;
        }
        count+=1;
        interimOrderTraversal(current.left);
        System.out.println("No "+count+" of Traversal is: key: "+current.key+" value: "+current.value);
        interimOrderTraversal(current.right);
    }

    private void postOrderTraversal(TreeNode current){
        if(current==null){
            return;
        }
        count+=1;
        postOrderTraversal(current.left);
        postOrderTraversal(current.right);
        System.out.println("No "+count+" of Traversal is: key: "+current.key+" value: "+current.value);
    }


    public static void main(String[] args){
        Scanner obj = new Scanner(System.in);
        System.out.println("pleae enter the node with format: int key,String value \\n:");
        BinarySearchTree bst = new BinarySearchTree();
        while(obj.hasNextLine()){
            String strInput = obj.nextLine();
            String[] listInput = strInput.split(",");
            int key = Integer.parseInt(listInput[0]);
            String value = listInput[1];
            bst.insert(key, value);
        }
        bst.traversal(OrderType.PRE_ORDER);
        bst.delete(4);
        bst.delete(28);
        bst.traversal(OrderType.PRE_ORDER);
    }
}
