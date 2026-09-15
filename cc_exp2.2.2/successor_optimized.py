class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorderSuccessor(root, p):

    successor = None

    # Search until root becomes None
    while root:

        # If p is greater than or equal to current node,
        # move to the right
        if p.val >= root.val:
            root = root.right

        else:
            # Current node is a possible successor
            successor = root

            # Try to find a smaller successor
            root = root.left

    return successor


# Creating the BST
#
#          5
#        /   \
#       3     6
#      / \
#     2   4
#    /
#   1

root = TreeNode(5)

root.left = TreeNode(3)
root.right = TreeNode(6)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.left.left.left = TreeNode(1)


# p = 3
p = root.left


answer = inorderSuccessor(root, p)


print("Optimized Approach")
print("p =", p.val)

if answer is not None:
    print("Inorder Successor =", answer.val)
else:
    print("Inorder Successor = null")