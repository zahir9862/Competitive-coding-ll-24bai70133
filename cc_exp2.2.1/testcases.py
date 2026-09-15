class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):

    if root is None or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


# Create Binary Tree

root = TreeNode(3)

node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)

root.left = node5
root.right = node1

node5.left = node6
node5.right = node2

node1.left = node0
node1.right = node8

node2.left = node7
node2.right = node4


# Test Case 1
p = node5
q = node1

answer = lowestCommonAncestor(root, p, q)

print("Test Case 1")
print("p =", p.val)
print("q =", q.val)
print("LCA =", answer.val)


# Test Case 2
p = node5
q = node4

answer = lowestCommonAncestor(root, p, q)

print("\nTest Case 2")
print("p =", p.val)
print("q =", q.val)
print("LCA =", answer.val)


# Test Case 3
p = node6
q = node8

answer = lowestCommonAncestor(root, p, q)

print("\nTest Case 3")
print("p =", p.val)
print("q =", q.val)
print("LCA =", answer.val)


# Test Case 4
p = node7
q = node4

answer = lowestCommonAncestor(root, p, q)

print("\nTest Case 4")
print("p =", p.val)
print("q =", q.val)
print("LCA =", answer.val)