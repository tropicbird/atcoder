def main():
    H, W=map(int,input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    L=[list('#' for i in range(W+2)) for i in range(H+2)]
    L = [list(map(int, input().split())) for i in range(H)]
    for h in range(H):
        L[h].insert(0,"#")
        L[h].append('#')
    L.insert(0, list('#' for i in range(W+2)))
    L.append(list('#' for i in range(W + 2)))

    def isWall(s):
        return 1 if s == '#' else 0

    def getWalls(arr, i, j):
        return isWall(arr[i + 1][j]) + isWall(arr[i - 1][j]) + isWall(arr[i][j + 1]) + isWall(arr[i][j - 1])

    def getEdge(arr, i, j, edges, v, c):
        for (a, b) in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            if isWall(arr[i + a][j + b]) == 0:
                arr[i + a][j + b] = '$'
                if arr[i + 2 * a][j + 2 * b] == 0:
                    vn = v
                    cn = c + 1
                else:
                    vn = arr[i + 2 * a][j + 2 * b]
                    edges.append((v, vn, c))
                    cn = 1
                getEdge(arr, i + 2 * a, j + 2 * b, edges, vn, cn)

    vs = 0
    edges = list()
    arr = list()
    # for line in open('maze_input.txt', 'r'):
    #     arr.append(list(line))
    height = len(L)
    width = len(L[height - 1])
    cellidi = range(1, width, 2)
    cellidj = range(1, height, 2)
    for i, j in it.product(cellidi, cellidj):
        if getWalls(arr, i, j) == 2:
            arr[i][j] = 0
        elif arr[i][j] == ' ':
            vs += 1
            arr[i][j] = vs




    a='#'
    L = [list('#' for i in range(W+2)) if (i==0) or (i==(H+1)) else ['#'].extend(list(map(int, input().split()))).extend('#') for i in range(H+2)]

    if

    for h in range(Dh-2,Dh+3):
        for w in range(Dw-2,Dw+3):

    # X = int(input())
    # L = [list(map(int, input().split())) for i in range(N)]

    X = int(input())
    L = list(map(int, input().split()))

    highest=L[0]
    val=0
    for A in L[1:]:
        if A<highest:
            val+=(highest-A)
        elif A>highest:
            highest=A
    print(val)


if __name__ == '__main__':
    main()