'''

Name:    Backtracking                             
Purpose: Various problems solved using backtracking                                      
Created by: TigerApps                                 

'''


#################################
## all permutations of a string##
#################################

# time complexity: O(n*n!)
def permute(mystring):
    permutations = []
    permute_h(permutations,mystring,0,len(mystring)-1)
    return permutations

def permute_h(permutations,mystring,start,end):
    if start == end:
        if mystring not in permutations:
            permutations.append(mystring)
    else:
        for i in range(start,end+1):
            mystring = swap(mystring,start,i)
            permute_h(permutations,mystring,start+1,end)
            mystring = swap(mystring,start,i)
            
def swap(s, i, j):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)

# print all permutatins of a string

#mystring = "abc"
#print permute(mystring)
#mystring = "aba"
#print permute(mystring)



###############################
## the knight's tour problem ##
###############################

# time complexity = O(8^(n^2-1))
def solveKT(n):
    sol = []
    for i in range(n):
        sol.append([])
        for j in range(n):
            sol[i].append(-1)
    
    xMove = [  2, 1, -1, -2, -2, -1,  1,  2 ]
    yMove = [  1, 2,  2,  1, -1, -2, -2, -1 ]
    sol[0][0]  = 0;
 
    if not solveKT_h(n, 0, 0, 1, sol, xMove, yMove):
        return False
    else:
        return sol
    
def solveKT_h(n,x,y,move_num,sol,xMove,yMove):
    if move_num == n*n:
        return True 

    for i in range(8):
        x = x + xMove[i]
        y = y + yMove[i]
        if safeKT(x,y,sol,n):
            sol[x][y] = move_num
            if solveKT_h(n,x,y,move_num+1,sol,xMove,yMove):
                return True
            else:
                sol[x][y] = -1
        x = x - xMove[i]
        y = y - yMove[i]
    return False

def safeKT(x,y,sol,n):
    if x >= 0 and x<n and y>=0 and y<n:
        if sol[x][y] == -1:
            return True
    return False

# print solution for knight tour problem

#n = 4
#sol = solveKT(n)
# if sol:
#     for i in range(len(sol)):
#         print sol[i]
# else:
#     print sol



###########################
## rat in a maze problem ##
###########################

# time complexity = O(4^(n^2-1))
def solveMaze(maze):
    sol = []
    n = len(maze)
    print n
    for i in range(n):
        sol.append([])
        for j in range(n):
            sol[i].append(-1)
    
    xMove = [  1, 0, -1,  0 ]
    yMove = [  0, 1,  0, -1 ]
    sol[0][0]  = 0;
 
    if not solveMaze_h(n, 0, 0, 1, sol, xMove, yMove, maze):
        return False
    else:
        return sol
    
def solveMaze_h(n,x,y,move_num,sol,xMove,yMove,maze):
    if x == n-1 and y == n-1:
        return True 

    for i in range(4):
        x = x + xMove[i]
        y = y + yMove[i]
        if safeMaze(x,y,sol,n,maze):
            sol[x][y] = move_num
            if solveMaze_h(n,x,y,move_num+1,sol,xMove,yMove,maze):
                return True
            else:
                sol[x][y] = -1
        x = x - xMove[i]
        y = y - yMove[i]
    return False

def safeMaze(x,y,sol,n,maze):
    if x >= 0 and x<n and y>=0 and y<n:
        if sol[x][y] == -1 and maze[x][y]==1:
            return True
    return False

# print solution for rat in a maze problem

# maze = [[ 1, 0, 0, 0 ],
#         [ 1, 1, 0, 1 ],
#         [ 0, 1, 0, 0 ],
#         [ 1, 1, 1, 1 ]]

# sol = solveMaze(maze)
# if sol:
#     for i in range(len(sol)):
#         print sol[i]
# else:
#     print sol