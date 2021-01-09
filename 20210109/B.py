from collections import Counter

N = int(input())
L = [list(map(int, input().split())) for i in range(N)]


def flatten(nested_list):
    """2重のリストをフラットにする関数"""
    return [e for inner_list in nested_list for e in inner_list]

all_int = set(flatten(L))

maximum = len(all_int)
# print(maximum)
all_dic = {}
for j in all_int:
    all_dic[j] = []

for i, l in enumerate(L):
    all_dic[l[0]].append(i)
    all_dic[l[1]].append(i)
ls = []

for i in all_int:
    if len(all_dic[i]) == 1:
        ls.append(all_dic[i][0])
S = Counter(ls)
values = S.values()
count = 0
for value in values:
    if value == 2:
        count += 1

ans = maximum - count
if ans >= N:
    print(N)
else:
    print(ans)