'''
1. 주어진 정보를 트리에 저장
  1.1 노드, 트리 구조 생성
  1.2 전우, 중위, 후위순회 함수 생성
2. 트리 정보 입력 방법

'''
# SOLVED

import sys

class Node:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right

def preorder(node):
  print(node.data, end="")
  if node.left != '.':
    preorder(tree[node.left])
  if node.right != '.':
    preorder(tree[node.right])

def inorder(node):
  if node.left != '.':
    inorder(tree[node.left])
  print(node.data, end="")
  if node.right != '.':
    inorder(tree[node.right])

def postorder(node):
  if node.left != '.':
    postorder(tree[node.left])
  if node.right != '.':
    postorder(tree[node.right])
  print(node.data, end="")
    
n = int(sys.stdin.readline().rstrip())
tree = {}

for _ in range(n):
  node, left, right = map(str, sys.stdin.readline().split())
  tree[node] = Node(data=node, left=left, right=right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])