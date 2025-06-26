N=int(input())
T=input()
A=input()
found=False
for i in range(N):
  if T[i]=="o" and A[i]=="o":
    print("Yes")
    found=True
    break
if not found:
  print("No")