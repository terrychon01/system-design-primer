# Given an m x n matrix, return all elements of the matrix in spiral order.

# right ... down ... left ... up .. right


def spiralOrder(matrix):

    if matrix == []:
        return matrix

    l = 0
    r = len(matrix[0]) - 1
    t = 0
    b = len(matrix) - 1
    
    print(l, r, t, b)

    ret = []
    while l < r and t < b:
        # top
        for i in range(l, r):
            ret.append(matrix[t][i])
            print('top', ret)
        # right
        for i in range(t, b):
            ret.append(matrix[i][r])
            print('right', ret)
        # bottom
        for i in range(r, l, -1):
            ret.append(matrix[b][i])
            print('left', ret)
        # left
        for i in range(b, t, -1):
            ret.append(matrix[i][l])

        l += 1
        r -= 1 
        t += 1
        b -= 1

    # single square
    if l == r and t == b:
        ret.append(matrix[t][l])
    # vertical line
    elif l == r:
        for i in range(t, b + 1):
            ret.append(matrix[i][l])
    # horizontal line
    elif t == b:
        for i in range(l, r + 1):
            ret.append(matrix[t][i])
    return ret


if __name__ == "__main__":
    
    input = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    
    output = spiralOrder(input)
    # output = [1,2,3,6,9,8,7,4,5]