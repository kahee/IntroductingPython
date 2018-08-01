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


def check_bracket(list):
    """
    괄호문 체크 함수
    :param list:
    :return:
    """
    left_bracket = ['{', '(', '[']
    right_bracket = ['}', ')', ']']

    # 매개변수로 받은 list의 문자 순회
    for letter in list:

        #  왼쪽 괄호 인 경우 Push()
        if letter in left_bracket:
            push(letter)

        # 오른쪽 괄호 인 경우 pop()
        if letter in right_bracket:

            # 오른쪽 괄호가 먼저 오는 경우가 있기 때문에
            # 체크를 해줘야 한다.
            if len(stack) != 0:
                item = pop()

                # pop한 왼쪽 괄호와 오른쪽 괄호가 같은 짝인지 체크
                # 만약 아니라면 다시 push()
                if left_bracket.index(item) != right_bracket.index(letter):
                    push(item)

    if len(stack) != 0:
        return print('괄호문 체크 실패')
    else:
        return print('괄호문 체크 완료')


stack = []
string = 'abc+[(x+y)+[z+e+y]+d]}'

check_bracket(string)
