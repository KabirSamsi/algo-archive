def maxArea(height):
    #Solve using dynamic programming
    #At any point, we may either build the tank here, or see if we can find a better position
    #OPT(i, i-1) = 0
    #OPT(i, i) = 0
    #OPT(i, i+1) = min(h[i], h[i+1]) * 1
    #OPT(i, n) = max{min(i, n) * (n-i), OPT(i+1, n), OPT(i, n-1)}
    # This recurrence outlines the idea that we either pick the two towers we have, or try and find a more optimal arrangement down the middle

    if len(height) < 2:
        return 0
    
    if len(height) == 2:
        return min(height)

    opt = [] #Initialize the DP Matrix
    n = len(height)
    
    #Set all unitialized opt values to -1
    for x in range(n):
        opt.append([0] * n)

    #Populate opt with base cases
    opt[0][0] = 0
    for i in range(1, len(opt)-1):
        opt[i][i] = 0
        opt[i][i-1] = 0
        opt[i][i+1] = min(height[i], height[i+1])
    #Leftover for loop populating 
    opt[len(opt)-1][len(opt)-1] = 0
    opt[len(opt)-1][len(opt)-2] = 0
    
    for x in range(n-2): #Last row is already populated, iterate backwards
        st = n-x-3
        for fn in range(st+1,n): #Move forward from central diagonal
            print(st, fn, min(height[st], height[fn]) * (fn-st), opt[st+1][fn], opt[st][fn-1])
            opt[st][fn] = max(min(height[st], height[fn]) * (fn-st), opt[st+1][fn], opt[st][fn-1])
    
    for row in opt:
        print(row)

    return opt[0][n-1]

print(maxArea([1,2,3,4,5,25,24,3,4]))