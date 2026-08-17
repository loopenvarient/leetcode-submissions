# 94. Binary Tree Inorder Traversal

- **Difficulty:** Easy  
- **Link:** https://leetcode.com/problems/binary-tree-inorder-traversal/

## Problem Summary
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Inorder traversal visits nodes in this order:
1. Left subtree
2. Current node
3. Right subtree

## Examples

### Example 1
- **Input:** `root = [1,null,2,3]`
- **Output:** `[1,3,2]`

### Example 2
- **Input:** `root = [1,2,3,4,5,null,8,null,null,6,7,9]`
- **Output:** `[4,2,6,5,7,1,3,9,8]`

### Example 3
- **Input:** `root = []`
- **Output:** `[]`

### Example 4
- **Input:** `root = [1]`
- **Output:** `[1]`

## Constraints
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Approach (Recursive DFS)
Use a helper function that recursively traverses:
- Left child
- Current node (append value to result)
- Right child

If the current node is `None`, return immediately.

## Complexity
- **Time:** `O(n)` — each node is visited once.
- **Space:** `O(h)` recursion stack, where `h` is tree height (`O(n)` worst case, `O(log n)` for balanced tree).