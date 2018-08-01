def push(item):
    stack.append(item)


def peek():
    # top 항목 접근
    if len(stack) != 0:
        return stack[-1]


def pop():
    # 삭제 연산
    if len(stack) != 0:
        # 리스트의 맨 뒤에 있는 항목 제거
        item = stack.pop(-1)
        return item


stack = []
push('apple')
push('orange')
push('cherry')
print(stack)

print(peek())
push('pear')
print(stack)

pop()
push('grape')
print(stack)


