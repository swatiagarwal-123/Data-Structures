def rotateMatrix(a, N):
    # Consider all matrix cells one by one
    for x in range(0, int(N/2)):

        # Consider the elements in groups of 4 in the current square
        for y in range(x, N-x-1):

            # Store the value of current cell in the 'temp' variable
            temp = a[x][y]

            # Rotation of values from Right to Top
            a[x][y] = a[y][N-1-x]

            # Rotation of values from Bottom to Right
            a[y][N-1-x] = a[N-1-x][N-1-y]

            # Rotation of values from Left to Bottom
            a[N-1-x][N-1-y] = a[N-1-y][x]

            # Assign value of 'temp' to Left
            a[N-1-y][x] = temp


def displayMatrix(a, N):
    for i in range(0, N):
        for j in range(0, N):
            print(a[i][j], end=' ')
        print("")


n = int(input("Enter the order of the matrix: "))
a = []
print("Enter the elements of the matrix: ")
for i in range(n):
    a.append(list(map(int, input().split())))

print("Original Array: ")
displayMatrix(a, n)
print("90 Degrees Rotated Array:")
rotateMatrix(a, n)
displayMatrix(a, n)
