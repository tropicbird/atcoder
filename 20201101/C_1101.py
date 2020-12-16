N = int(input())
L = [list(map(int, input().split())) for i in range(N)]


def collinear(x1, y1, x2, y2, x3, y3):

    """ Calculation the area of
        triangle. We have skipped
        multiplication with 0.5 to
        avoid floating point computations """
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

    if (a == 0):
        print("Yes")
        exit()
    #
    # else:
    #     print("No")

import itertools
for comb in itertools.combinations(L,3):
    x1=comb[0][0]
    y1=comb[0][1]
    x2=comb[1][0]
    y2=comb[1][1]
    x3=comb[2][0]
    y3=comb[2][1]
    collinear(x1, y1, x2, y2, x3, y3)
print("No")



