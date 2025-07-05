N=int(input())
S=[]
for i in range(N):
  S.append(input())#Sの中には各文字列
S_con=[]
#各文字列を組み合わせたものを作る
for i in range(N):
  for j in range(N):
    if i!=j:
      S_con.append(S[i]+S[j])
#重複を削除する。
print(len(set(S_con)))