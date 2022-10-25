def fractionalKnapsack(W, wt, val, n):
    k = []
    for i in range(n+1):
        x = []
        for w in range(W+1):
            if i == 0 or w == 0:
                x.append(0)
            elif wt[i-1] <= w:
                x.append(max(val[i-1]+k[i-1][w-wt[i-1]], k[i-1][w]))
            else:
                x.append(k[i-1][w])
        k.append(x)
    print("Maximum possible benefit value:", k[n][W])


val = []
wt = []
n = int(input("Enter the total number of items present in Knapsack: "))
for i in range(n):
    v, w = map(int, input("Enter the value and weight of item "+str(i+1)+" : ").split())
    val.append(v)
    wt.append(w)
W = int(input("Enter the maximum capacity of the Knapsack: "))
fractionalKnapsack(W, wt, val, n)
