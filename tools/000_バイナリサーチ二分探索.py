from bisect import bisect_left
def contains(a, x):
    """returns true if sorted sequence `a` contains `x`"""
    i = bisect_left(a, x)
    print(i)
    return i != len(a) and a[i] == x

print(contains([1,1,2,2.1,3,5], 3))
print(contains([1,2,3,5], 4))

#On the other hand, sorting a list has greater time-complexity than building a set, so most of the time a set would be the way to go.
# a = [10, 6, 8, 1, 2, 5, 9]
# a_set = set(a)
# 10 in a_set