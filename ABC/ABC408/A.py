N,S=map(int,input().split())
T=list(map(int,input().split()))
cheek_sleep=True
if T[0]>=S+0.5:
  cheek_sleep=False
  print("No")
if cheek_sleep:
  for i in range(N-1):
    if T[i+1]-T[i]>=S+0.5:
      cheek_sleep=False
      break
  if cheek_sleep:
    print("Yes")
  else:
    print("No")