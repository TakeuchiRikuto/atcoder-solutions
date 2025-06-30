N,M=map(int,input().split())
total=0
is_inf=False
for i in range(M+1):
  total=total+N**i
  if total>10**9:
    is_inf=True
    break
  
if not is_inf:
  print(total)
else:
  print("inf")