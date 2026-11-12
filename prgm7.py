def minimax(d, i, m, s, a, b):
    if d == 3:
        return s[i]

    if m:
        best = float('-inf')

        for x in range(2):
            v = minimax(d+1, i*2+x, False, s, a, b)
            best = max(best, v)
            a = max(a, best)

            if b <= a:
                break

        return best

    else:
        best = float('inf')

        for x in range(2):
            v = minimax(d+1, i*2+x, True, s, a, b)
            best = min(best, v)
            b = min(b, best)

            if b <= a:
                break

        return best

s = [3,5,6,9,1,2,0,-1]

print("Optimal value:", minimax(0,0,True,s,float('-inf'),float('inf')))