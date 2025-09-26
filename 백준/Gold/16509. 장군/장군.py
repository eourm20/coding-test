import sys
input = sys.stdin.readline

def dfs():
    S = tuple(map(int, input().split()))
    K = tuple(map(int, input().split()))

    go = (((1,0),(1,-1)), ((1,0),(1,1)), ((-1,0),(-1,-1)), ((-1,0),(-1,1)), ((0,1),(-1,1)), ((0,1),(1,1)), ((0,-1),(-1,-1)), ((0,-1),(1,-1)))

    stack = [(0,S[0],S[1])]
    while stack:
        n, r, c = stack.pop(0)
        if r==K[0] and c==K[1]:
            print(n)
            return
        for g,gg in go:
            nr, nc = r+g[0], c+g[1]
            if 0<=nr<=9 and 0<=nc<=8:
                if nr==K[0] and nc==K[1]:
                    continue
                else:
                    nnr, nnc = nr+gg[0], nc+gg[1]
                    if 0<=nnr<=9 and 0<=nnc<=8:
                        if nnr==K[0] and nnc==K[1]:
                            continue
                        else:
                            nnnr, nnnc = nnr+gg[0], nnc+gg[1]
                            if 0<=nnnr<=9 and 0<=nnnc<=8:
                                if nnnr==K[0] and nnnc==K[1]:
                                    print(n+1)
                                    return
                                else:
                                    nn = n+1
                                    stack.append((nn, nnnr, nnnc))


dfs()
