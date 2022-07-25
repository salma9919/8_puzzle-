
import copy
from locale import currency
#from msilib.schema import IniFile
import time
from hashset import *
from hashsetfora import*


Inital_State=125340678
Goal_State=12345678

frontier=[]
explored=[]
depth=[]
Parent_hash = MyHashSet_A()
frontier_hash=MyHashSet()
explored_hash=MyHashSet()   
class Dfs_Bfs:
    def __init__(self):
        self.Goal_State=Goal_State
        self.Initial_State=Inital_State

    @staticmethod
    def twoD_oneD(state):
        oneD=[]
        oneD.extend(state[0])
        oneD.extend(state[1])
        oneD.extend(state[2])
        return oneD
    @staticmethod
    def int_to_oneD(state):

        list=[0,0,0,0,0,0,0,0,0]

        for i in range (0,9):

                list[8-i]=state%10 

                state//=10
        return list 

    @staticmethod
    def swap(row,column,row_new,column_new,state):
            zeroIndex=8-(row*3+column)
            swapIndex=8-(row_new*3+column_new)
            swapped_number=(state//10**swapIndex)%10
            swapped_number%=10
            state-=swapped_number*10**swapIndex
            state+=swapped_number*10**zeroIndex
            return state

    @staticmethod        
    def get_I_J(index):
            Row=index//3
            Column=index%3
        
            return Row , Column
        
    def zero_index(self,Inital_State):
    
        if Inital_State>100000000:
            for i in range (0,9):
                if Inital_State%10==0:
                 return self.get_I_J(8-i)
        
                Inital_State//=10
        else:
         return self.get_I_J(0)   

    def get_path(self,Goal_State,parent,Inital_State):
        path=[]
        state=Goal_State
        while state != Inital_State:
            current_couple=parent.contains(state)
        
            path.append(self.int_to_oneD(current_couple[0]))
            state=current_couple[1]
        return path
    @staticmethod
    def explored_count():
        return(len(explored))
    
    @staticmethod
    def check_child(child,Current_State):
        if explored_hash.contains(child) or frontier_hash.contains(child)  :
                            
            return
        
        else:
            g=Parent_hash.contains(Current_State)[2]
           
            frontier_hash.add(child)
            
            frontier.append(child)
            Parentt=[child,Current_State,g+1]
            depth.append(g+1)
            Parent_hash.add(Parentt)   
        return    

        
    def BFS(self,Inital_State,Goal_State,algorithm_chosen=0):
            # Frontier=[]
            # Explored=[]
            # Parent=[0,0]
            
            parents=[Inital_State,Inital_State,0]
            depth.append(0)
            Parent_hash.add(parents)
            count=0
            #Parent.append([int_to_oneD(Inital_State),int_to_oneD(Inital_State),"none"])
            frontier_hash.add(Inital_State)
            frontier.append(Inital_State)
        
            while len(frontier) >0:
                # Current_State=frontier_hash.contains(Inital_State)
                Current_State=copy.deepcopy(frontier[algorithm_chosen])
                frontier_hash.remove(Current_State)
                frontier.remove(Current_State)
                explored_hash.add(Current_State)
                explored.append(Current_State)
                #Explored.append(copy.deepcopy(Current_State))
                if Goal_State == Current_State:
                    

                    #return Parent, True
                    print("search depth:"+str(max(depth)))
                    return  Parent_hash,True
                else:
                    
            
                        
                    # getting the row and colum indecees of current state
                    
                    row,column=self.zero_index(Current_State)
                
                
                

                    

                    #case of numebr moved upwards  
                    if row + 1 < 3:
                    
                        child=self.swap(row,column,row+1,column,Current_State)
                        self.check_child(child,Current_State)

                        
                        
                            #Parent.append([int_to_oneD(child),int_to_oneD(Current_State),"up"])
                        
                    #case of number moved downwards 
                    if row - 1 >= 0:
                        
                        child=self.swap(row,column,row-1,column,Current_State)
                        
                        self.check_child(child,Current_State)
                        
                    

                    #case of number moved right
                    if column - 1 >= 0:
                    
                        child=self.swap(row,column,row,column-1,Current_State)
                        
                        self.check_child(child,Current_State)
                            
                    
                    #case of number moved left
                    if column + 1 < 3:
                    
                        child=self.swap(row,column,row,column+1,Current_State)
                        
                        self.check_child(child,Current_State)
                        
                    # print(Parent_hash.hash_table)
                    # print(frontier_hash.hash_table)
            return Parent_hash,False
        


# Inital_State=[[1,2,5],
#               [3,4,0],
#               [6,7,8]]
# Goal_State=[[0,1,2],
#             [3,4,5],
#             [6,7,8]]


# parent,result,count=BFS(Inital_State,Goal_State)
# path=get_path(Goal_State,parent,Inital_State)
# print(path)



# parent , found = BFS(Inital_State,Goal_State)
# print("found state = "+str(found))
# for i in parent:

#      print("state:"+str(i[0]))
 
# for i in range(0,len(parent)):
#     print("node number:"+str(i))
#     print("myparent:")
#     print(parent[i][1][0])
#     print(parent[i][1][1])
#     print(parent[i][1][2])
#     print("child:")
#     print(parent[i][0][0])
#     print(parent[i][0][1])
#     print(parent[i][0][2])
#get path

 

# print("path:")
# # path=get_path(int_to_oneD(Goal_State),parent,int_to_oneD(Inital_State))
# # print(path)
# # #print path

# def print_path(path):
#     for i in range(0,len(path)):
#         print("node number:"+str(i))
#         print("myparent:")
#         print(path[len(path)-i-1][0][0])
#         print(path[len(path)-i-1][0][1])
#         print(path[len(path)-i-1][0][2])



