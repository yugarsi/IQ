import threading
import collections
#blocking queue using threading using two semaphores
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.Enqueue = threading.Semaphore(capacity)  # init semaphore 1 to max size (capacity
        self.Dequeue = threading.Semaphore(0)  # init to 0
        self.q = collections.deque()

    def enqueue(self, element: int) -> None:
        self.Enqueue.acquire()  # if full don't add anymore and block it
        # acquire decrements a counter everytime called
        self.q.append(element)  # semaphore is blocked when semaphore counter reaches 0
        self.Dequeue.release()  # release increments semaphore counter

    def dequeue(self) -> int:
        self.Dequeue.acquire()  # if empty block and don't let it deque
        res = self.q.popleft()
        self.Enqueue.release()
        return res

    def size(self) -> int:
        return len(self.q)
