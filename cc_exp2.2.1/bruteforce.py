class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def findPath(root, target, path):

    if root is None:
        return False

    path.append(root)

    if root == target:
        return True

    if findPath(root.left, target, path):
        return True

    if findPath(root.right, target, path):
        return True

    path.pop()
    return False


def lowestCommonAncestor(root, p, q):

    path1 = []
    path2 = []

    findPath(root, p, path1)
    findPath(root, q, path2)

    i = 0

    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1

    return path1[i - 1]


# Creating the Binary Tree
#
#          3
#        /   \
#       5     1
#      / \   / \
#     6   2 0   8
#        / \
#       7   4

root = TreeNode(3)

root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)


# p = 5, q = 1
p = root.left
q = root.right


answer = lowestCommonAncestor(root, p, q)

print("Brute Force Approach")
print("p =", p.val)
print("q =", q.val)
print("Lowest Common Ancestor =", answer.val)