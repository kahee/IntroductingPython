def add(item):
    q.append(item)


def remove():
    # 맨 앞의 항목 삭제
    if len(q) != 0:
        item = q.pop(0)
        return item


def print_q():
    print('front ->', end='')
    for i in range(len(q)):
        # :<8 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 8로 맞출 수 있다.
        print('{!s:<8}'.format(q[i]), end='')

    print('<- rear')


q = []
add('apple')
add('orange')
add('cherry')
add('pear')
print_q()
remove()
print_q()
remove()
print_q()
add('grape')
print_q()
