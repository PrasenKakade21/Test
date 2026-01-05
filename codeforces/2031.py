/*
 * Problem: CF Problem
 * URL: https://codeforces.com/contest/2031/submit
 * Platform: codeforces
 */

for T in range(int(input())):
    h = []
    n = int(input())
    h = list(map(int,input().split()))
    res = 0
    i = 0
    while i < n-1:
        if h[i] > h[i+1]:
            res += 1 
            i += 1 
        elif h[i] == h[i+1]:
            res += 1 
            while h[i] == h[i+1]:
                i+=1 
            i+=1 
        else:
            break 
    print(res)