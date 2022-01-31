import math

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min = math.inf
    max = 0

    for j in range(0, len(arr)):

        soma = 0

        for i in range(0, len(arr)):

            if (i != j):
                soma += arr[i]

        if (soma > max):
            max = soma

        if (soma < min):
            min = soma

    print(min, max)


if __name__ == '__main__':
    arr = [1,2,3,4,5]

    miniMaxSum(arr)
