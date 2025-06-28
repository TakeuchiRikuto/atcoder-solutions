T=int(input())
for i in range(T):
    counts=2
    N=int(input())#個数
    S=list(map(int,input().split()))#S[N-1]<2[0]
    used = set() 
    used.add(0)
    used.add(N-1)
    current=0
    while 2*S[current]<S[N-1]:
      candidates = [(i, S[i]) for i in range(N) 
                  if i not in used and S[i] <= 2*S[current]]
      if not candidates:  # 候補がない = -1
        counts = -1
        break
      next_index, next_value = max(candidates, key=lambda x: x[1])
      used.add(next_index)
      current = next_index
      counts += 1
    print(counts)
      #グリーディ2*S[i]に最も近いもの探すそれが最後のS[N-1]より小さければ終了