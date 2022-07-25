
import math
from typing import Counter
import heapdict
from hashsetfora import*

Inital_State=125340678
Goal_State=12345678

indicieas=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
# frontier=[]
explored={}
# parent=[]
parent = MyHashSet_A()
depth=[]
frontier = heapdict.heapdict()
class A_star:
    def __init__(self):
        self.Goal_State=Goal_State
        self.Initla_State=Inital_State
        pass
    def swap(self,row, column, row_new, column_new, state):
        zeroIndex = 8 - (row * 3 + column)
        swapIndex = 8 - (row_new * 3 + column_new)
        swapped_number = (state // 10 ** swapIndex) % 10
        swapped_number %= 10
        state -= swapped_number * 10 ** swapIndex
        state += swapped_number * 10 ** zeroIndex
        return state
        
    def zero_index(self,Inital_State):
        if Inital_State > 100000000:
            for i in range(0, 9):
                if Inital_State % 10 == 0:
                    return self.index_to_i_j (8 - i)

                Inital_State //= 10
        else:
            return self.index_to_i_j(0)

    def in_frontier(self,child,frontier):
        val=frontier.get(child, False)
        if val:
            return val
        else:
            return False

    # def get_from_frontier(self,child,frontier):
    #     for i in range(0,len(frontier)):
    #         if child==frontier[i][0]:
    #             return frontier[i]
    #     return False


    def get_from_parent(self,child,parent):
        
        return parent.contains(child)
        
        

    def get_min(self,listt):
        min=1000
        cell=[]
        for i in range(0,len(listt)):
            if min>listt[i][1]:
                min=listt[i][1]
                cell=listt[i]
        return cell
    
    def index_to_i_j(self,i):
        row = i // 3
        column = i % 3
        return row,column


    def int_to_oneD(self,state):
        list=[0,0,0,0,0,0,0,0,0]
        for i in range (0,9):
                list[8-i]=state%10
                state//=10
        return list

    def get_I_J(self,index):
            Row=index//3
            Column=index%3
            return Row , Column
    
    def manhaten(self,state):
        total=0
        manhaten = []
        trace=[]
        if state > 100000000:
            for i in range(0,9):
                row, column = self.index_to_i_j(8 - i)
                manhaten.append(abs(row - indicieas[state % 10][0]) + abs(column - indicieas[state % 10][1]))
                trace.append(state%10)
                state //= 10
        else :manhaten.append(0)
        for ele in range(0, len(manhaten)):
            total = total + manhaten[ele]
        return total

    def Euclidean(self,state):
        total=0
        Euclidean = []
        if state > 100000000:
            for i in range(0,9):
                row, column = self.index_to_i_j(8 - i)
                Euclidean.append( math.sqrt((row - indicieas[state % 10][0])**2 + (column - indicieas[state % 10][1])**2))
                state //= 10
        else:
            Euclidean.append(0)
        for ele in range(0, len(Euclidean)):
            total = total + Euclidean[ele]
        return total


    def get_path(self,Goal_State,parent,Inital_State):
        path=[]
        state=Goal_State
        while state != Inital_State:
            current_couple=parent.contains(state)
        
            path.append(self.int_to_oneD(current_couple[0]))
            state=current_couple[1]
        return path


    def explored_count(self):
        return(len(explored))

            
    def check_child(self,child,current_state,huristic):
        if str(child) in explored:
                return

        else:
            #g=get_from_frontier(current_state,parent)[2]

            temp = self.in_frontier(child, frontier)
            if temp==False :
                g=self.get_from_parent(current_state[0],parent)[2]
           
                f=g+huristic(child)+1
                frontier[str(child)]=f
                parent.add([child,current_state[0],g+1])
                depth.append(g+1)
            else:
                g = self.get_from_parent(current_state[0], parent)[2]
            
                f = g + huristic(child) + 1
                if f < int(temp):
                    frontier[str(child)]=f
                    temp_in_parent=self.get_from_parent(child,parent)
                    parent.remove(temp_in_parent)
                    parent.add([child,current_state[0],g+1])
                    depth.append(g+1)

                else:
                    return
        return


    def BFS(self,Initial_state,Goal_State,algorithm=0):
        # adding in parent child , parent , g
        if algorithm==0:
            huristic=self.manhaten
        else:
            huristic=self.Euclidean
        parent.add([Initial_state,Initial_state,0])
        frontier[str(Initial_state)]=0
        while len(list(frontier.items()))>0:
            #current_statee is a list of the state and cost
            current_state=list(frontier.popitem())
            current_state=[int(current_state[0]),current_state[1]]
          
            #appending the state only in the explored
            explored[str(current_state[0])]=0
            temp=[]
            if Goal_State==current_state[0]:
                print("search depth:"+str(max(depth)))
                return parent,True
            else:
                row,column = self.zero_index(current_state[0])
                # up case
                if row + 1 < 3:
                    child = self.swap(row, column, row + 1, column, current_state[0])
                    self.check_child(child,current_state,huristic)
                 
                # down case
                if row - 1 >= 0:
                    child = self.swap(row, column, row -1, column, current_state[0])
                    self.check_child(child,current_state,huristic)
                 
                # right case
                if column - 1 >= 0:
                    child = self.swap(row, column, row, column - 1,current_state[0])
                    self.check_child(child,current_state,huristic)
               
                # left case  
                if column + 1 < 3:
                    child = self.swap(row, column, row, column + 1,current_state[0])
                    self.check_child(child,current_state,huristic)
                   
        return parent,False

    # for i in range(0,len(parent)):
    #     parent[i][0]=int_to_oneD(parent[i][0])
    #     parent[i][1]=int_to_oneD(parent[i][1])

    # B_star(Inital_State,Goal_State)s
    # path=[]
    # path=get_path(Goal_State,parent,Inital_State)
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




