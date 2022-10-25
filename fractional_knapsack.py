def fractionalKnapsack(W, wt, val, n):
    used = [0]*n
    tot_v = 0
    cur_w = W
    while cur_w > 0:
        max_i = -1
        for i in range(n):
            if used[i] == 0 and (max_i == -1 or val[i]/wt[i] > val[max_i]/wt[max_i]):
                max_i = i
        used[max_i] = 1
        cur_w -= wt[max_i]
        tot_v += val[max_i]
        if cur_w < 0:
            tot_v -= val[max_i]
            tot_v += (1 + cur_w/wt[max_i])*val[max_i]
    print("Maximum possible benefit value:", int(tot_v))


val = []
wt = []
n = int(input("Enter the total number of items present in Knapsack: "))
for i in range(n):
    v, w = map(int, input("Enter the value and weight of item "+str(i+1)+" : ").split())
    val.append(v)
    wt.append(w)
W = int(input("Enter the maximum capacity of the Knapsack: "))
fractionalKnapsack(W, wt, val, n)
