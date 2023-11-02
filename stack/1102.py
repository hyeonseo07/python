#스택 정렬 | 가장 나중에 들어온 자료가 먼저 선출되는 선입후출
stack_size=5
list[None]*stack_size
top=-1              #top의 값에 기준으로 가득찼는지 아닌지 측정

def isEmpty():
    if top==-1:return True #만약 (비어)바깥에 위치하면 True를 반환
    else:return False

def isFull():
    return top==stack_size-1
def push(e):


def pop():
    global top
    if not isEmpty():
        return True
    else: return False
    
def peek():
    if not isEmpty():
        return list[top]
    else:pass

push(1)
push(1)

