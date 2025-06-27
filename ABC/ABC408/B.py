N = int(input())
A = list(map(int, input().split()))

# 重複を除いてソート
unique_A = sorted(set(A))

# 重複除去後の個数と要素を出力
print(len(unique_A))
print(*unique_A)