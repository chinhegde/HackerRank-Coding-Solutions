n=int(input())
s1=set(map(int,input().split()))
n=int(input())
s2=set(map(int,input().split()))
print(len(s1.union(s2)-s1.intersection(s2)))

