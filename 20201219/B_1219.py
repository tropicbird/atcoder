H, W = map(int, input().split())
L = [list(map(int, input().split())) for i in range(H)]

def flatten(nested_list):
    """2重のリストをフラットにする関数"""
    return [e for inner_list in nested_list for e in inner_list]

minimum=min(flatten(L))

ans=0
for l in L:
    for a in l:
        ans+=a-minimum
print(ans)

