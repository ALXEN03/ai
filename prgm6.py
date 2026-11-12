def minimax(d, i, m, s):
    if d == 3:
        return s[i]

    if m:
        return max(
            minimax(d+1, i*2, False, s),
            minimax(d+1, i*2+1, False, s)
        )
    else:
        return min(
            minimax(d+1, i*2, True, s),
            minimax(d+1, i*2+1, True, s)
        )

s = [3,5,2,9,12,5,23,1]

print("Optimal value:", minimax(0,0,True,s))