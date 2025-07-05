"""from collections import deque 

Q=int(input())
A=deque()
for k in  range(Q):
  query=list(map(int,input().split()))
  if query[0]==1:
    for i in range(query[1]):
      A.append(query[2])
  elif query[0]==2:
    pop_sum=0
    for j in range(query[1]):
      pop_sum=pop_sum+A.popleft()
    print(pop_sum)
"""
##dequeの大切さ
##計算量が多い時はタプルなどで保存→保存方法の大切さ
from collections import deque 

Q=int(input())
A=deque()
for k in  range(Q):
  query=list(map(int,input().split()))
  if query[0]==1:
      A.append((query[2], query[1]))#(value, count)
  elif query[0]==2:
    k = query[1]
    pop_sum = 0
    while k>0:
        value,count=A[0]
        if count <= k:
            pop_sum += value*count
            k -= count
            A.popleft()
        else:
            pop_sum += value*k
            A[0] = value,count-k
            k=0
    print(pop_sum)
"""
from collections import deque

Q = int(input())

A = deque()

for i in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        c, x = query[1], query[2]
        A.append((x, c))
    
    elif query[0] == 2:
        k = query[1]
        pop_sum = 0
        
        while k > 0:
            value, count = A[0] 
            
            if count <= k:
                pop_sum += value * count
                k -= count
                A.popleft()
            else:
                pop_sum += value * k
                A[0] = (value, count - k)
                k = 0
        
        print(pop_sum)
"""