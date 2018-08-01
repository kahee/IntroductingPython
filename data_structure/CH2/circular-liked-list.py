from list import EmptyError


class CList:
    class _Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.last = None
        self.size = 0

    def no_items(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        n = self._Node(item, None)

        if self.is_empty():
            # 첫 노드를 삽입하는 경우,
            # 새 노드는 자기 자신을 참조, last가 새 노드 참조
            n.next = n
            self.last = n

        else:
            n.next = self.last.next
            self.last.next = n

        self.size += 1

    def first(self):
        if self.is_empty():
            raise EmptyError('UnderFlow')
        f = self.last.next
        return f.item

    def delete(self):
        if self.is_empty():
            raise EmptyError('UnderFlow')
        x = self.last.next
        if self.size == 1:
            # 노드가 한개인 경우는 last를 None
            self.last = None
        else:
            self.last.next = x.next

        self.size -= 1

        return x.item

    def print_list(self):
        if self.is_empty():
            print("리스트 비어있음")
        else:
            f = self.last.next
            p = f
            while p.next != f:
                # 첫 노드가 다시 방문되면 루프 중단
                print(p.item, '->', end='')
                p = p.next
            print(p.item)


if __name__ == '__main__':
    s = CList()
    s.insert('pear')
    s.insert('cheery')
    s.insert('orange')
    s.insert('apple')
    s.print_list()

    print('s의 길이= ', s.no_items())
    print('s의 첫 항목:', s.first())
    s.delete()
    print('첫 노드 삭제 후: ', end='')
    s.print_list()

    print('s의 길이= ', s.no_items())
    print('s의 첫 항목:', s.first())
    s.delete()
    print('첫 노드 삭제 후: ', end='')
    s.print_list()
