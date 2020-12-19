#import pandas as pd

N = int(input())
A = list(map(int, input().split()))

# N = 2*10**5
# A = list(range(N))

#num = [7, 5, 1, 6, 9]





indices = [*range(N)]
sorted_indices = sorted(indices, key=lambda i: -A[i])
sorted_num = [A[i] for i in sorted_indices]
print(sorted_num)      # ==> [9, 7, 6, 5, 1]
print(sorted_indices)  # ==> [4, 0, 3, 1, 2]

for i in range(1,N):
    index_tmp=sorted_num.index(i)
    tmp=index_tmp-i
    tmp*





ans=0
for i, a in enumerate(A):
    index_tmp = sorted_num.index(a)
    index_tmp = sorted_indices.index(i)
    bigger = sorted_num[:index_tmp]
    smaller = sorted_num[index_tmp:]
    ans+=bigger.sum-a*len(bigger)
    ans+=a * len(smaller)-smaller.sum



for i in range(N-1):
    base=A[i]*N-i-1
    sorted_A=merge_sort(A[i:])
    index_tmp=sorted_A.index(A[i])
    minus=sorted_A[:index_tmp]
    plus=





#
#
#
#
#
for i in range(N-1):
    base=A[i]*N-i-1
    sorted_A=merge_sort(A[i:])
    index_tmp=sorted_A.index(A[i])
    minus=sorted_A[:index_tmp]
    plus=
#
#
#
#
# A_posi=list(range(N))
# A_new=merge_sort(A)
#
#
#
#
# for a in A:
#     A_new.index(a)
#
#
#
#
#
#
#
# A_posi=list(range(N))
#
#
#
#
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     # ここで分割を行う
#     left = arr[:mid]
#     right = arr[mid:]
#
#     # 再帰的に分割を行う
#     left = merge_sort(left)
#     right = merge_sort(right)
#
#     # returnが返ってきたら、結合を行い、結合したものを次に渡す
#     return merge(left, right)
#
#
# def merge(left, right):
#     merged = []
#     l_i, r_i = 0, 0
#
#     # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
#     while l_i < len(left) and r_i < len(right):
#         # ここで=をつけることで安定性を保っている
#         if left[l_i] <= right[r_i]:
#             merged.append(left[l_i])
#             l_i += 1
#         else:
#             merged.append(right[r_i])
#             r_i += 1
#
#     # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
#     if l_i < len(left):
#         merged.extend(left[l_i:])
#     if r_i < len(right):
#         merged.extend(right[r_i:])
#     return merged
#
# for a in A:
#     A_new = merge_sort(A)
#
#
# A_new=merge_sort(A)
# for a in A:
#     A_new.index(a)
#
#
#
#
# ans=0
#
# for i in range(N-1):
#     # print(f'i:{i}')
#     for j in range(i+1,N):
#         # print(f'j:{j}')
#         # print(i,j)
#         # print(A[i],A[i+j])
#         # print(abs(A[i]-A[j]))
#         tmp=abs(A[i]-A[j])
#         ans+=tmp
#         # print(ans)
# print(ans)