'''
developer: Nat Rungpeng 3118999255
latest update: 22-03-2019, 15:10
'''
def print_Matrix(m):
    for row in m:
        print (row)

def print_Solution(m):
    for i in range(len(m)):
        print ('x'+str(i+1)+' = '+str(m[i]))

def Gaussian_Elimination(m):
    a = m
    n = len(a)
    p = [0 for col in range(len(a[0]))]
    s = [0 for row in range(n)]

    # find the maximal elements of the row
    for i in range(n):    
        s[i] = 0
        for j in range(n):
            s[i] = max(s[i],abs(a[i][j]))
        p[i] = i # save row pointer to its number

    # find largest scaled column entry
    for k in range(n-1):
        r_max = 0
        for i in range(k,n):
            r = abs(a[p[i]][k] / s[p[i]])
            if (r > r_max):
                r_max = r
                j = i       # row index of largest scaled entry
        temp = p[k]         # swap row pointers
        p[k] = p[j]
        p[j] = temp
        for i in range(k+1,n): # eliminate submatrix
            a[p[i]][k] /= a[p[k]][k]
            for j in range(k+1,n):
                a[p[i]][j] -= (a[p[i]][k] * a[p[k]][j])
                
    return Forward_Elimination(a,p,s)

def Forward_Elimination(m, pointers, sMax):
    a = m
    p = pointers
    s = sMax
    n = len(a)
    LAST_COL_INDEX = len(a[0])-1

    for k in range(n-1):
        for i in range(k+1,n):
            a[p[i]][LAST_COL_INDEX] -= (a[p[i]][k] * a[p[k]][LAST_COL_INDEX])
    
    return Backward_substitution(a,p)   

def Backward_substitution(m, pointers):
    print (m)
    a = m
    p = pointers
    n = len(a)
    LAST_COL_INDEX = len(a[0])-1
    x = [0 for row in range(n)] # initialize array
    for i in range(n-1,-1,-1):
        s = a[p[i]][LAST_COL_INDEX]
        for j in range(i+1,n):
            s -= (a[p[i]][j] * x[j])
        x[i] = s / a[p[i]][i]
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
          
matrix04 = [[0.05, 0.07, 0.06, 0.05, 0.23],
        [0.07, 0.10, 0.08, 0.07, 0.32],
        [0.06, 0.08, 0.10, 0.09, 0.33],
        [0.05, 0.07, 0.09, 0.10, 0.31],]
        # answer: [1,1,1,1]

print_Solution(Gaussian_Elimination(matrix04))

