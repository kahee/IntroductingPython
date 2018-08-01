from collections import deque

dq = deque('data')
for elem in dq:
    print(elem.upper(), end='')
print()

# 맨뒤와 맨앞에 항목 삽입
dq.append('r')
dq.appendleft('k')

print(dq)

# 맨뒤와 맨앞 항목 삭제
dq.pop()
dq.popleft()

# 마지막 항목 출력
print(dq[-1])
print('x' in dq)

dq.extend('structure')
dq.extendleft(reversed('python'))
print(dq)