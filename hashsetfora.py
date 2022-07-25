# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Buckets:
   def __init__(self):
      self.bucketss=[]

   def update(self, key):
      found=False
      for i,k in enumerate(self.bucketss):
         if key==k:
            self.bucketss[i]=key
            found=True
            break
      if not found:
         self.bucketss.append(key)

   def get(self, key):
      for k in self.bucketss:
         if k[0]==key:
            return k
      return False


   def get_min(self,key):
      min=1000
      t=[]
      for k in self.bucketss:
         if k[1]<min:
            min=k[1]
            t=k
      return t

   def remove(self, key):
      for i,k in enumerate(self.bucketss):
         if key==k:
            del self.bucketss[i]

class MyHashSet_A:
   def __init__(self):
      self.costs =[]
      self.key_space = 1000000
      self.hash_table=[Buckets() for i in range(self.key_space)]
   def add(self, state):
      hash_key=state[0]%self.key_space
      self.hash_table[hash_key].update(state)
   def remove(self, key):
      hash_key=key[0]%self.key_space
      self.hash_table[hash_key].remove(key)
   def get_bucket(self,key):
      hash=key[0]%self.key_space
      return self.hash_table[hash].get(key)
      #print(self.hash_table[hash].bucket)
   def contains(self, key):
      hash_key=key%self.key_space
      return self.hash_table[hash_key].get(key)

# ob = MyHashSet_A()
#child,currrentstate
#ob.add(([111111,2222222]))
# cost,state
# for A*
# state=[111111,123456780]
# state1=[111111,56780123]
# ob.add(state)
# ob.add(state1)
# print(ob.get_bucket(state))
# print(ob.get_bucket(state)[0])
# print(ob.get_bucket(state)[1])
# ob.remove(state1)
# print(ob.get_bucket(state1))

#for BFS AND DFS
# state=[123456780]
# state1=[56780123]
# ob.add(state)
# ob.add(state1)
# print(ob.get_bucket(state)[0])
# print(ob.get_bucket(state1)[0])
# ob.remove(state1)
# print(ob.get_bucket(state1))
#ob.add([[[1111]]])
# ob.add(3)
# print(ob.contains(1))
# print(ob.contains(2))
# ob.add(2)
# print(ob.contains(2))
# ob.remove(2)

