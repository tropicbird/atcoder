import heapq
import time
import timeit

def heapsort(iterable):

    h = []
    for value in iterable:
        heapq.heappush(h, value)

    return [heapq.heappop(h) for i in range(len(h))]

#t1 = time.time()
x=[1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
result = timeit.timeit('heapsort(x)', globals=globals(), number=10000)
print(result)

result = timeit.timeit('sorted(x)', globals=globals(), number=10000)
print(result)

#t2 = time.time()
#elapsed_time = t2 - t1
#print(f"経過時間：{elapsed_time}")