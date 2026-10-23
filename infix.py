def infix_to_prefix(exp):
    stack = []
    result = []
    exp = exp[::-1]

    for ch in exp:
        if ch.isalnum():
            result.append(ch)
        elif ch == ')':
            stack.append(ch)
        elif ch == '(':
            while stack and stack[-1] != ')':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != ')' and stack[-1] in '+-*/^':
                if ch == '^' and stack[-1] == '^':
                    break
                result.append(stack.pop())
            stack.append(ch)

    while stack:
        result.append(stack.pop())

    return ''.join(result[::-1])

exp = input("Enter infix expression: ")
print("Prefix expression:", infix_to_prefix(exp))