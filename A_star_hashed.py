
import math
inititial_state=125340678
Goal_state=12345678


def swap(row, column, row_new, column_new, state):
    zeroIndex = 8 - (row * 3 + column)
    swapIndex = 8 - (row_new * 3 + column_new)
    swapped_number = (state // 10 ** swapIndex) % 10
    swapped_number %= 10
    state -= swapped_number * 10 ** swapIndex
    state += swapped_number * 10 ** zeroIndex
    return state
    
def zero_index(Inital_State):
    if Inital_State > 100000000:
        for i in range(0, 9):
            if Inital_State % 10 == 0:
                return 8 - i

            Inital_State //= 10
    else:
        return 0

def in_frontier(child,frontier):
    for i in range(0,len(frontier)):
        if child==frontier[i][0]:
            return True
        else:
            return False
def get_from_frontier(child,frontier):
    for i in range(0,len(frontier)):
        if child==frontier[i][0]:
            return frontier[i]
    return False
def get_from_parent(child,parent):
    for i in range(0,len(parent)):
        if child==parent[i][0]:
            return parent[i]
    return False
def get_min(listt):
    min=1000
    cell=[]
    for i in range(0,len(listt)):
        if min>listt[i][1]:
            min=listt[i][1]
            cell=listt[i]
    return cell
def index_to_i_j(i):
    row = i // 3
    column = i % 3
    return row,column
indicieas=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
def int_to_oneD(state):

    list=[0,0,0,0,0,0,0,0,0]

    for i in range (0,9):

            list[8-i]=state%10

            state//=10
    return list


def manhaten(state):
    total=0
    manhaten = []
    trace=[]
    if state > 100000000:
        for i in range(0,9):
            row, column = index_to_i_j(8 - i)
            manhaten.append(abs(row - indicieas[state % 10][0]) + abs(column - indicieas[state % 10][1]))
            trace.append(state%10)
            state //= 10
    else :manhaten.append(0)
    for ele in range(0, len(manhaten)):
        total = total + manhaten[ele]
    return total

def Euclidean(state):
    total=0
    Euclidean = []
    if state > 100000000:
        for i in range(0,9):
            row, column = index_to_i_j(8 - i)
            Euclidean.append( math.sqrt((row - indicieas[state % 10][0])**2 + (column - indicieas[state % 10][1])**2))
            state //= 10
    else:
        Euclidean.append(0)
    for ele in range(0, len(Euclidean)):
        total = total + Euclidean()[ele]
    return total

frontier=[]
explored=[]
parent=[]
def B_star(Initial_state,Goal_state):


    # adding in parent child , parent , g
    parent.append([Initial_state,Initial_state,0])
    frontier.append([Initial_state,0])
    while len(frontier)>0:
        #current_statee is a list of the state and cost
        current_state=get_min(frontier)

        #appending the state only in the explored
        explored.append(current_state[0])
        temp=[]
        if Goal_state==current_state[0]:
            return parent,True
        else:
            zero = zero_index(current_state[0])
            row = zero // 3
            column = zero % 3
        if row + 1 < 3:

            child = swap(row, column, row + 1, column, current_state[0])

            if child in explored :
                pass

            else:
                #g=get_from_frontier(current_state,parent)[2]

                temp = get_from_frontier(child, frontier)
                if temp==False :
                    g=get_from_parent(current_state[0],parent)[2]
                    f=g+manhaten(child)+1
                    frontier.append([child,f])
                    parent.append([child,current_state[0],g+1])
                else:
                    g = get_from_parent(current_state[0], parent)[2]
                    f = g + manhaten(child) + 1
                    if f < int(temp[1]):
                        frontier.remove(temp)
                        frontier.append([child,f])
                        temp_in_parent=get_from_frontier(child,parent)
                        parent.remove(temp_in_parent)
                        parent.append([child,current_state[0],g+1])
                    else:
                        pass
        if row - 1 >= 0:

            child = swap(row, column, row -1, column, current_state[0])

            if child in explored :
                pass

            else:
                temp = get_from_frontier(child, frontier)
                if temp==False:
                    g = get_from_parent(current_state[0], parent)[2]
                    f=g+manhaten(child)+1
                    frontier.append([child,f])
                    parent.append([child,current_state[0],g+1])
                else:
                    g = get_from_parent(current_state[0], parent)[2]
                    f = g + manhaten(child) + 1
                    if f<temp[1]:
                        frontier.remove(temp)
                        frontier.append([child,f])
                        temp_in_parent=get_from_frontier(child,parent)
                        parent.remove(temp_in_parent)
                        parent.append([child,current_state[0],g+1])
                    else:
                        pass

        if column - 1 >= 0:

            child = swap(row, column, row, column - 1,current_state[0])

            if child in explored:
                pass

            else:
                temp = get_from_frontier(child, frontier)
                if temp == False:
                    g = get_from_parent(current_state[0], parent)[2]
                    f = g + manhaten(child) + 1
                    frontier.append([child, f])
                    parent.append([child, current_state[0], g + 1])
                else:
                    g = get_from_parent(current_state[0], parent)[2]
                    f = g + manhaten(child) + 1
                    if f < temp[1]:
                        frontier.remove(temp)
                        frontier.append([child, f])
                        temp_in_parent = get_from_frontier(child, parent)
                        parent.remove(temp_in_parent)
                        parent.append([child, current_state[0], g + 1])
                    else:
                        pass
        if column + 1 < 3:
            child = swap(row, column, row, column + 1,current_state[0])

            if child in explored:
                pass

            else:
                temp = get_from_frontier(child, frontier)
                if temp == False:
                    g = get_from_parent(current_state[0], parent)[2]
                    f = g + manhaten(child) + 1
                    frontier.append([child, f])
                    parent.append([child, current_state[0], g + 1])
                else:
                    g = get_from_parent(current_state[0], parent)[2]
                    f = g + manhaten(child) + 1
                    if f < temp[1]:
                        frontier.remove(temp)
                        frontier.append([child, f])
                        temp_in_parent = get_from_frontier(child, parent)
                        parent.remove(temp_in_parent)
                        parent.append([child, current_state[0], g + 1])
                    else:
                        pass
        frontier.remove(current_state)
    return parent

for i in range(0,len(parent)):
    parent[i][0]=int_to_oneD(parent[i][0])
    parent[i][1]=int_to_oneD(parent[i][1])
def get_path(Goal_State,parent,Inital_State):
    path=[]
    state=Goal_State
    while state != Inital_State:
        for i in range(0,len(parent)):
            if parent[i][0]==state:
                path.append(parent[i][0])
                state=parent[i][1]
                break
    return path
#B_star(inititial_state,Goal_state)
path=[]
#path=get_path(Goal_state,parent,inititial_state)
# for i in range(0,len(path)):
#     path[i]=int_to_oneD(path[i])
# def print_path(path):
#     for i in range(0,len(path)):
#         print("node number:"+str(i))
#         print("myparent:")
#         print(path[len(path)-i-1][0][0])
#         print(path[len(path)-i-1][0][1])
#         print(path[len(path)-i-1][0][2])
# print(path)




