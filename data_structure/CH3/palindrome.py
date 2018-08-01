def push(item):
    stack.append(item)


def pop():
    # 삭제 연산
    if len(stack) != 0:
        # 리스트의 맨 뒤에 있는 항목 제거
        item = stack.pop(-1)
        return item


def check_palindrome(string):
    """
    회문 검사 함수
    :param string:
    :return:
    """
    length = len(string)

    # 매개변수로 받은 문자열이 짝수 인 경우
    if length % 2 == 0:
        # 앞에 반절은 스택에 push
        for letter in string[:length // 2]:
            push(letter)

        # 스택에 있는 문자와 뒤에 있는 문자 비교
        for letter in string[length // 2:]:
            item = pop()
            # 같지 않은 경우 push
            if item != letter:
                push(item)

    # 매개변수로 받은 문자열이 홀수 인 경우
    else:
        for letter in string[:length // 2]:
            push(letter)

        # 중간 문자를 버리고 비교
        for letter in string[length // 2 + 1:]:
            item = pop()
            print(length//2+1)
            print(letter)

            if item != letter:
                push(item)


    if len(stack) != 0:
        return print('회문이 아닙니다.')

    else:
        return print('회문입니다.')


stack = []
letters = "raceDar"
check_palindrome(letters)
