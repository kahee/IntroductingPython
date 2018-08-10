class BHeap:
    def __init__(self, a):
        # 리스트 a
        self.a = a
        # 항목 수 N
        self.N = len(a) - 1

    def create_heap(self):
        # 초기 힙 만들기 = 상향식 힙 만들기
        # 초기에 임의의 순서로 키가 저장되어 있는 리스트 a[1]~a[N]의 항목들을 최소힙으로 만든다.
        # a[1]을 downheap하여 최소힙을 만드는 것을 의미
        # a[N//2+1] ~ a[N] 에 대하여 downheap 을 수행하지 않는 이유는 이 노드들이 이파리이므로
        # 각각의 노드가 힙 크기가 1인 독립적인 최소힙이기 때문이다.
        for i in range(self.N // 2, 0, -1):
            self.downheap(i)

    def insert(self, key_value):
        self.N += 1
        self.a.append(key_value)
        self.upheap(self.N)

    def delete_min(self):

        if self.N == 0:
            print('힙이 비어있음')
            return None

        minimum = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]
        self.N -= 1
        self.downheap(1)
        return minimum

    def downheap(self, i):

        while 2 * i <= self.N:
            # 왼쪽, 오른쪽 자식중에서 승자 결정
            k = 2 * i

            if k < self.N and self.a[k][0] > self.a[k + 1][0]:
                k += 1
            # 힙속성 만족하면, 루프 나가기
            if self.a[i][0] < self.a[k][0]:
                break
            # 자식 승자와 현재 노드 교환
            self.a[i], self.a[k] = self.a[k], self.a[i]
            i = k

    def upheap(self, j):
        while j > 1 and self.a[j // 2][0] > self.a[j][0]:
            # 부모와 자식 교환
            self.a[j], self.a[j // 2] = self.a[j // 2], self.a[j]
            # 현재 노드가 한단계 위로 올라감
            j = j // 2

    def print_heap(self):
        for i in range(1, self.N+1):
            print(f'[{self.a[i][0]}, {self.a[i][1]}]', end='')
        print('\n 힙 크기 = ', self.N)


if __name__ == '__main__':
    a = [None] * 1
    a.append([90, 'watermelon'])
    a.append([80, 'pear'])
    a.append([70, 'melon'])
    a.append([50, 'lime'])
    a.append([60, 'mango'])
    a.append([20, 'cherry'])
    # a.append([30, 'grape'])
    # a.append([35, 'orange'])
    # a.append([10, 'apricot'])
    # a.append([15,'banana'])
    # a.append([45,'lemon'])
    # a.append([40,'kiwi'])
    # print(a)
    b = BHeap(a)
    b.print_heap()

    b.create_heap()
    print("최소힙")
    b.print_heap()

    print('최솟값 삭제 후')
    print(b.delete_min())
    b.print_heap()

    b.insert([5,'apple'])
    print('5 삽입 후')
    b.print_heap()