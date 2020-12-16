N, M = map(int, input().split())
A = list(map(int, input().split()))
import numpy as np
from collections import deque
from collections import Counter


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # ここで分割を行う
    left = arr[:mid]
    right = arr[mid:]

    # 再帰的に分割を行う
    left = merge_sort(left)
    right = merge_sort(right)

    # returnが返ってきたら、結合を行い、結合したものを次に渡す
    return merge(left, right)


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged

A=merge_sort(A)
# print(A)
arr1 = deque(A)
arr2 = deque(A)

arr1.appendleft(0)
arr2.append(N+1)
# print(arr1)
# print(arr2)

arr1=np.array(arr1)
arr2=np.array(arr2)

# print(arr1)
# print(arr2)

range_arr=(arr2-arr1)-1
# print(range_arr)
k=0
ss=sorted(set(range_arr))
for k in ss:
    if k!=0:
        break
if k==0:
    print(0)
    exit()

S=Counter(range_arr)
ans=0
for i in S.items():
    if i[0]==0:
        continue
    tmp=i[0]//k
    if i[0] % k!=0:
        tmp+=1
    ans+=tmp*i[1]
print(ans)