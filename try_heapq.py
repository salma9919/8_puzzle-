import heapq as hq
  
# list of students
list_stu = [(1,12345678),(9,888),(3,797644),(2,65789),(4,45679)]
  
# Arrange based on the roll number
hq.heapify(list_stu)
  
print("The order of presentation is :")          
print(hq.heappop(list_stu))
hq.heappush(list_stu,(5,'bheema'))
for i in list_stu:
  print(i[0],':',i[1])