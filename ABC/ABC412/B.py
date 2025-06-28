S=input()
T=input()
S=S[0].lower()+S[1:]#iSSSなどに
is_OK=True
for i in range(len(S)):
    if S[i].isupper():
        if not T.find(S[i-1]) != -1:
            is_OK=False
            break
if is_OK:
    print("Yes")
else:
    print("No")

