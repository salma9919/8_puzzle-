
import copy
from locale import currency
from msilib.schema import IniFile
import time
import hashset

def twoD_oneD(state):
    oneD=[]
    oneD.extend(state[0])
    oneD.extend(state[1])
    oneD.extend(state[2])
    return oneD

def int_to_oneD(state):

    list=[0,0,0,0,0,0,0,0,0]

    for i in range (0,9):

            list[8-i]=state%10 

            state//=10
    return list 


def swap(row,column,row_new,column_new,state):
        zeroIndex=8-(row*3+column)
        swapIndex=8-(row_new*3+column_new)
        swapped_number=(state//10**swapIndex)%10
        swapped_number%=10
        state-=swapped_number*10**swapIndex
        state+=swapped_number*10**zeroIndex
        return state
        

      
def zero_index(Inital_State):
 
    if Inital_State>100000000:
        for i in range (0,9):
            if Inital_State%10==0:
             return 8-i
    
            Inital_State//=10
    else:
     return 0     
                
def BFS(Inital_State,Goal_State,algorithm_chosen=0):
        Frontier=[]
        Explored=[]
        Parent=[]
        Parent.append([int_to_oneD(Inital_State),int_to_oneD(Inital_State),"none"])
        Frontier.append(Inital_State)
        while len(Frontier)>0:
            Current_State=copy.deepcopy(Frontier[algorithm_chosen])
            Frontier.remove(Current_State)
            Explored.append(copy.deepcopy(Current_State))
            if Goal_State == Current_State:
                

                return Parent, True
            else:
                
         
                    
                zero=zero_index(Current_State)
              
                
                row=zero//3
                column=zero%3
            
            

                

                #case of numebr moved upwards  
                if row + 1 < 3:
                    
                    child=swap(row,column,row+1,column,copy.deepcopy(Current_State))
                   
                    if  child in Explored or child in Frontier  :
                        pass
                    else:
                     
                        Frontier.append(copy.deepcopy(child))
                        Parent.append([int_to_oneD(child),int_to_oneD(Current_State),"up"])
                      
                #case of number moved downwards 
                if row - 1 >= 0:
                   
                    child=swap(row,column,row-1,column,copy.deepcopy(Current_State))
                    
                    if child in Explored or child in Frontier:
                        pass
                    else:
                 
                        Frontier.append(copy.deepcopy(child))
                        Parent.append([int_to_oneD(child),int_to_oneD(Current_State),"down"])
                   

                #case of number moved right
                if column - 1 >= 0:
                    
                    child=swap(row,column,row,column-1,copy.deepcopy(Current_State))
                    
                    if child in Explored or child in Frontier :
                        pass
                    else:
                     
                        Frontier.append(copy.deepcopy(child))
                        Parent.append([int_to_oneD(child),int_to_oneD(Current_State),"right"])
                 
                #case of number moved left
                if column + 1 < 3:
                    
                    child=swap(row,column,row,column+1,copy.deepcopy(Current_State))
                    
                    if child in Explored or child in Frontier :
                        pass
                    else:
                   
                        Frontier.append(copy.deepcopy(child))
                        Parent.append([int_to_oneD(child),int_to_oneD(Current_State),"left"])
                    
        
             
                
        

        return Parent,False


# Inital_State=[[1,2,5],
#               [3,4,0],
#               [6,7,8]]
# Goal_State=[[0,1,2],
#             [3,4,5],
#             [6,7,8]]
Inital_State=125340678
Goal_State=12345678



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
# print("path:")
# path=get_path(int_to_oneD(Goal_State),parent,int_to_oneD(Inital_State))
# print(path)
# #print path

def print_path(path):
    for i in range(0,len(path)):
        print("node number:"+str(i))
        print("myparent:")
        print(path[len(path)-i-1][0][0])
        print(path[len(path)-i-1][0][1])
        print(path[len(path)-i-1][0][2])



