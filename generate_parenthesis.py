def genParenthesis(i, n, open, close, exp):

    # Base Case

    if i == 2*n:
        print("".join(exp))
        return

    # Recursive Case

    if open < n:
        exp[i] = '{'
        genParenthesis(i+1, n, open+1, close, exp)

    if close < open:
        exp[i] = '}'
        genParenthesis(i+1, n, open, close+1, exp)


n = int(input("Enter a number: "))
exp = [""]*2*n
genParenthesis(0, n, 0, 0, exp)
