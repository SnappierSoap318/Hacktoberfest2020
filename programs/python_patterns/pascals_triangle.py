def binomialCoeff(n, k) : 
    res = 1
    if (k > n - k) :
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1) 
      
    return res

def printPascal(n):
    m = (2 * n) - 2
    for i in range(n):
        print(' '*m, end = ' ')
        m = m - 1
        for j in range(i+1):
            print(binomialCoeff(i,j), end = ' ')
        print('\n')

def main():
    n = int(input("Enter a number: "))
    printPascal(n)

main()