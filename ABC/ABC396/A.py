N=int(input())
A=list(map(int,input().split()))
is_true=False
for i in range(len(A)-2):
  if A[i]==A[i+1]==A[i+2]:
    is_true=True
    break
if is_true:
  print("Yes")
else:
  print("No")