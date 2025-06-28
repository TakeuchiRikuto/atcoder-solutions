N=int(input())
counts=0
for i in range(N):
  A,B=map(int,input().split())
  if A<B:
    counts+=1
print(counts)