#!/usr/bin/env python
# encoding: utf-8

from binary_tree.binary_search_tree import BST

def test(args=None, BSTtype=BST):
    import random, sys
    if not args:
        args = sys.argv[1:]
    if not args:
        print 'usage: %s <number-of-random-items | item item item ...>' % \
                    sys.argv[0]
        sys.exit()
    elif len(args) == 1:
        items = (random.randrange(100) for i in xrange(int(args[0])))
    else:
        items = [int(i) for i in args]

    tree = BSTtype()
    for item in items:
        tree.insert(item)
    size = tree.size(tree.root)
    print "the size of tree is : %d" % size
    max = tree.find_min(tree.root)
    print "the min of the tree is: %s " % max.key
    tree.post_order(tree.root)
    print "以下是非递归后序遍历结果"
    tree.post_order_v2()


if __name__ == "__main__" :
    test()
