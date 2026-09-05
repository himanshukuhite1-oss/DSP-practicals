# Stack Operations and Infix to Postfix

# Stack implementation
stack = []

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return None
    return stack.pop()

def peek():
    if len(stack) == 0:
        return None
    return stack[-1]


# Operator precedence
def precedence(operator):
    if operator == '^':
        return 3
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return 0


# Infix to Postfix conversion
def infix_to_postfix(expression):
    operators = []
    postfix = ""

    for char in expression:
        # If character is an operand
        if char.isalnum():
            postfix += char

        # Opening bracket
        elif char == '(':
            operators.append(char)

        # Closing bracket
        elif char == ')':
            while operators and operators[-1] != '(':
                postfix += operators.pop()
            operators.pop()

        # Operator
        else:
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(char)):
                postfix += operators.pop()

            operators.append(char)

    # Pop remaining operators
    while operators:
        postfix += operators.pop()

    return postfix


# Stack operations
print("===== STACK OPERATIONS =====")

push(10)
push(20)
push(30)

print("Stack:", stack)
print("Top element:", peek())

print("Popped element:", pop())
print("Stack after pop:", stack)


# Infix to Postfix
print("\n===== INFIX TO POSTFIX =====")

expression = input("Enter infix expression: ")

result = infix_to_postfix(expression)

print("Infix Expression :", expression)
print("Postfix Expression:", result)