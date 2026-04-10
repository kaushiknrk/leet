line = input().strip()
if line:
    T = int(line)
    for _ in range(T):
        N = int(input().strip())
        triangle = []

        for i in range(1, N + 1):
            row = []
            while len(row) < i:
                row.extend(map(int, input().split()))
            triangle.append(row)

        for r in range(N - 2, -1, -1):
            for c in range(len(triangle[r])):
                if triangle[r+1][c] > triangle[r+1][c+1]:
                    triangle[r][c] += triangle[r+1][c]
                else:
                    triangle[r][c] += triangle[r+1][c+1]
        if triangle:
            print(triangle[0][0])
