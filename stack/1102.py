stack_size = 5
stack = [None] * stack_size
top = -1

def isEmpty():
    return top == -1

def isFull():
    return top == stack_size - 1

def push(e):
    global top
    if not isFull():
        top += 1
        stack[top] = e

def pop():
    global top
    if not isEmpty():
        popped_element = stack[top]
        top -= 1
        return popped_element
    else:
        return None

def peek():
    if not isEmpty():
        return stack[top]
    else:
        return None

# 예제 사용
push(1)
push(2)

popped_value = pop()

if popped_value is not None:
    pass

peek_value = peek()
