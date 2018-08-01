class EmptyError(Exception):
    pass


class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)

        else:
            self.head = self.Node(item, self.head)

        self.size += 1

    def insert_after(self, item, p):
        print(p.item)
        print(p.next.item)
        # 오렌지를 선택
        # 오렌지 다음의 아이템을 연결
        # P가 결과적으로 오렌지니까 사과랑 연결이 됨
        p.next = self.Node(item, p.next)

        self.size += 1

    def delete_front(self):
        """
        첫 노드를 삭제 하는 경우
        :return:
        """
        if self.is_empty():
            raise EmptyError('Underflow')

        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self, p):
        """
        p가 가리키는 노드의 다음 노드를 삭제
        :param p:
        :return:
        """
        if self.is_empty():
            raise EmptyError('Underflow')
        t = p.next
        p.next = t.next
        self.size -= 1

    def search(self, target):
        # head부터 순차적으로 검색
        p = self.head

        for k in range(self.size):
            # 탐색 성공
            if target == p.item:
                return k
            p = p.next
        # 탐색 실패
        return None

    def print_list(self):
        p = self.head

        while p:
            if p.next != None:
                print(p.item, '->', end='')
            else:
                print(p.item)

            p = p.next


if __name__ == '__main__':
    s = SList()
    s.insert_front('grape')
    s.insert_front('orange')
    s.insert_front('cherry')
    s.insert_after('apple', s.head.next)
    s.print_list()
    print('cherry는 %d 번째' % s.search('cherry'))
    print('kiwi는 ', s.search('kiwi'))
    # end = 줄바꿈 방지
    # print 문 실행 시 항상 문자열 마지막에 \n 문자가 출력되어 줄바꿈이 일어나게 된다. 이렇게 마지막 문자인 \n을 생략할 수 있는 방법
    print('pear 다음 노드 삭세후:', end='')
    s.delete_after(s.head)
    s.print_list()
    print('첫 노드 삭세 후:', end= '')
    s.delete_front()
    s.print_list()
    print('첫 노드로 망고, 딸기 삽입 후:', end='')
    s.insert_front('mango')
    s.insert_front('strawberry')
    s.print_list()

