# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def build_tree():
#     a = Node('a')
#     b = Node('b')
#     c = Node('c')
#     d = Node('d')
#     e = Node('e')
#     f = Node('f')
#     g = Node('g')
#     i = Node('i')
#     j = Node('j')

#     times1 = Node('*')
#     plus1 = Node('+')
#     times2 = Node('*')
#     plus2 = Node('+')
#     pow = Node('^')

#     times1.left = plus1
#     times1.right = times2

#     plus1.left = times2
#     plus1.right = g

#     times2.left = plus2
#     times2.right = pow

#     plus2.left = d
#     plus2.right = e

#     pow.left = i
#     pow.right = j

#     plus1.left.left = a
#     plus1.left.right = b
#     plus2.left.left = c

#     return times1

# root = build_tree()
class Node:
    def init(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(expression):
    stack = []
i = 0
while i < len(expression):
    if expression[i] == '(':
        i += 1
    stack.append('(')
elif expression[i] == ')':
i += 1
subtree = stack.pop()
if stack[-1] == '(':
stack.pop()
if len(stack) > 0 and stack[-1] != '(':
node = Node(stack.pop())
node.right = subtree
node.left = stack.pop()
stack.append(node)
else:
stack.append(subtree)
elif expression[i] in ['+', '-', '', '/']:
stack.append(expression[i])
i += 1
else:
j = i
while j < len(expression) and expression[j] not in ['(', ')', '+', '-', '', '/']:
j += 1
stack.append(Node(expression[i:j]))
i = j
return stack[0]

expression = "(a+b)(c(d+e+f))+g*(i+j^2)"
root = build_tree(expression)
print(root.value)  # Output: *
print(root.left.value)  # Output: +(a, b)
print(root.right.value)  # Output: +
print(root.right.left.value)  # Output: *(c, +(d, e, f))
print(root.right.right.value)  # Output: *(g, j^2)
print(root.right.right.left.value)  # Output: i
