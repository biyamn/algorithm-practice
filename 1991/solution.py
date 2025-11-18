# 입력 예시
# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .

# 트리로 만든 예시
#       A
#     /   \
#    B     C
#   /     / \
#  D     E   F
#             \
#              G

# 입력을 튜플로 저장한 예시
# tuple = ("A", 
#           ("B", 
#             ("D", None, None), 
#             None
#           ),
#           ("C", 
#             ("E", None, None), 
#             ("F", 
#               None, 
#                 ("G", None, None)
#             )
#           )
#         )


# 맨 처음에 N 입력받음
N = int(input())

# 딕셔너리 형태로 저장
dictionary = {}
for i in range(N):
  parent, left, right = input().split(" ")
  dictionary[parent] = (left, right)

# 딕셔너리 형태 -> 튜플 형태로 저장
def dictionary_to_tuple(node):
  if node == ".":
    return None
  left, right = dictionary[node]
  return (
    node,
    dictionary_to_tuple(left),
    dictionary_to_tuple(right)
  )

tuple = dictionary_to_tuple("A")

# preorder
# 루트 방문 -> 왼쪽 서브트리 방문 -> 오른쪽 서브트리 방문
# A B D C E F G
preOrder_array = []
def preOrder(tuple): 
  if tuple is None:
    return
  parent, left, right = tuple
  preOrder_array.append(parent)
  preOrder(left)
  preOrder(right)

# inorder
# 왼쪽 서브트리 방문 -> 루트 방문 -> 오른쪽 서브트리 방문
# D B A E C F G
inOrder_array = []
def inOrder(tuple): 
  if tuple is None:
    return
  parent, left, right = tuple
  inOrder(left)
  inOrder_array.append(parent)
  inOrder(right)

# postorder
# 왼쪽 서브트리 방문 -> 오른쪽 서브트리 방문 -> 루트 방문
# D B E G F C A
postOrder_array = []
def postOrder(tuple): 
  if tuple is None:
    return
  parent, left, right = tuple
  postOrder(left)
  postOrder(right)
  postOrder_array.append(parent)

preOrder(tuple)
inOrder(tuple)
postOrder(tuple)

print("".join(preOrder_array))
print("".join(inOrder_array))
print("".join(postOrder_array))


# 💥 실제 연산자가 들어간 식을 풀어본다면???? 💥
# 문제: 2 + 3 * 4

# 트리 구조로 표현
#     +
#   /   \
#  2     *
#       / \
#      3   4

# 전위 표기법(preOrder)
# 2 + 3 * 4

# 중위 표기법(inOrder)
# 2 + 3 * 4

# 후위 표기법(postOrder)
# 2 3 4 * +