from myqueue.priority_queue import PriorityQueue
import heapq


def sol_347(nums, k):
    """
    nums中, 频次前k的数
    [1, 1, 1, 2, 2, 3], 2 -> [1, 2]
    $ 先用map统计次数, 然后使用优先级队列(最大堆)
    """

    class Freq:
        def __init__(self, e, freq):
            self.e = e
            self.freq = freq

        def __gt__(self, other):
            # 频次越低的, 优先级越高
            return self.freq < other.freq

    res = {}

    for i in nums:
        res[i] = res.get(i, 0) + 1

    pq = PriorityQueue()

    for i, v in res.items():
        # 不够k个直接放入, 多于k个的值, 如果频次比最小频次大, 最小频次(队头)出队, 入队当前值
        if pq.size() < k:
            pq.enqueue(Freq(i, v))

        elif v > pq.get_front().e:
            pq.dequeue()
            pq.enqueue(Freq(i, v))

    print(pq.size())  # 最多只维护k个值
    for i in range(k):
        print(pq.dequeue().e)


if __name__ == '__main__':
    sol_347([1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5], 3)
