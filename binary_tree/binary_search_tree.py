#!/usr/bin/env python
# encoding: utf-8

#import os.path
#import sys
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from stack.stack import Stack
from queue.queue import Queue

#BST node defination
class BSTnode(object) :
    """
    Representation of a node in binary search tree.
    Has a left child,right child,and key value
    """
    def __init__(self,value) :
        """
        creat a new leaf with key value
        """
        self.key = value
        self.tag = 0         #用于后续遍历标记
        self.disconnect()
    def disconnect(self) :
        self.left = None
        self.right = None
        self.parent = None

class BST(object) :
    """
    simple binary search tree implementation.
    This BST supports insert,find,and delete-min operation
    Each tree contains some(possibly 0) BSTnode objects,representing nodes,
    and a pointer to the root
    """
    def __init__(self) :
        self.root = None
    def insert(self,value) :
        """
        Insert key value into this BST ,modifying it in place.
        """
        new_node = BSTnode(value)
        if self.root == None :             #如果树为空,则该节点为树的根节点
            self.root = new_node
        else :
            node = self.root
            while True :
                if value < node.key :      #比根节点小,进入左子树
                    if node.left is None :#左子树为空,则直接插入
                        node.left = new_node
                        new_node.parent = node
                        break
                    node = node.left      #继续查找左子树
                else :
                    if node.right is None :  #右子树为空,直接插入
                        node.right = new_node
                        new_node.parent = node
                        break
                    node = node.right        #继续查找右子树
        return new_node

    def find(self,value) :
        """
        Return the node for key value if is in the tree,or None otherwise.
        """
        node = self.root
        while node is not None :
            if value == node.key :    #节点值等于要查找的值,返回
                return node
            elif value < node.key :   #要查找的值小于节点的至,继续查找左子树
                node = node.left
            else :                    #要查找的值大于节点的至,继续查找右子树
                node = node.right
        return None

    def delete_min(self) :
        """
        Delete the minimum key(and return the old node containing it).
        """
        if self.root is None :
            return None,None
        else :
            #walk to the left most node
            node = self.root
            while node.left is not None :
                node = node.left
            #remove the node and promote its right subtree
            if node.parent is not None :
                node.parent.left = node.right
            else :
                #the root is the smallest
                self.root=node.right
            #如果该节点的右子树不空,则将其parent节点置为该节点的parent节点
            if node.right is not None :
                node.right.parent = node.parent
            parent = node.parent
            node.disconnect()
            return node,parent

    def next_larger(self,value) :
        """
        寻找value的后继,即下一个比value大的元素
        if right child not NIL, return minimum(right)
        else y = parent(x)
        while y not NIL and x = right(y)
            x = y; y = parent(y)
            return(y);
        """
        return 0

    def find_min(self,root=None) :
        """
        寻找最小值,以root为根节点的二叉搜索树的最小值
        """
        if root is None :
            return
        else :
            node = root
            while node.left is not None :
                node = node.left
            return node

    def find_max(self,root=None) :
        """
        寻找最大值,以root为根节点的二叉树的最大值
        """
        if root is None :
            return
        else :
            node = root
            while node.right is not None :
                node = node.right
            return node

    def delete(self,value) :
        """
        Delete the key value,if exist.return delete result.
        if value is not in the tree , return False,and print sth
        二叉搜索数的删除分三种情况进行处理:
            1.p为叶子节点,直接删除该节点,再修改其父节点指针.
            2.p为单支节点(即只有左子树或者右子树),让p的子树与父节点相连,删除p即可.
              注意,分根节点和非根节点.
            3.p的左子树和右子树均不空,找到p的后继(下一个比它大的)y,因为y一定没有左子树,所以可以删除y,
              并让y的父节点成为y的右子树的父节点,并用y的值替代p的值.
        """

        node = self.find(value)        #找到节点,find函数找到的是该节点
        if(node is not None) :
            #1.叶子节点
            if node.left is None and node.right is None :
                parent = node.parent
                if parent is None :    #根节点
                    self.root = None
                elif parent.left == node :
                    parent.left = None
                else :
                    parent.right = None
            #2.要删除的节点只有一个字节点
            elif node.right is None and node.left is not None :
                #要删除的节点只有一个leftchild
                parent = node.parent
                if parent is None :    #根节点
                    self.root = node.left
                elif parent.left == node:   #节点本身是leftnode
                    parent.left = node.left
                elif parent.right ==node :  #节点本身是rightnode
                    parent.right = node.left
            elif node.left is None and node.right is not None :
                #要删除的节点只有有一个:rightchild
                parent = node.parent
                if parent is None :    #根节点
                    self.root = node.right
                elif parent.left == node :   #节点本身是左节点
                    parent.left = node.right
                elif parent.right == node :  #节点本身是右节点
                    parent.right = node.right
            #3.要删除的节点有两个子节点
            else :
                #有两个节点,要删除有两个节点的节点,要用其中序后继节点来替代该节点
                #其中序后继节点也就是该节点右子树的元素最小值那个节点
                successor = self.get_successor(node)
                parent = node.parent
                if parent is None :    #要删除的是根节点
                    self.root = successor
                elif parent.left == node :  #节点本身是左节点
                    parent.left = successor
                elif parent.right == node :
                    parent.right = successor
                successor.left = node.left
            return node
        else :    #未找到节点
            return None

    def get_successor(self,del_node) :
        """
        获取要删除节点的中序后继节点,说白了也就是寻找该节点右子树的元素最小
        值的那个节点,用上面函数get_min()就可以的,此处为了更加清晰的理解,重新
        写一个函数
        """
        if del_node is None :
            return
        else :
            successor = del_node.right
        while successor.left is not None :
            successor = successor.left
        #如果后继不是该节点的右字节点,准备删除successor
        if del_node.right != successor :
            parent = successor.parent
            parent.left = successor.right
            successor.right = del_node.right

        return successor



    def pre_order(self,root=None) :
        """
        前序遍历,递归版
        """
        if root is None :
            return
        print "%s," % root.key
        self.pre_order(root.left)
        self.pre_order(root.right)

    def pre_order_v2(self) :
        """
        前序遍历,非递归版本
        思想:先让根进栈,只要栈不为空,就可以做弹出操作,每次弹出一个节点,记得将左右
        节点都进栈,右子树先进栈,这样可以保证右子树总在左子树下面
        """
        stack = Stack()    #初始化一个堆栈
        node = self.root
        if node is None :
            return         #空树
        while node is not None or not stack.empty() :
            while node is not None :
                stack.push(node)
                print "%s," % node.key
                node = node.left
            node = stack.pop()
            node = node.right

    def mid_order(self,root=None) :
        """
        中序遍历,递归版
        """
        if root is None :
            return
        self.mid_order(root.left)
        print "%s," % root.key
        self.mid_order(root.right)

    def mid_order_v2(self) :
        """
        中序遍历,非递归版
        """
        stack = Stack()
        node = self.root
        if node is None :
            return
        while node is not None or not stack.empty() :
            while node is not None :
                stack.push(node)
                node = node.left
            node = stack.pop()
            print "%s," % node.key
            node = node.right

    def post_order(self,root=None) :
        """
        后序遍历,递归版.
        """
        if root is None :
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print "%s," % root.key

    def post_order_v2(self) :
        """
        后序遍历,非递归版
        思路:对于任意节点p,将其入栈,然后沿其左子树一直往下搜索,知道搜索到没有左孩子节点,
        此时该节点出现在栈顶,但是此时不能将其出栈,因为右孩子还没有被访问,所以接下来按照
        相同的规则对右子树进行访问当访问完右子树时,该节点又一次出现在栈顶,此时可以访问
        并出栈,可以看出在每个节点都有两次出现在栈顶,只有在第二次出现时,才能访问它..因此
        需要多设置一个变量标识该节点是第几次访问.
        """
        stack = Stack()
        node = self.root
        if node is None :
            return
        else :
            while node is not None or not stack.empty() :
                while node is not None :#向左走到底
                    node.tag = 0        #设置访问标记,0表示第一次访问,1表示第二次访问
                    stack.push(node)
                    node = node.left
                node = stack.top()      #查看栈顶元素
                if node.tag == 0 :      #第一次访问时,转向同层的右节点
                    stack.pop()         #将栈顶元素出栈
                    node.tag = 1        #修改tag为1
                    stack.push(node)    #重新压栈
                    node = node.right   #访问该节点的右子树
                else :                  #第二次访问时
                    while node.tag == 1 :
                        node = stack.pop()
                        print "%s," % node.key
                        node = stack.top()
                    node = None         #将node设置None,直接访问右子树

    def level_order(self) :
        """
        层次遍历二叉树:按从顶向下,从左至右的逐层访问每个节点.
        层次遍历中需要用到队列.
        """
        queue = Queue()
        node = self.root
        if node is None :
            return
        else :
            queue.enqueue(node)         #根节点入队列
            while not queue.empty() :   #队列不空,对首元素出队
                node = queue.dequeue()
                print "%s," % node.key
                #左子树不空,则将左子树入队
                if node.left is not None :
                    queue.enqueue(node.left)
                #右子树不空,则将右子树入队
                if node.right is not None :
                    queue.enqueue(node.right)

    def size(self,root=None) :
        """
        return the number of elements of the tree.
        """
        if root is None :
            return 0
        else :
            return  self.size(root.left) + self.size(root.right) + 1

    def creat_binary_tree_with_pre_in(self, pre_order, in_order, pre_left,
            pre_right, in_left, in_right) :
        """
        根据二叉树的前序序列和中序序列构造一个二叉树.
        算法:首先根据给定的前序序列建立二叉树的根节点,根据中序遍历确定二叉树
        的左子树序列和右子树序列;然后再根据左子树的前序序列和中序序列递归地构建
        左子树,根据右子树的前序序列和中序序列递归地构建右子树.
        """
        self.root = BSTnode(pre_order[pre_left])
        mid = in_left
        while in_order[mid] != pre_order[pre_left] :
            #查找根节点在中序遍历序列中的位置
            mid += 1
        #生成左子树
        creat_binary_tree_with_pre_in(pre_order,in_order,pre_left+1,
                pre_left+mid-in_left,in_left,mid-1)
        #生成右子树
        creat_binary_tree_with_pre_in(pre_order,in_order,pre_left+mid-in_left+1,
                pre_right,mid+1,in_right)
        return self.root
        




