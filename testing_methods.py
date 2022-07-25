
# def int_to_oneD(state):

#         list=[0,0,0,0,0,0,0,0,0]

#         for i in range (0,9):

#                 list[8-i]=state%10 

#                 state//=10
#         return list

# def validation(state):
#     state=int_to_oneD(state)
#     print(len(state))
#     for i in range(0,len(state)):
#         print("i="+str(state[i]))
#         for j in range(1+i,len(state)):
#             print("j="+str(state[j]))
#             if state[i] == state[j]:
#                 return False
#     return True
# list=12345678
# print(validation(list))


import heapdict
  
h = heapdict.heapdict()
  
# Adding pairs into heapdict
h['123456789']= 1
h['876543210']= 2
h['12345678900']= 3
h['99999999999']= 4
  
print('list of key:value pairs in h:\n', list(h.items()))
print('pair with lowest priority:\n', h.peekitem())
print('list of keys in h:\n',list(h.keys()))
print('list of values in h:\n',list(h.values()))


print('remove pair with lowest priority:\n',)
h['12345678900']=0
print('get value for key 5 in h:\n',h.get('12345678900', False))
# val=h.get('8765432310', False)
# if val:
#     print("found")
# else:
#     print("not")

# # clear heapdict h
# h.clear()
print(list(h.items()))