class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root, order):

    if root is None:
        return

    # Visit left subtree
    inorder(root.left, order)

    # Store current node
    order.append(root)

    # Visit right subtree
    inorder(root.right, order)


def inorderSuccessor(root, p):

    order = []

    # Perform inorder traversal
    inorder(root, order)

    # Find p and return the next node
    for i in range(len(order)):

        if order[i] == p:

            if i + 1 < len(order):
                return order[i + 1]

            return None

    return None


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


print("Brute Force Approach")
print("p =", p.val)

if answer is not None:
    print("Inorder Successor =", answer.val)
else:
    print("Inorder Successor = null")