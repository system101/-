'''
developer: Nat Rungpeng 3118999255
latest update: 20-03-2019, 14:16
'''
def print_Matrix(m):
    for row in m:
        print (row)

def print_Solution(m):
    for i in range(len(m)):
##        print ('x'+str(i+1)+' = '+str(format_e(m[i])))
        print ('x'+str(i+1)+' = '+str(m[i]))

def format_e(n):
    a = '%e' % n
    return a.split('e')[0].rstrip('0').rstrip('.') + 'e' + a.split('e')[1]

def Gaussian_Elimination(m):
    a = m
    n = len(m)
    for k in range(n-1): # no. of steps
        for i in range(k+1,n): # no. of rows
            if (i >= n): 
                break
            elif (a[k][k] != 0): # divide zero case
                factor = a[i][k]/a[k][k]
                for j in range(k+1,n): 
                    a[i][j] = a[i][j] - (factor * a[k][j])
                a[i][len(a[i])-1] -= (factor * a[k][len(a[k])-1]) # b(i) -= factor * b(k)
    return a

def Backward_Substitution(m):
    a = m
    n = len(m)
    x = [0 for row in range(n)] # initialize array
    if (a[n-1][len(a[n-1])-2] != 0):
        x[n-1] = a[n-1][len(a[n-1])-1]/a[n-1][len(a[n-1])-2]
    for i in range(n-1,-1,-1): # range from n-1 to 0 step down by one
        stack = a[i][len(a[i])-1] # stack = b(i)
        for j in range(i+1, n):
            stack -= (a[i][j] * x[j])
        if (a[i][i] != 0):
            x[i] = stack / a[i][i]
    return x

matrix01 = [[5,2,3],   
          [-3,3,15]]
          # answer: [-1,4]

matrix02 = [[1,2,-3,-1,0],   
          [0,-3,2,6,-8],
          [-3,-1,3,1,0],
          [2,3,2,-1,-8]]
          # answer: [-1,-2,-1,-2]

matrix03 = [[5,2,0,2],   
          [2,1,-1,0],
          [2,3,-1,3]]
          # answer: [-1/5,3/2,11/10]

matrix04 = [[0,0,0,2],   
          [0,0,0,0],
          [0,0,0,-3]]

matrix05 = [[0.05, 0.07, 0.06, 0.05, 0.23],
        [0.07, 0.10, 0.08, 0.07, 0.32],
        [0.06, 0.08, 0.10, 0.09, 0.33],
        [0.05, 0.07, 0.09, 0.10, 0.31],]
        # answer: [1,1,1,1]
print_Solution(Backward_Substitution(Gaussian_Elimination(matrix05)))
