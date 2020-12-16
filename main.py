from collections import Counter
n=int(input())
word=[]
for i in range(0,n):
    word.append(input())
l=Counter(word)

print(len(set(word)))

for i in l.values():
    print(i,end=" ")
