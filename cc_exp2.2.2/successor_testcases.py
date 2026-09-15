class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorderSuccessor(root, p):

    successor = None

    while root:

        if p.val >= root.val:
            root = root.right

        else:
            successor = root
            root = root.left

    return successor


# Creating BST
#
#          5
#        /   \
#       3     6
#      / \
#     2   4
#    /
#   1

root = TreeNode(5)

node3 = TreeNode(3)
node6 = TreeNode(6)
node2 = TreeNode(2)
node4 = TreeNode(4)
node1 = TreeNode(1)

root.left = node3
root.right = node6

node3.left = node2
node3.right = node4

node2.left = node1


# Test Case 1
p = node3
answer = inorderSuccessor(root, p)

print("Test Case 1")
print("p =", p.val)

if answer:
    print("Successor =", answer.val)
else:
    print("Successor = null")


# Test Case 2
p = node6
answer = inorderSuccessor(root, p)

print("\nTest Case 2")
print("p =", p.val)

if answer:
    print("Successor =", answer.val)
else:
    print("Successor = null")


# Test Case 3
p = node2
answer = inorderSuccessor(root, p)

print("\nTest Case 3")
print("p =", p.val)

if answer:
    print("Successor =", answer.val)
else:
    print("Successor = null")


# Test Case 4
p = node1
answer = inorderSuccessor(root, p)

print("\nTest Case 4")
print("p =", p.val)

if answer:
    print("Successor =", answer.val)
else:
    print("Successor = null")