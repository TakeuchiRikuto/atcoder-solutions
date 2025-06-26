N=int(input())
A=list(map(int,input().split()))
fig=0
maxfig=0
for i in range(N+1):#1,2,3
  for j in range(N):#0,1,2
    if A[j]>=i:#
      fig+=1#0の場合3. 1の場合3
  if fig>=i:#3>0,3>1, 1>2
    maxfig=i
  fig=0
print(maxfig)